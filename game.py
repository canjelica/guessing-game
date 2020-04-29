name = input("Hi, what's your name?")
name = name.title()

import random
secret_number = random.randint(1,100)

print("{}, I'm thinking of a number between 1 and 100.".format(name))

guess = int(input("Try to guess my number: "))


