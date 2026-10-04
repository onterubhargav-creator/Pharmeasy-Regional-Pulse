import json, datetime, uuid
def review_gate_v1(report, decision, reviewer_notes=""):
    if decision not in ("approve","edit","reject"):
        raise ValueError(f"Invalid {decision}")
    entry={"timestamp":datetime.datetime.now().isoformat(),"run_id":str(uuid.uuid4())[:8],"region":"Guntur","decision":decision,"reviewer_note":reviewer_notes}
    with open("audit_log.jsonl","a") as f: f.write(json.dumps(entry)+"\n")
    return {"report":report,"decision":decision,"external_use_allowed":decision=="approve","audit_entry":entry}

if __name__=="__main__":
    for d,n in [("approve","Verified Part2 SQL"),("edit","Add order-mix"),("reject","Unverified external")]:
        print(f"Before {d}"); print(review_gate_v1("Guntur +122.19% draft",d,n))
