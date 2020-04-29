import random
secret_number = random.randint(0,100)
print(secret_number)

name = input("Hi, what's your name?")

greeting = input("{}, I'm thinking of a number between 1 and 100.".format(name))

guess = input("Try to guess my number: ")

while True:
    count = 0
    if guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high, try again.")
            count = count + 1
        guess = input("Your guess? ")
        else:
            print("Your guess is too low, try again.")
            guess = input("Your guess? ")
            count = count + 1
    else:
        print(f"Excellent job {name}! You guess the number in {} tries!")"