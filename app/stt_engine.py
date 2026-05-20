import requests
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os

from app.config import SARVAM_API_KEY

SAMPLE_RATE = 16000
DURATION = 5


def record_audio():

    print("\n🎤 Listening...\n")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    # Create temp file path
    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_path = temp_file.name

    # CLOSE file immediately
    temp_file.close()

    # Write recording
    write(
        temp_path,
        SAMPLE_RATE,
        recording
    )

    return temp_path


def transcribe_audio(audio_path):

    url = "https://api.sarvam.ai/speech-to-text"

    headers = {
        "api-subscription-key": SARVAM_API_KEY
    }

    try:

        with open(audio_path, "rb") as audio_file:

            files = {
                "file": (
                    "audio.wav",
                    audio_file,
                    "audio/wav"
                )
            }

            response = requests.post(
                url,
                headers=headers,
                files=files
            )

        # Remove temp file
        os.remove(audio_path)

        if response.status_code != 200:

            print("\n[STT ERROR]")
            print(response.text)

            return None

        result = response.json()

        transcript = result.get("transcript", "")

        return transcript

    except Exception as e:

        print("\n[STT ERROR]")
        print(e)

        return None