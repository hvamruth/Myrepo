import openai
import pyttsx3
import pyspeech
import os

# Set your OpenAI API key here
openai.api_key = 'OPENAI.API_KEY'

# Text-to-speech setup using pyttsx3
engine = pyttsx3.init()

def chat_with_gpt3(prompt):
    try:
        # Make a request to the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can also use "gpt-3.5-turbo" for this integration
            prompt=prompt,
            max_tokens=150,
            stop=None,
            temperature=0.7,
        )

        # Extract the response from the API and print it
        answer = response.choices[0].text.strip()
        print("AI: " + answer)

        # Speak the answer
        engine.say(answer)
        engine.runAndWait()

    except Exception as e:
        print("Error: ", str(e))

# Main loop
if __name__ == "__main__":
    print("AI: Hello! I am your AI assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("AI: Goodbye!")
            break
        else:
            chat_with_gpt3("You: " + user_input + "\nAI:")
