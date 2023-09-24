import os
import json

# Define the directory where JSON result files are located
result_directory = "results/"

# Initialize variables to store aggregated pass and fail counts
total_pass_count = 0
total_fail_count = 0

# Iterate through JSON files in the result directory
for filename in os.listdir(result_directory):
    if filename.endswith(".json"):
        file_path = os.path.join(result_directory, filename)

        # Load the JSON file
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)

            # Check if the JSON data contains "pass" and "fail" keys
            if "pass" in data and "fail" in data:
                pass_count = data["pass"]
                fail_count = data["fail"]
                total_pass_count += pass_count
                total_fail_count += fail_count
        except json.JSONDecodeError as e:
            print(f"Error loading JSON file {filename}: {e}")

# Print the aggregated results
print(f"Total pass count from JSON files: {total_pass_count}")
print(f"Total fail count from JSON files: {total_fail_count}")