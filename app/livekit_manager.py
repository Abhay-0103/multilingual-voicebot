def get_language_code(language):

    mapping = {
        "English": "en-IN",
        "Hindi": "hi-IN",
        "Kannada": "kn-IN"
    }

    return mapping.get(
        language,
        "en-IN"
    )