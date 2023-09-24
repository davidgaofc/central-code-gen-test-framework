import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")
import openai

api_key = "YOUR_API_KEY"
def llm_call(prompt):
    # openai.api_key = api_key
    # response = openai.Completion.create(
    #     engine="davinci",  # Choose the engine you want to use
    #     prompt=prompt,
    #     max_tokens=100  # Adjust the max_tokens as needed
    # )
    #
    # if response.choices:
    #     return response.choices[0].text
    # else:
    #     return None

    return("llm_call " + prompt)