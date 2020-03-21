# Python 3.7 Version

import string
import random

def passgen(length):

        chars=string.ascii_letters + string.digits + string.punctuation

        result= "".join(random.choice(chars) for _ in range(length))
        return result


length=int(input('How many characters in your password? = '))
print(passgen(length))
