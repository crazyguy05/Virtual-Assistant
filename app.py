import streamlit as st
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
SYSTEM_PROMPT = "You are a helpful assistant."

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Chat Assistant")
st.caption("Local LLM powered chat assistant with command support")

# ==============================
# SESSION STATE
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# ==============================
# COMMAND HANDLERS
# ==============================
def handle_system_command(text):
    text = text.lower()

    if "time" in text:
        return f"The time is {datetime.datetime.now().strftime('%I:%M %p')}"

    if "date" in text:
        return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"

    if "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    return None


def handle_youtube_command(text):
    text = text.lower()

    if "play music" in text:
        webbrowser.open("https://music.youtube.com")
        return "Playing music on YouTube Music"

    if text.startswith("play "):
        song = text.replace("play", "").strip()
        query = song.replace(" ", "+")
        url = f"https://music.youtube.com/search?q={query}&autoplay=1"
        webbrowser.open(url)
        return f"Playing {song} on YouTube Music"

    return None


def get_ai_response(user_text):
    st.session_state.messages.append(
        {"role": "user", "content": user_text}
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    return reply

# ==============================
# CHAT UI STYLES
# ==============================
st.markdown(
    """
    <style>
    .chat-container {
        background-color: #f4f6f9;
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 12px;
    }
    .user-msg {
        background-color: #cfe2ff;
        color: #000000;
        padding: 10px;
        margin: 8px;
        border-radius: 12px;
        max-width: 75%;
        margin-left: auto;
        text-align: left;
        box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    }
    .ai-msg {
        background-color: #e2e3e5;
        color: #000000;
        padding: 10px;
        margin: 8px;
        border-radius: 12px;
        max-width: 75%;
        margin-right: auto;
        text-align: left;
        box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# CHAT DISPLAY
# ==============================
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='user-msg'><strong>You:</strong> {msg['content']}</div>",
            unsafe_allow_html=True
        )
    elif msg["role"] == "assistant":
        st.markdown(
            f"<div class='ai-msg'><strong>AI:</strong> {msg['content']}</div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# INPUT AREA
# ==============================
user_input = st.text_input(
    "Type your message",
    placeholder="Ask a question or say 'play music'",
    key="input"
)

col1, col2 = st.columns([1, 1])

with col1:
    send_clicked = st.button("Send")

with col2:
    clear_clicked = st.button("Clear Chat")

# ==============================
# ACTION HANDLING
# ==============================
if send_clicked and user_input.strip():

    yt_response = handle_youtube_command(user_input)
    if yt_response:
        st.session_state.messages.append(
            {"role": "assistant", "content": yt_response}
        )
        st.rerun()

    sys_response = handle_system_command(user_input)
    if sys_response:
        st.session_state.messages.append(
            {"role": "assistant", "content": sys_response}
        )
        st.rerun()

    get_ai_response(user_input)
    st.rerun()

if clear_clicked:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    st.rerun()
