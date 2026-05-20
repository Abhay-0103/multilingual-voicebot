from langdetect import detect


def detect_language(text):

    try:

        detected = detect(text)

        # Hindi
        if detected == "hi":

            return "Hindi"

        # Kannada
        elif detected == "kn":

            return "Kannada"

        # Default English
        else:

            return "English"

    except Exception:

        return "English"