import random
secret_number = random.randint(0,100)
#print(secret_number)

name = input("Hi, what's your name?")
name = name.title()


print(f"{name}, I'm thinking of a number between 1 and 100.")

guess = int(input("Try to guess my number: "))


count = 0
   
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high, try again.")
        count = count + 1
        guess = int(input("Your guess? "))
    if guess < secret_number:
        print("Your guess is too low, try again.")
        guess = int(input("Your guess? "))
        count = count + 1
    else:
        count = count + 1
        print(f"Excellent job {name}! You guessed the number in {count} tries!")
        break