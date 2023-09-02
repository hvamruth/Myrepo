import openai
import os
import pyttsx3
import tkinter as tk

from tkinter import Scrollbar, Text

# Set your OpenAI API key here
openai.api_key = "api key omitted 😉 "
engine="davinci",
prompt="Once upon a time",
max_tokens=5

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


        # Extract the response from the API and return it
        return response.choices[0].text.strip()

    except Exception as e:
        print("Error: ", str(e))
        return "Error: Something went wrong."

def speak(answer):
    # Speak the answer
    engine.say(answer)
    engine.runAndWait()

def process_input():
    user_input = user_input_text.get("1.0", tk.END).strip()
    if user_input.lower() in ['exit', 'quit', 'bye']:
        output_text.insert(tk.END, "AI: Goodbye!\n")
        speak("Goodbye!")
        root.quit()
    else:
        ai_response = chat_with_gpt3("You: " + user_input + "\nAI:")
        output_text.insert(tk.END, "AI: " + ai_response + "\n")
        speak(ai_response)

# Create the main application window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x500")

# Create input and output text boxes
user_input_text = Text(root, wrap=tk.WORD, width=40, height=5)
user_input_text.pack(pady=20)

scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = Text(root, wrap=tk.WORD, width=40, height=15, yscrollcommand=scrollbar.set)
output_text.pack()

# Create a button to process the input
process_button = tk.Button(root, text="Send", command=process_input)
process_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()