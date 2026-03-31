"""Consolidate SMS_Manual_Test_Cases.csv: one row per test case, Steps and Expected Result in single cells."""
import csv
from collections import defaultdict

INPUT_PATH = "c:/Users/sanjay.waghmare/SOLUTO/docs/SMS_Manual_Test_Cases.csv"
OUTPUT_PATH = "c:/Users/sanjay.waghmare/SOLUTO/docs/SMS_Manual_Test_Cases.csv"

def main():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    # header: Test Case ID, Title, Scenario, Priority, Step, Action, Expected Result, Expected Result (Overall), subscriberId, mdn, ...
    idx = {h: i for i, h in enumerate(header)}
    tc_id_i = idx["Test Case ID"]
    title_i = idx["Title"]
    scenario_i = idx["Scenario"]
    priority_i = idx["Priority"]
    step_i = idx["Step"]
    action_i = idx["Action"]
    exp_result_i = idx["Expected Result"]
    overall_i = idx["Expected Result (Overall)"]

    # Group by Test Case ID (order preserved by list)
    groups = defaultdict(list)
    for row in rows:
        if len(row) > max(tc_id_i, action_i, exp_result_i):
            groups[row[tc_id_i]].append(row)

    out_rows = []
    for row in rows:
        tid = row[tc_id_i]
        if tid not in groups:
            continue
        group = groups.pop(tid)
        if not group:
            continue
        first = group[0]
        steps_actions = []
        steps_results = []
        for r in group:
            step_num = r[step_i] if step_i < len(r) else ""
            act = r[action_i] if action_i < len(r) else ""
            res = r[exp_result_i] if exp_result_i < len(r) else ""
            steps_actions.append(f"{step_num}. {act}".strip())
            steps_results.append(f"{step_num}. {res}".strip())
        combined_action = "\n".join(steps_actions)
        combined_result = "\n".join(steps_results)
        out_row = [
            first[tc_id_i],
            first[title_i],
            first[scenario_i],
            first[priority_i],
            "",  # Step - empty when consolidated
            combined_action,
            combined_result,
            first[overall_i],
        ]
        for k in ["subscriberId", "mdn", "serviceEnabled", "kfsServiceEnabled", "appleSubscriptionEnabled", "birthday", "gender", "brand"]:
            if k in idx and idx[k] < len(first):
                out_row.append(first[idx[k]])
        out_rows.append(out_row)

    out_header = ["Test Case ID", "Title", "Scenario", "Priority", "Step", "Action", "Expected Result", "Expected Result (Overall)",
                  "subscriberId", "mdn", "serviceEnabled", "kfsServiceEnabled", "appleSubscriptionEnabled", "birthday", "gender", "brand"]

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(out_header)
        w.writerows(out_rows)

    print(f"Wrote {len(out_rows)} test cases to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
