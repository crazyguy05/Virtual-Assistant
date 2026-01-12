# AI Voice Assistant (Local LLM – Ollama)

## Overview
This project is a voice-controlled AI assistant built using Python that can understand spoken commands, respond intelligently using a locally hosted Large Language Model (Ollama), and execute real-world actions such as playing music on YouTube, reporting the current time/date, and answering general questions.

The assistant is designed as a **voice-first, command-driven system** and runs entirely on the local machine without relying on paid cloud-based AI services.

---

## Key Features
- Voice input using microphone (Speech-to-Text)
- AI-powered responses using a local LLM (Ollama)
- Text-to-Speech responses
- Intelligent command routing
- YouTube Music autoplay for spoken music requests
- System commands such as time, date, and browser actions
- Runs fully locally (no paid APIs required)

---

## How It Works
1. The assistant listens for user speech via the microphone.
2. Spoken input is converted to text.
3. The input is routed through a command handler:
   - If it is a known command (e.g., play music, open YouTube, get time), the corresponding action is executed.
   - Otherwise, the input is sent to a local LLM via Ollama for an AI-generated response.
4. The assistant responds using Text-to-Speech.

This design separates **deterministic commands** from **AI-driven conversation**, similar to how real-world voice assistants are architected.

---

## Tech Stack
- Python
- Ollama (Local LLM inference)
- OpenAI-compatible API interface (for Ollama)
- SpeechRecognition (Speech-to-Text)
- pyttsx3 (Text-to-Speech)
- Webbrowser module (YouTube playback control)

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
