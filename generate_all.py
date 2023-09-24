import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

import os
import json

# Define the root directory where you have multiple folders
root_directory = "benchmarks/"

# Load the JSON configuration file
config_file = "benchmarks.json"

def main():
    print("compiling ai generated code ... ")
    try:
        with open(config_file, "r") as json_file:
            config_data = json.load(json_file)
    except FileNotFoundError:
        print(f"Config file not found: {config_file}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error parsing JSON in config file: {config_file}")
        exit(1)

    # Iterate through each benchmark in the configuration
    for benchmark_name, benchmark_info in config_data.items():
        folder_name = benchmark_info.get("folder_name")
        generation_script = benchmark_info.get("generation_script")
        evaluation_script = benchmark_info.get("evaluation_script")

        if not folder_name or not generation_script:
            print(f"Invalid configuration for benchmark: {benchmark_name}")
            continue

        folder_path = os.path.join(root_directory, folder_name)
        generate_script_path = os.path.join(folder_path, generation_script)
        # Check if the "generation_script" exists in the folder
        if os.path.isfile(generate_script_path):
            # Run the "generation_script" in the folder
            try:
                os.system(f"python {generate_script_path}")
            except Exception as e:
                print(f"Error running {generation_script} in {folder_name}: {str(e)}")
        else:
            print(f"Generation script not found for benchmark: {benchmark_name}")

main()