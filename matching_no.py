import random

number = random.randint(1, 20)

while True:
    guess = int(input("Enter your number: "))

    if guess>number:
        print("Too High")
    elif guess<number:
        print("Too Low")
    else:
        print("Correct!")
        break