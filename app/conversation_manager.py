conversation_context = {
    "language": "English",
    "history": []
}

def update_language(language):
    conversation_context["language"] = language

def add_message(role, content):

    conversation_context["history"].append({
        "role": role,
        "content": content
    })

def get_history():
    return conversation_context["history"]

def get_language():
    return conversation_context["language"]