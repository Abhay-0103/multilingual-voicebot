conversation_context = {
    "language": "English",
    "history": []
}


def update_language(language):

    conversation_context["language"] = language


def get_language():

    return conversation_context["language"]


def add_message(role, content):

    conversation_context["history"].append({
        "role": role,
        "content": content
    })

    # Keep only recent messages
    conversation_context["history"] = (
        conversation_context["history"][-10:]
    )


def get_history():

    return conversation_context["history"]