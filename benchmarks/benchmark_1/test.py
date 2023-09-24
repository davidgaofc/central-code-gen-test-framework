import json
test_results = {"pass": 99, "fail": 1}

json_output = json.dumps(test_results, indent=4)
print(json_output)