import random
import string

def generate_short_url(length=8) -> str:

    words = string.ascii_letters + string.digits

    #start with an empty string
    short_url = ''

    for w in range(length):
        #pick one random character from words
        random_word = random.choice(words)
        short_url += random_word

    return short_url

