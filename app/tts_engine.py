import requests
import tempfile
import os
import base64
import winsound

from app.config import SARVAM_API_KEY


def speak_text(text, language="en-IN"):

    print("\n[TTS] Generating speech...")

    url = "https://api.sarvam.ai/text-to-speech"

    payload = {
        "inputs": [text],
        "target_language_code": language,
        "speaker": "anushka"
    }

    headers = {
        "api-subscription-key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }

    try:

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        if response.status_code != 200:

            print("[TTS] Error:")
            print(response.text)
            return

        # Parse JSON
        data = response.json()

        # Extract base64 audio
        audio_base64 = data.get("audios", [])[0]

        if not audio_base64:

            print("[TTS] No audio received.")
            return

        # Decode base64 audio
        audio_bytes = base64.b64decode(audio_base64)

        # Save WAV file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio_bytes)

            temp_audio_path = temp_audio.name

        print("\n🔊 Speaking...\n")

        # DIRECT AUDIO PLAYBACK
        winsound.PlaySound(
            temp_audio_path,
            winsound.SND_FILENAME
        )

        # Cleanup
        os.remove(temp_audio_path)

    except Exception as e:

        print("\n[TTS ERROR]")
        print(e)