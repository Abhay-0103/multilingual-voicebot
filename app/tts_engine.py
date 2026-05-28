# import requests
# import tempfile
# import os

# from playsound import playsound

# from app.config import DEEPGRAM_API_KEY


# def speak_text(text, language="en-IN"):

#     print("\n[TTS] Generating speech...")

#     voice_map = {

#         "en-IN": "aura-2-orion-en",
#         "hi-IN": "aura-2-orion-en",
#         "kn-IN": "aura-2-orion-en"
#     }

#     model = voice_map.get(
#         language,
#         "aura-2-orion-en"
#     )

#     url = f"https://api.deepgram.com/v1/speak?model={model}"

#     headers = {
#         "Authorization": f"Token {DEEPGRAM_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "text": text
#     }

#     try:

#         response = requests.post(
#             url,
#             headers=headers,
#             json=payload
#         )

#         if response.status_code != 200:

#             print("\n[TTS ERROR]")
#             print(response.text)

#             return

#         with tempfile.NamedTemporaryFile(
#             delete=False,
#             suffix=".mp3"
#         ) as temp_audio:

#             temp_audio.write(response.content)

#             temp_audio_path = temp_audio.name

#         print("\nSpeaking...\n")

#         playsound(temp_audio_path)

#         os.remove(temp_audio_path)

#     except Exception as e:

#         print("\n[TTS ERROR]")
#         print(e)




# using Headphone Mic for better quality

# import requests
# import tempfile
# import os
# import sounddevice as sd
# import soundfile as sf

# from app.config import DEEPGRAM_API_KEY


# def speak_text(text, language="en-IN"):

#     print("\n[TTS] Generating speech...")

#     voice_map = {

#         "en-IN": "aura-2-orion-en",
#         "hi-IN": "aura-2-orion-en",
#         "kn-IN": "aura-2-orion-en"
#     }

#     model = voice_map.get(
#         language,
#         "aura-2-orion-en"
#     )

#     url = f"https://api.deepgram.com/v1/speak?model={model}"

#     headers = {
#         "Authorization": f"Token {DEEPGRAM_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "text": text
#     }

#     try:

#         response = requests.post(
#             url,
#             headers=headers,
#             json=payload
#         )

#         if response.status_code != 200:

#             print("\n[TTS ERROR]")
#             print(response.text)

#             return

#         with tempfile.NamedTemporaryFile(
#             delete=False,
#             suffix=".mp3"
#         ) as temp_audio:

#             temp_audio.write(response.content)

#             temp_audio_path = temp_audio.name

#         print("\nSpeaking...\n")

#         # Load audio
#         data, fs = sf.read(temp_audio_path)

#         # Play on current output device
#         sd.play(data, fs)

#         sd.wait()

#         os.remove(temp_audio_path)

#     except Exception as e:

#         print("\n[TTS ERROR]")
#         print(e)




# Both deepgram and saravam

import requests
import tempfile
import os
import base64
import winsound

import sounddevice as sd
import soundfile as sf

from app.config import (
    DEEPGRAM_API_KEY,
    SARVAM_API_KEY
)


def play_audio(file_path):

    try:

        data, fs = sf.read(file_path)

        # Auto-detect headphones / speakers
        default_output_device = sd.default.device[1]

        sd.play(
            data,
            fs,
            device=default_output_device
        )

        sd.wait()

    except Exception as e:

        print("\n[AUDIO PLAYBACK ERROR]")
        print(e)


# ---------------- DEEPGRAM TTS ---------------- #

def deepgram_tts(text):

    url = (
        "https://api.deepgram.com/v1/speak"
        "?model=aura-asteria-en"
    )

    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": text
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            stream=True,
            timeout=30
        )

        if response.status_code != 200:

            print("\n[DEEPGRAM TTS ERROR]")
            print(response.text)

            return

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as temp_audio:

            for chunk in response.iter_content(chunk_size=1024):

                if chunk:
                    temp_audio.write(chunk)

            temp_audio_path = temp_audio.name

        print("\nSpeaking...\n")

        play_audio(temp_audio_path)

        os.remove(temp_audio_path)

    except Exception as e:

        print("\n[DEEPGRAM TTS ERROR]")
        print(e)


# ---------------- SARVAM TTS ---------------- #

def sarvam_tts(text, language):

    speakers = {

        "hi-IN": "shreya",
        "kn-IN": "pooja"
    }

    speaker = speakers.get(
        language,
        "shreya"
    )

    url = "https://api.sarvam.ai/text-to-speech"

    payload = {
        "inputs": [text],
        "target_language_code": language,
        "speaker": speaker,
        "model": "bulbul:v3"
    }

    headers = {
        "api-subscription-key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }

    try:

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            stream=True,
            timeout=30
        )

        if response.status_code != 200:

            print("\n[SARVAM TTS ERROR]")
            print(response.text)

            return

        data = response.json()

        audios = data.get("audios", [])

        if not audios:

            print("\n⚠ No audio received.")
            return

        audio_base64 = audios[0]

        audio_bytes = base64.b64decode(audio_base64)

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio_bytes)

            temp_audio_path = temp_audio.name

        print("\nSpeaking...\n")

        play_audio(temp_audio_path)

        os.remove(temp_audio_path)

    except Exception as e:

        print("\n[SARVAM TTS ERROR]")
        print(e)


# ---------------- MAIN ROUTER ---------------- #

def speak_text(text, language="en-IN"):

    print("\n[TTS] Generating speech...\n")

    # English → Deepgram
    if language == "en-IN":

        deepgram_tts(text)

    # Hindi/Kannada → Sarvam
    else:

        sarvam_tts(
            text,
            language
        )