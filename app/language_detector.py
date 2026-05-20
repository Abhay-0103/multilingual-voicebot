from langdetect import detect

def detect_language(text):

    try:

        lang = detect(text)

        if lang == "hi":
            return "Hindi"

        elif lang == "kn":
            return "Kannada"

        return "English"

    except:
        return "English"