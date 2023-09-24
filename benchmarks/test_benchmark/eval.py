import json

test_results = {"pass": 80, "fail": 20}

json_output = json.dumps(test_results, indent=4)
print(json_output)