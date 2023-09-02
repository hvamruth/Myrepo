import tkinter as tk
from tkinter import scrolledtext
import openai
import speech_recognition as sr
import pyttsx3

# Replace 'YOUR_API_KEY' with your actual GPT-3.5 API key
openai.api_key = 'YOUR_API_KEY'

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use the appropriate engine for GPT-3.5
            prompt=prompt,
            max_tokens=150,  # Adjust as needed
            stop=None,
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm sorry, there was an error in generating the response."

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio).lower()
        print(f"User: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def on_voice_input():
    user_input = get_voice_input()
    if user_input:
        response = generate_response(user_input)
        text_box.insert(tk.END, f"\nYou: {user_input}\n")
        text_box.insert(tk.END, f"Jarvis: {response}\n")
        speak(response)

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("ChatGPT with Voice Recognition")

text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
text_box.pack(padx=10, pady=10)

voice_input_button = tk.Button(root, text="Voice Input", command=on_voice_input)
voice_input_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=5)

root.mainloop()
