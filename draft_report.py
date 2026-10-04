def draft_report_v1(flagged_regions, metrics):
    # flagged_regions union 8: Bengaluru only Apr->May, Vijayawada only May->Jun, rest 6 both
    unique=sorted(set(flagged_regions))
    report=[]
    for r in unique:
        m=metrics[r]
        ctx=f"Context: {r} flagged MoM >8% threshold. Sales Apr {m['2026-04']}, May {m['2026-05']}, Jun {m['2026-06']} from pharmeasy.db"
        ins=f"Insight: Apr->May {m['apr_may_change']:.2f}% May->Jun {m['may_jun_change']:.2f}% via (Cur-Prev)/Prev*100"
        imp="Implication: Worth human glance, not proof shift. Single block covers both transitions if flagged twice."
        report.append(f"{ctx}\n{ins}\n{imp}")
    return "\n\n".join(report)
