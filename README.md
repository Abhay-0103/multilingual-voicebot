# Multilingual AI Marketing VoiceBot

A real-time multilingual AI voice assistant built using:

- Gemini 2.5 Flash
- Sarvam AI STT + TTS
- LiveKit Realtime Streaming
- Python
- Voice Activity Detection (VAD)

Supports:

- English
- Hindi
- Kannada

The assistant can:
- listen through microphone
- detect language automatically
- generate AI responses
- respond back with voice
- maintain conversation context
- support realtime LiveKit streaming

---

# Features

## AI Voice Conversation

- Voice input through microphone
- AI-generated responses
- Voice output playback

---

## Multilingual Support

Supports:
- English
- Hindi
- Kannada

Automatic language detection included.

---

## Real-Time AI Pipeline

Pipeline:

```text
Microphone
   ↓
Sarvam Speech-to-Text
   ↓
Language Detection
   ↓
Gemini 2.5 Flash
   ↓
Conversation Memory
   ↓
Sarvam Text-to-Speech
   ↓
Speaker Output
```

---

## LiveKit Realtime Streaming

Includes:
- LiveKit Agent
- Realtime audio rooms
- Streaming-ready architecture
- Voice Activity Detection (VAD)

---

## Production-Style Architecture

- Modular structure
- Logging support
- Error handling
- Retry handling
- Scope restriction
- Conversation memory

---

# Project Structure

```text
multilingual-voicebot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── voice_agent.py
│   ├── livekit_agent.py
│   ├── llm_processor.py
│   ├── language_detector.py
│   ├── stt_engine.py
│   ├── tts_engine.py
│   ├── livekit_manager.py
│   ├── conversation_manager.py
│   ├── logger.py
│   ├── scope_validator.py
│   └── config.py
│
├── logs/
│   └── conversations.log
│
├── venv/
│
├── .env
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Abhay-0103/multilingual-voicebot.git

cd multilingual-voicebot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Packages

```txt
google-genai
python-dotenv
langdetect
requests
sounddevice
numpy
scipy
livekit
livekit-agents
livekit-plugins-silero
```

---

# Environment Variables

Create:

# `.env`

```env
# Gemini
GEMINI_API_KEY=your_gemini_api_key

# Sarvam AI
SARVAM_API_KEY=your_sarvam_api_key

# LiveKit
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

---

# API Setup

## 1. Gemini API

Get API Key:

https://aistudio.google.com/app/apikey

---

## 2. Sarvam AI

Get API Key:

https://www.sarvam.ai/

Used for:
- Speech-to-Text
- Text-to-Speech

---

## 3. LiveKit

Create Free Account:

https://cloud.livekit.io

Used for:
- realtime streaming
- voice rooms
- audio transport

---

# Running the Project

## CLI Voice Assistant

Run:

```bash
python -m app.main
```

---

## LiveKit Streaming Agent

Run:

```bash
python -m app.livekit_agent dev
```

---

# Supported Voice Commands

## English

```text
Tell me about AI automation
```

---

## Hindi

```text
AI automation क्या है
```

---

## Kannada

```text
AI automation ಬಗ್ಗೆ ಹೇಳಿ
```

---

# Scope Restrictions

The assistant intentionally DOES NOT:
- discuss pricing
- negotiate deals
- provide legal advice
- discuss contracts

This simulates enterprise-safe AI assistants.

---

# Logging

All conversations are stored in:

```text
logs/conversations.log
```

Includes:
- timestamps
- language
- user input
- AI response

---

# Voice Features

## Current Features

- Voice Input
- Voice Output
- Language Detection
- Conversation Memory
- Real-Time STT/TTS

---

## Upcoming Improvements

- interruption handling
- streaming TTS
- lower latency
- silence detection
- frontend UI
- realtime streaming pipelines

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Gemini 2.5 Flash | AI Responses |
| Sarvam AI | STT + TTS |
| LiveKit | Realtime Streaming |
| Python | Backend |
| Silero VAD | Voice Activity Detection |

---

# Future Scope

- Web dashboard
- Analytics
- AI sales assistant
- CRM integrations
- WhatsApp integration
- Voice cloning
- Streaming LLM responses

---

# Final Result

This project demonstrates:

- Realtime AI Voice Interaction
- Multilingual Conversations
- AI Automation Workflows
- Production-Style Voice Architecture
- Live Streaming Infrastructure

---