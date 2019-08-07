# This code is about a small gaming app
import random

while True:
    print("")
    print("THIS IS A GUESS GAME----GUESS RIGHT TO WIN-----FOLLOW THE INSTRUCTION CLOSELY")
    print("")
    user_name = input("Please enter your UserName: ").upper()
    print("")
    while len(user_name) >= 4:
        fn = int(input("Choose your first number in the guess range: "))
        print("")
        ln = int(input("Choose your last number in the guess range: "))
        while abs(fn - ln) >= 5:
            guess = abs(random.randint(fn, ln))
            attempt = 1
            print("")
            print(f"Welcome {user_name} to the Game of Guess.....You have 5 attempts only!! ")
            while attempt < 5:
                guess_entry = abs(int(input(f"Guess a NUMBER between {fn} and {ln}: ")))
                if guess_entry == guess:
                    print(f"CONGRATULATIONS {user_name} You Win....Genius...Awesome!!!")
                    print("")
                    print(f"You Guessed {guess_entry} and the System_Guess was {guess}")
                    print("")
                    print(f"High Score for {attempt} attempt(s) is: {(6 - attempt) * 1000} points")
                    break
                else:
                    print("Try Again \n")
                    if attempt == 4:
                        print(f"You Failed :)_!!!\nPlay Again {user_name}")
                attempt += 1
                print("")
        else:
            print("Kindly set your guess range to minimum of 5 difference")
            print("")
    else:
        print("Kindly Specify a username of 4 characters minimum")
        print("")
