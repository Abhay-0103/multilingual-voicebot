# import requests
# import sounddevice as sd
# from scipy.io.wavfile import write
# import tempfile
# import os

# from app.config import DEEPGRAM_API_KEY

# SAMPLE_RATE = 16000
# DURATION = 5


# def record_audio():

#     print("\n🎤 Listening...\n")

#     recording = sd.rec(
#         int(DURATION * SAMPLE_RATE),
#         samplerate=SAMPLE_RATE,
#         channels=1,
#         dtype="int16"
#     )

#     sd.wait()

#     temp_file = tempfile.NamedTemporaryFile(
#         suffix=".wav",
#         delete=False
#     )

#     temp_path = temp_file.name

#     temp_file.close()

#     write(
#         temp_path,
#         SAMPLE_RATE,
#         recording
#     )

#     return temp_path


# def transcribe_audio(audio_path):

#     url = "https://api.deepgram.com/v1/listen?model=nova-3&language=multi"

#     headers = {
#         "Authorization": f"Token {DEEPGRAM_API_KEY}",
#         "Content-Type": "audio/wav"
#     }

#     try:

#         with open(audio_path, "rb") as audio_file:

#             response = requests.post(
#                 url,
#                 headers=headers,
#                 data=audio_file
#             )

#         os.remove(audio_path)

#         if response.status_code != 200:

#             print("\n[STT ERROR]")
#             print(response.text)

#             return None

#         result = response.json()

#         transcript = (
#             result["results"]["channels"][0]
#             ["alternatives"][0]
#             ["transcript"]
#         )

#         return transcript

#     except Exception as e:

#         print("\n[STT ERROR]")
#         print(e)

#         return None




# Using headphone auto detected 

# import requests
# import sounddevice as sd
# from scipy.io.wavfile import write
# import tempfile
# import os

# from app.config import DEEPGRAM_API_KEY

# SAMPLE_RATE = 16000
# DURATION = 5


# def record_audio():

#     # print("\n================================")
#     # print(" Available Audio Devices ")
#     # print("================================\n")

#     # print(sd.query_devices())

#     print("\n🎤 Listening...\n")

#     try:

#         # Automatically use default microphone
#         default_input_device = sd.default.device[0]

#         recording = sd.rec(
#             int(DURATION * SAMPLE_RATE),
#             samplerate=SAMPLE_RATE,
#             channels=1,
#             dtype="int16",
#             device=default_input_device
#         )

#         sd.wait()

#         # Create temp file
#         temp_file = tempfile.NamedTemporaryFile(
#             suffix=".wav",
#             delete=False
#         )

#         temp_path = temp_file.name

#         temp_file.close()

#         # Save recording
#         write(
#             temp_path,
#             SAMPLE_RATE,
#             recording
#         )

#         return temp_path

#     except Exception as e:

#         print("\n[RECORDING ERROR]")
#         print(e)

#         return None


# def transcribe_audio(audio_path):

#     if not audio_path:
#         return None

#     url = (
#         "https://api.deepgram.com/v1/listen"
#         "?model=nova-3"
#         "&language=multi"
#         "&smart_format=true"
#         "&punctuate=true"
#     )

#     headers = {
#         "Authorization": f"Token {DEEPGRAM_API_KEY}",
#         "Content-Type": "audio/wav"
#     }

#     try:

#         with open(audio_path, "rb") as audio_file:

#             response = requests.post(
#                 url,
#                 headers=headers,
#                 data=audio_file
#             )

#         # Delete temp file
#         os.remove(audio_path)

#         if response.status_code != 200:

#             print("\n[STT ERROR]")
#             print(response.text)

#             return None

#         result = response.json()

#         transcript = (
#             result["results"]["channels"][0]
#             ["alternatives"][0]
#             ["transcript"]
#         )

#         if not transcript:

#             print("\n⚠ No speech detected.")

#             return None

#         return transcript

#     except Exception as e:

#         print("\n[STT ERROR]")
#         print(e)

#         return None


# Both deepgram and sarvam 

import requests
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os
import numpy as np
import time

from app.config import (
    DEEPGRAM_API_KEY,
    SARVAM_API_KEY
)

from app.language_detector import detect_language

SAMPLE_RATE = 16000

# Voice Activity Detection Settings
SILENCE_THRESHOLD = 500
SILENCE_DURATION = 1.5


# ---------------- RECORD AUDIO ---------------- #

def record_audio():

    print("\n🎤 Listening...\n")

    try:

        # Auto-detect headphone mic / default mic
        default_input_device = sd.default.device[0]

        recording = []

        silence_start = None

        def audio_callback(
            indata,
            frames,
            time_info,
            status
        ):

            nonlocal silence_start

            volume_norm = (
                np.linalg.norm(indata) * 10
            )

            recording.append(indata.copy())

            # Detect silence
            if volume_norm < SILENCE_THRESHOLD:

                if silence_start is None:
                    silence_start = time.time()

            else:

                silence_start = None

        # Start microphone stream
        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
            device=default_input_device,
            callback=audio_callback
        ):

            while True:

                time.sleep(0.1)

                if silence_start:

                    silence_time = (
                        time.time() - silence_start
                    )

                    # Stop after silence
                    if silence_time > SILENCE_DURATION:
                        break

        # Combine audio chunks
        audio_data = np.concatenate(
            recording,
            axis=0
        )

        # Create temp audio file
        temp_file = tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        )

        temp_path = temp_file.name

        temp_file.close()

        # Save WAV file
        write(
            temp_path,
            SAMPLE_RATE,
            audio_data
        )

        return temp_path

    except Exception as e:

        print("\n[RECORDING ERROR]")
        print(e)

        return None


# ---------------- DEEPGRAM STT ---------------- #

def deepgram_transcribe(audio_path):

    url = (
        "https://api.deepgram.com/v1/listen"
        "?model=nova-3"
        "&language=en"
        "&smart_format=true"
        "&punctuate=true"
    )

    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "audio/wav"
    }

    try:

        with open(audio_path, "rb") as audio_file:

            response = requests.post(
                url,
                headers=headers,
                data=audio_file,
                timeout=30
            )

        if response.status_code != 200:

            print("\n[DEEPGRAM STT ERROR]")
            print(response.text)

            return None

        result = response.json()

        transcript = (
            result["results"]["channels"][0]
            ["alternatives"][0]
            ["transcript"]
        )

        return transcript

    except Exception as e:

        print("\n[DEEPGRAM STT ERROR]")
        print(e)

        return None


# ---------------- SARVAM STT ---------------- #

def sarvam_transcribe(audio_path):

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
                files=files,
                timeout=30
            )

        if response.status_code != 200:

            print("\n[SARVAM STT ERROR]")
            print(response.text)

            return None

        result = response.json()

        transcript = result.get(
            "transcript",
            ""
        )

        return transcript

    except Exception as e:

        print("\n[SARVAM STT ERROR]")
        print(e)

        return None


# ---------------- MAIN ROUTER ---------------- #

def transcribe_audio(audio_path):

    if not audio_path:
        return None

    try:

        # Try Deepgram first
        transcript = deepgram_transcribe(
            audio_path
        )

        if transcript:

            language = detect_language(
                transcript
            )

            # English → Use Deepgram
            if language == "en-IN":

                os.remove(audio_path)

                return transcript

        # Hindi/Kannada → Use Sarvam
        transcript = sarvam_transcribe(
            audio_path
        )

        # Remove temp file
        os.remove(audio_path)

        if not transcript:

            print("\n⚠ No speech detected.")

            return None

        return transcript

    except Exception as e:

        print("\n[STT ERROR]")
        print(e)

        return None