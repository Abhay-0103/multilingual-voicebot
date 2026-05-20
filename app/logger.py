from datetime import datetime


def log_conversation(user_text, bot_text, language):

    with open(
        "logs/conversations.log",
        "a",
        encoding="utf-8"
    ) as log_file:

        log_file.write(
            f"""
[{datetime.now()}]

Language: {language}

User:
{user_text}

Bot:
{bot_text}

-----------------------------------
"""
        )