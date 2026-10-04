import json
def compute_percentage_change_v1(current, previous):
    if previous==0 or previous is None: return 0
    return (current-previous)/previous*100

def flag_significant_regions_v1(changes, threshold=8):
    return [r for r,c in changes.items() if abs(c)>threshold]

def save_state_v1(data, path="state.json"):
    json.dump(data, open(path,'w'), indent=2)

def load_previous_state_v1(path="state.json"):
    return json.load(open(path))

# Example: Guntur Apr->May +122.19% flagged, union 8 unique regions
