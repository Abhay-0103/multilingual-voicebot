import asyncio

from livekit.agents import (
    AgentSession,
    Agent,
    RoomInputOptions,
    WorkerOptions,
    cli
)

from livekit.plugins import silero

from app.language_detector import detect_language
from app.llm_processor import generate_response

from app.tts_engine import speak_text

class MarketingAssistant(Agent):

    def __init__(self):

        super().__init__(
            instructions="""
            You are a multilingual AI marketing voice assistant.

            Supported languages:
            - English
            - Hindi
            - Kannada

            Your role:
            - discuss AI automation
            - explain industry trends
            - help users understand AI technology

            Keep responses:
            - concise
            - natural
            - professional
            """
        )

    async def on_message(self, message):

        user_text = message.text

        print(f"\nUser: {user_text}")

        language = detect_language(user_text)

        response = generate_response(
            user_text,
            language
        )

        print(f"\nBot: {response}")

        return response


async def entrypoint(ctx):

    await ctx.connect()

    print("Connected to LiveKit room.")

    speak_text(
    "Hello! I am your multilingual AI marketing assistant.")

    session = AgentSession(
        vad=silero.VAD.load()
    )

    await session.start(
        room=ctx.room,
        agent=MarketingAssistant(),
        room_input_options=RoomInputOptions()
    )


if __name__ == "__main__":

    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint
        )
    )