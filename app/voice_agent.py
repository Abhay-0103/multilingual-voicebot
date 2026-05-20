from app.language_detector import detect_language
from app.llm_processor import generate_response
from app.tts_engine import speak_text
from app.livekit_manager import get_language_code
from app.conversation_manager import update_language

from app.stt_engine import (
    record_audio,
    transcribe_audio
)

import time


def start_voicebot():

    print("\n=== AI Marketing VoiceBot ===")
    print("Languages: English | Hindi | Kannada")
    print("Say 'exit' to quit\n")

    while True:

        try:

            input("\nPress ENTER to speak...")

            # Record microphone
            audio_path = record_audio()

            # Convert speech to text
            user_input = transcribe_audio(audio_path)

            if not user_input:

                print("No speech detected.\n")
                continue

            print(f"\nYou: {user_input}")

            # Exit condition
            if "exit" in user_input.lower():

                print("\nGoodbye!\n")
                break

            # Detect language
            language = detect_language(user_input)

            update_language(language)

            print(f"\nDetected Language: {language}")

            # Generate AI response
            response = generate_response(
                user_input,
                language
            )

            print(f"\nBot: {response}\n")

            # Convert language code
            language_code = get_language_code(language)

            # Speak response
            speak_text(
                response,
                language_code
            )

            time.sleep(1)

        except KeyboardInterrupt:

            print("\n\nVoicebot stopped.\n")
            break

        except Exception as e:

            print("\n[VOICEBOT ERROR]")
            print(e)