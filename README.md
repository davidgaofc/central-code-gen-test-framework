# Generative AI Benchmarking Framework 🤖📊

Welcome to the most comprehensive framework for benchmarking generative AI models! If you're looking to understand the strengths, weaknesses, and capabilities of your generative AI, you're in the right place. Our framework aggregates multiple benchmarks, enabling you to assess AI performance across a spectrum of tasks, all in one go!

## Features 🔥

- **Unified Framework**: Bring together multiple benchmarks under one roof.
- **Easy Testing**: Just a few scripts away from generating results and understanding the prowess of your AI.
- **Aggregated Scoring**: We provide a holistic score taking into consideration various benchmarks, giving you a full view of AI capability.

## Getting Started 🚀

1. **Clone the Repository**
    ```
    git clone https://github.com/davidgaofc/central-code-gen-test-framework.git
    cd central-code-gen-test-framework
    ```

2. **Install Dependencies**

3. **Setting Up Your Model**

    Make sure to place your generative AI model inside the `llm_call` file and insert the necessary API call.

## Running the Framework 🖥

Here's a quick overview of how you can run the entire benchmarking:

1. **Generate AI Responses**
    ```bash
    python generate_all.py
    ```
    This will generate outputs from your AI for all the benchmarks included in the framework.

2. **Run Benchmark Tests**
    ```bash
    python test_all.py
    ```
    This will run the benchmark tests on the generated outputs and produce a score for each individual test.

3. **Aggregate Results**
    ```bash
    python total_results.py
    ```
    Fetch an aggregated score for your AI across all the benchmarks. This will give you an overall perspective on how well your AI performs.

## Contribution 🙌

Your contributions are always welcome! If you have a new benchmark test or improvement in mind, don't hesitate to fork, modify, and make a pull request.

## Support and Feedback 📧

For any inquiries, issues, or feedback, please open an issue in the repository or contact David.

---

## Instructions for Integrating Your Own Benchmark 🛠

Want to add a new benchmark to our framework? Awesome! Follow these simple steps to seamlessly integrate your benchmark and expand the capabilities of our testing environment:

1. **Clone the Repository (if you haven't already)**
    ```
    git clone https://github.com/davidgaofc/central-code-gen-test-framework.git
    cd central-code-gen-test-framework
    ```

2. **Move Your Benchmark Directory**

    Transfer your benchmark's directory/folder into the `benchmarks` folder of the project.

    ```
    mv path/to/your/benchmark benchmarks/
    ```

    Make sure your benchmark structure is consistent with the conventions described in `benchmarks/README.md`.

3. **Update the `benchmark.json`**

    Navigate to `benchmark.json` and add an entry for your benchmark:

    ```json
    {
        "benchmark_name": {
            "path": "name of your benchmark directory",
            "generation_script": "your file in the benchmark directory that generates outputs",
            "evaluation_script": "your file in the benchmark directory that runs the tests"
        }
    }
    ```

4. **Make Sure your scripts fit the expected output**
    - Generation Script: Your generation script can do whatever you want.
    - Evaluation Script: Your evaluation script should output a json structured like the following to stdout (print).
   ```json
   {
    "pass": 99,
    "fail": 1
    }
    ```
5. **Implement Centralized API Call (Optional)**

    If you are loading in multiple benchmarks, it may be beneficial to implement llm_call.py as you see fit so all benchmarks can use the same LLM generation.

---

**Join our community and let's push the boundaries of what generative AI can achieve! 🌟**
