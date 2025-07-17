import openai
import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import webbrowser
from new import apikey

# Initialize OpenAI
openai.api_key = apikey
model_id = "gpt-3.5-turbo"

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Use voices[0] for male, [1] for female

# Track conversation
conversation = [
    {
        "role": "system",
        "content": "You are Nova, an intelligent and respectful AI assistant.",
    }
]

# Speak out loud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to microphone input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query
        except Exception:
            print("Sorry, I couldn't understand.")
            return "error"

# Get response from ChatGPT
def chat_with_gpt(prompt):
    conversation.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    reply = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": reply})
    print(f"Nova: {reply}")
    speak(reply)

# Launch applications
def open_app(app_name):
    apps = {
        "discord": r"C:\Users\User\AppData\Local\Discord\app-1.0.9021\Discord.exe",
        "vscode": r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "whatsapp": r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2342.7.0_x64__cv1g1gvanyjgm\WhatsApp.exe",
        "telegram": r"C:\Users\User\AppData\Roaming\Telegram Desktop\Telegram.exe",
        "settings": r"C:\Windows\ImmersiveControlPanel\SystemSettings.exe",
        "calculator": r"C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2307.4.0_x64__8wekyb3d8bbwe\CalculatorApp.exe",
        "acrobat": r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    }
    if app_name in apps:
        speak(f"Opening {app_name}")
        subprocess.Popen(apps[app_name])
    else:
        speak("Application not found.")

# Main function
def main():
    speak("Hello, I am Nova. Ready to help.")
    print("Say 'Nova' followed by your command.")

    while True:
        query = take_command().lower()

        if "error" in query:
            continue

        elif "open website" in query:
            speak("Please say the website name")
            site = take_command()
            if site != "error":
                speak(f"Opening {site}")
                webbrowser.open(f"https://{site}.com")

        elif "open app" in query:
            speak("Which app would you like to open?")
            app = take_command().lower()
            open_app(app)

        elif "time" in query:
            time_str = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time_str}")

        elif "reset chat" in query:
            conversation[:] = conversation[:1]
            speak("Conversation history cleared.")

        elif "exit" in query or "quit" in query:
            speak("Goodbye.")
            break

        else:
            chat_with_gpt(query)

if __name__ == "__main__":
    main()
