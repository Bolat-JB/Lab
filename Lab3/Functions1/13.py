import random
guessing = random.randint(1, 20)

k = 0

print("Hello! What is your name?")
name = str(input())
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
num = 0

while num != guessing:
    num = int(input())
    if num < guessing:
        print("Your guess is to low.\nTake a guess.")
        k += 1
    if num > guessing:
        print("Your guess is to high.\nTake a guess.")
        k += 1

print(f"Good job, {name}! You guessed my number in {k} guesses!")