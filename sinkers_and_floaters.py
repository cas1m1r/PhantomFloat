# codex42.py
# Sacred Floating Point Codex – Base42 Message Encoder/Decoder

CHARSET = (
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    " .?!#$\n,"
)
BASE = len(CHARSET)         # 42
EXPONENT = 42               # 2^42 normalization space
MAX_CHARS_PER_FLOAT = 7     # Because 42^7 < 2^42 safely fits

def encode_chunk(text, max_chars=MAX_CHARS_PER_FLOAT):
    """Encode a chunk of text (up to max_chars) into a float in [0, 1)."""
    assert all(c in CHARSET for c in text), f"Invalid character(s) in: {text}"
    text = text[:max_chars].ljust(max_chars, CHARSET[0])  # pad with 'a'
    value = 0
    for c in text:
        value = value * BASE + CHARSET.index(c)
    return value / (2 ** EXPONENT)


def decode_chunk(f, max_chars=MAX_CHARS_PER_FLOAT):
    """Decode a float in [0, 1) into a chunk of max_chars."""
    value = int(f * (2 ** EXPONENT))
    chars = []
    for _ in range(max_chars):
        value, rem = divmod(value, BASE)
        chars.append(CHARSET[rem])
    return ''.join(reversed(chars))


def encode_string(message):
    """Encode a full message into a list of floats."""
    message = message.lower()
    chunks = [message[i:i + MAX_CHARS_PER_FLOAT] for i in range(0, len(message), MAX_CHARS_PER_FLOAT)]
    return [encode_chunk(chunk) for chunk in chunks]  # round for display


def decode_floats(float_list):
    """Decode list of floats back to a string."""
    return ''.join(decode_chunk(f) for f in float_list).rstrip(CHARSET[0])
