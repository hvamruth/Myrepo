import os
import openai

def chat_with_gpt3(prompt):
    api_key = "YOUR_API_KEY"  # Replace this with your actual API key from OpenAI

    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )

    if "choices" in response:
        return response["choices"][0]["text"].strip()
    else:
        return f"Error: {response['error']['message']}"

# Example usage:
prompt = "Once upon a time"
response_text = chat_with_gpt3(prompt)
print(response_text)
