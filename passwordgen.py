import string
import random

#ask user for length of passwords
lpasswords = input('how long should the passwords be?')
#ask user for how many passwords to generate
npasswords = input('how many passwrords should be generated?')

#retrives all possible characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#aggregate all into the same pool
all = lower + upper + num + symbols

#loop that generates based on the user's request
while npasswords > 0:
    new = random.sample(all,lpasswords)
    npasswords = npasswords -1
    password = "".join(new)
    print password
