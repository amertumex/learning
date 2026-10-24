import random

random_number = random.randint(1, 100)
#print(random_number)

while True:
    user_number = int(input("Guess the number: "))
    if user_number < random_number:
        print("Try bigger Number")
    elif user_number > random_number:
        print("Try smaller Number")
    else:
        print("You guessed the number")
        break