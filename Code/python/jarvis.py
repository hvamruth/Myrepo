import openai
import speech_recognition as sr
import pyttsx3
import dotenv

# Replace 'YOUR_API_KEY' with your actual GPT-3.5 API key
openai.api_key = 'OPENAI_KEY'

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

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    print("Hello, I am Jarvis. How can I assist you?")
    while True:
        user_input = get_voice_input()
        if "exit" in user_input:
            print("Goodbye!")
            break
        if user_input:
            response = generate_response(user_input)
            print(f"Jarvis: {response}")
            speak(response)

if __name__ == "__main__":
    main()
