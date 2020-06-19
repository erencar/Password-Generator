# Python 3.7 Version

import string
import random

def passgen(length):

        chars=string.ascii_letters + string.digits + string.punctuation

        result= "".join(random.choice(chars) for _ in range(length))
        return result

while True:
        try:
                length=int(input('How many characters in your password? = '))
                break
        except ValueError:
                print("Input wasn't an integer. Try again...")

print(passgen(length))
