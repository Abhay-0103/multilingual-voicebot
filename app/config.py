from dotenv import load_dotenv
import os

load_dotenv()

LIVEKIT_URL = os.getenv("LIVEKIT_URL")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")