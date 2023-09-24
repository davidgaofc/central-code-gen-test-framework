import json

test_results = {"pass": 90, "fail": 10}

json_output = json.dumps(test_results, indent=4)
print(json_output)