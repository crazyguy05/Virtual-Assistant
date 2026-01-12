import time
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
import datetime
import webbrowser

# ==============================
# LLM CONFIGURATION (OLLAMA)
# ==============================
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL = "llama3.2:1b"

SYSTEM_PROMPT = "You are a helpful voice assistant."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# ==============================
# TEXT TO SPEECH
# ==============================
def speak_text(text: str):
    print("AI:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 190)   # faster speech
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ==============================
# SPEECH TO TEXT
# ==============================
def listen_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=4) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(
            source,
            timeout=None,
            phrase_time_limit=8
        )

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Recognition error:", e)
        return ""

# ==============================
# LLM HELPERS
# ==============================
def get_assistant_reply(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    return response.choices[0].message.content


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

# ==============================
# SYSTEM COMMANDS
# ==============================
def handle_command(text):
    text = text.lower()

    # ---- TIME ----
    if "time" in text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak_text(f"The time is {current_time}")
        return True

    # ---- DATE ----
    if "date" in text:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak_text(f"Today's date is {today}")
        return True

    # ---- OPEN YOUTUBE ----
    if "open youtube" in text:
        speak_text("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True

    return False

# ==============================
# YOUTUBE MUSIC COMMANDS
# ==============================
def handle_youtube_command(text):
    text = text.lower()

    # ---- PLAY GENERIC MUSIC ----
    if "play music" in text:
        speak_text("Playing music on YouTube Music")
        webbrowser.open("https://music.youtube.com")
        return True

    # ---- PLAY SPECIFIC SONG (AUTOPLAY) ----
    if text.startswith("play "):
        song_name = text.replace("play", "").strip()
        speak_text(f"Playing {song_name} on YouTube Music")

        query = song_name.replace(" ", "+")
        url = f"https://music.youtube.com/search?q={query}&autoplay=1"
        webbrowser.open(url)
        return True

    return False

# ==============================
# MAIN LOOP
# ==============================
def main():
    speak_text("Voice assistant started. You can talk to me.")

    while True:
        user_input = listen_from_microphone()

        if not user_input:
            continue

        clean_input = user_input.lower().strip()

        # ---- EXIT ----
        if "exit" in clean_input or "quit" in clean_input:
            speak_text("Goodbye!")
            break

        # ---- YOUTUBE COMMANDS FIRST ----
        if handle_youtube_command(clean_input):
            time.sleep(1.2)
            continue

        # ---- SYSTEM COMMANDS ----
        if handle_command(clean_input):
            time.sleep(1.2)
            continue

        # ---- AI CHAT ----
        add_user_message(messages, user_input)

        assistant_reply = get_assistant_reply(messages)

        add_assistant_message(messages, assistant_reply)

        speak_text(assistant_reply)

        time.sleep(1.5)

# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()
