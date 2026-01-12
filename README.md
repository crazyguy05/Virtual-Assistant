# AI Voice & Chat Assistant (Local LLM)

## Overview
This project is an AI-powered assistant that supports **two interaction modes**:
1. A **voice-based CLI assistant** using microphone input and text-to-speech output.
2. A **web-based chat assistant** built using Streamlit.

Both modes are powered by a **locally hosted Large Language Model (LLM)** using Ollama, allowing the system to run entirely on the local machine without relying on paid cloud APIs.

The assistant can understand natural language commands, respond intelligently, and perform real-world actions such as playing music on YouTube, opening websites, and providing system information like time and date.

---

## Key Features
- Voice-based assistant using Speech-to-Text and Text-to-Speech
- Chat-based assistant with a clean Streamlit UI
- Local LLM inference using Ollama
- Intelligent command routing (commands vs AI conversation)
- YouTube Music autoplay for spoken or typed music requests
- System commands such as time, date, and browser control
- Fully local execution (no paid APIs required)

---

## Interaction Modes

### 1. Voice Assistant (CLI)
- Uses the system microphone for input
- Responds using text-to-speech
- Runs as a continuous voice-driven loop in the terminal

Run using:
```bash
python voice_assistant.py
```

---

### 2. Chat Assistant (Streamlit UI)
- Web-based chat interface
- Supports the same commands as the voice assistant
- Useful for demos, testing, and showcasing the project

Run using:
```bash
streamlit run app.py
```

---

## How It Works
1. User input (voice or text) is captured.
2. Input is passed through a command router:
   - If it matches a known command (e.g., play music, open YouTube, get time), the action is executed directly.
   - Otherwise, the input is sent to the local LLM for an AI-generated response.
3. The assistant responds via speech (voice mode) or chat bubbles (Streamlit mode).

This architecture separates **deterministic system commands** from **AI-driven conversation**, similar to real-world assistants.

---

## Tech Stack
- Python
- Ollama (Local LLM runtime)
- OpenAI-compatible API interface (used with Ollama)
- SpeechRecognition (Speech-to-Text)
- pyttsx3 (Text-to-Speech)
- Streamlit (Web UI)
- Webbrowser module (Music and website control)

---

## Requirements
- Python 3.10+
- Ollama installed and running locally
- A supported Ollama model (example below)

---

## Setup Instructions

### 1. Install Ollama
Download and install Ollama from:
https://ollama.com

Pull a supported model:
```bash
ollama pull llama3.2:1b
```

---

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Run the Voice Assistant
```bash
python voice_assistant.py
```

---

### 5. Run the Chat UI
```bash
streamlit run app.py
```

---

## Example Commands
- "Play music"
- "Play Believer by Imagine Dragons"
- "Open YouTube"
- "What time is it?"
- "What is today's date?"
- "Tell me a joke"
- "Exit"

---

## Project Structure
```
.
├── voice_assistant.py   # Voice-based CLI assistant
├── app.py               # Streamlit chat UI
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Notes
- Music playback is handled via YouTube Music in the browser due to third-party API restrictions.
- Spotify integration is intentionally designed as a future extension.
- The project focuses on backend logic and assistant behavior rather than frontend-heavy design.

---

## Future Improvements
- Browser-based voice input for the Streamlit UI
- Spotify API integration when available
- Improved intent classification
- Command history and logging
- Model selection for different Ollama models

---

## Author
Built as a hands-on AI engineering project to understand voice systems, local LLM integration, and real-world assistant architecture.
