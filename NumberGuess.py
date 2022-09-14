#Generate a random number, track how many tries it takes the user to guess it

#Install the default module for random generation
import random

#Establish an upper limit for the game utilizing user input. Number cannot be 0 or lower. Accounting for
#user to type in a non-interger.
limit=input("Type a number: ")

if limit.isdigit():
    limit = int(limit)
    if limit<=0:
        print("Please type in a number greater than 0 next time.")
        quit()
else:
    print("Please type in a number next time.")
    quit()

random_number = random.randint(0, limit)

#Begin the game utilizing a loop and prompt until the user guesses the number.
guess_count=0
while True:
    guess_count += 1
    user_guess=input("Guess what number I thought of? ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess==random_number:
            break
        if user_guess>random_number:
            print("Your guess was greater than the number.")

        if 0<=user_guess<random_number:
            print("Your guess was lower than the number.")

        if user_guess<0:
            print("Please input a positive integer.")

    else:
        print("Please type an integer.")

#Finish game and tell score

print("Congratulations, you guessed the correct number!")
print("It took you ", guess_count, " tries to guess the number.")