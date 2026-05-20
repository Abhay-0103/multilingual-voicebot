from google import genai
import time

from app.config import GEMINI_API_KEY
from app.scope_validator import validate_scope
from app.conversation_manager import add_message

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are a professional multilingual AI Marketing Voice Assistant.

Supported languages:
- English
- Hindi
- Kannada

Your role:
- educate users about AI automation
- explain industry trends
- discuss use cases
- help users understand AI voice technology
- maintain natural conversations

STRICTLY FORBIDDEN:
- pricing discussions
- discounts
- contracts
- negotiations
- legal advice
- confidential information

Conversation Style:
- concise
- natural
- human-like
- professional Indian conversational tone
- avoid robotic responses
- avoid overly long answers

IMPORTANT:
- preserve conversation context
- smoothly handle language switching
- respond in the same language as the user
"""

conversation_history = []


def generate_response(user_text, language):

    if not validate_scope(user_text):

        return """
I apologize, but pricing and commercial discussions
are handled by our sales specialists.
Would you like me to connect you with the sales team?
"""

    add_message("user", user_text)

    conversation_history.append(
        f"User: {user_text}"
    )

    # Keep only recent messages
    conversation_history[:] = conversation_history[-6:]

    prompt = f"""
{SYSTEM_PROMPT}

Respond ONLY in {language}.

Conversation:
{conversation_history}

User:
{user_text}
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            bot_response = response.text
            bot_response = bot_response[:400]

            conversation_history.append(
                f"Assistant: {bot_response}"
            )

            add_message("assistant", bot_response)

            return bot_response

        except Exception as e:

            print("\n⚠ AI service busy... retrying...")

            time.sleep(5)

    return """
I'm currently experiencing high traffic.
Please try again in a few moments.
"""