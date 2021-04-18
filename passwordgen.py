import string
import random


lpasswords = input('how long should the passwords be?')
npasswords = input('how many passwrords should be generated?')




lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


all = lower + upper + num + symbols




while npasswords > 0:
    new = random.sample(all,lpasswords)
    npasswords = npasswords -1
    password = "".join(new)
    print password