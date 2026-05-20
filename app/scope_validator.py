BLOCKED_TOPICS = [
    "price",
    "pricing",
    "discount",
    "payment",
    "contract",
    "legal",
    "invoice"
]

def validate_scope(text):

    text = text.lower()

    for topic in BLOCKED_TOPICS:

        if topic in text:

            return False

    return True