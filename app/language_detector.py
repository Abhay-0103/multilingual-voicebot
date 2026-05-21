import re
from langdetect import detect


def detect_language(text):

    # Detect Hindi (Devanagari)
    if re.search(r'[\u0900-\u097F]', text):

        return "Hindi"

    # Detect Kannada
    elif re.search(r'[\u0C80-\u0CFF]', text):

        return "Kannada"

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