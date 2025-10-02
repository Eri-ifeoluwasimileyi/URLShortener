import random
import string

def generate_short_url(length=8) -> str:

    words = string.ascii_letters + string.digits

    short_url = ''

    for w in range(length):
        random_word = random.choice(words)
        short_url += random_word

    return short_url

