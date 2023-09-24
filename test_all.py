import os
import json
import subprocess

# Define the root directory where you have multiple folders
root_directory = "benchmarks/"

# Load the JSON configuration file
config_file = "benchmarks.json"

try:
    with open(config_file, "r") as json_file:
        config_data = json.load(json_file)
except FileNotFoundError:
    print(f"Config file not found: {config_file}")
    exit(1)
except json.JSONDecodeError:
    print(f"Error parsing JSON in config file: {config_file}")
    exit(1)

# Define the directory where stdout files will be saved
output_directory = "results/"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through each benchmark in the configuration
for benchmark_name, benchmark_info in config_data.items():
    folder_name = benchmark_info.get("folder_name")
    test_script = benchmark_info.get("evaluation_script")

    if not folder_name or not test_script:
        print(f"Invalid configuration for benchmark: {benchmark_name}")
        continue

    folder_path = os.path.join(root_directory, folder_name)
    test_script_path = os.path.join(folder_path, test_script)

    # Check if the "generation_script" exists in the folder
    # print(folder_path, test_script_path)
    if os.path.isfile(test_script_path):
        # Define the output file path
        output_file = os.path.join(output_directory, f"{benchmark_name}_stdout.json")
        # print(output_file)

        # Run the "generation_script" and capture stdout
        try:
            with open(output_file, "w") as stdout_file:
                subprocess.run(
                    ["python", test_script_path],
                    stdout=stdout_file,
                    stderr=subprocess.STDOUT,
                )

            print(f"Executed {test_script} for {benchmark_name}.")
        except Exception as e:
            print(f"Error running {test_script} for {benchmark_name}: {str(e)}")
    else:
        print(f"Generation script not found for benchmark: {benchmark_name}")