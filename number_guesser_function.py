print("Greetings player! I have a fun game for you to play.")
print("\nI'm thinking of a number between 1 and 100. Can you guess it correctly in as few guesses as possible?")
difficulty = input("\nWould you like to play easy (enter 'e'), medium ('m') or hard ('h)?")

from random import randint


def play_game_hard():
    active = True
    my_number = randint(1, 100)
    count = 0
    while active:
        if count < 4:   
            their_number = int(input("Okay, guess:"))
            if their_number == my_number:
                print(f"Congratulations, {their_number} was the correct number!")
                count += 1
                active = False
            elif their_number > my_number:
                    print(f"That number is high, try again")
                    count += 1
            elif their_number < my_number: 
                    print("Thats low, try again.")
                    count += 1
        else:
             print("Sorry you've exceeded your number of guesses!")
             active = False
    else:
        print(f" Number of guesses = {count}")
        replay = input("Would you like to play again?('yes' or 'no')")
        if replay == 'yes':
            new_difficulty = input("\nWould you like to play easy (enter 'e'), medium ('m') or hard ('h)?")
            if new_difficulty == 'e':
                 play_game_easy()
            elif new_difficulty == 'm':
                 play_game_medium()
            elif new_difficulty =='h':
                 play_game_hard()
        else:
            print("Thanks for playing!")    


def play_game_medium():
    active = True
    my_number = randint(1, 100)
    count = 0
    while active:
        if count < 8:   
            their_number = int(input("Okay, guess:"))
            if their_number == my_number:
                print(f"Congratulations, {their_number} was the correct number!")
                count += 1
                active = False
            elif their_number > my_number:
                    print(f"That number is high, try again")
                    count += 1
            elif their_number < my_number: 
                    print("Thats low, try again.")
                    count += 1
        else:
             print("Sorry you've exceeded your number of guesses!")
             active = False
    else:
        print(f" Number of guesses = {count}")
        replay = input("Would you like to play again?('yes' or 'no')")
        if replay == 'yes':
            new_difficulty = input("\nWould you like to play easy (enter 'e'), medium ('m') or hard ('h)?")
            if new_difficulty == 'e':
                 play_game_easy()
            elif new_difficulty == 'm':
                 play_game_medium()
            elif new_difficulty =='h':
                 play_game_hard()
        else:
            print("Thanks for playing!") 

def play_game_easy():
    active = True
    my_number = randint(1, 100)
    count = 0
    while active:
        if count < 15:   
            their_number = int(input("Okay, guess:"))
            if their_number == my_number:
                print(f"Congratulations, {their_number} was the correct number!")
                count += 1
                active = False
            elif their_number > my_number:
                    print(f"That number is high, try again")
                    count += 1
            elif their_number < my_number: 
                    print("Thats low, try again.")
                    count += 1
        else:
             print("Sorry you've exceeded your number of guesses!")
             active = False
    else:
        print(f" Number of guesses = {count}")
        replay = input("Would you like to play again?('yes' or 'no')")
        if replay == 'yes':
            new_difficulty = input("\nWould you like to play easy (enter 'e'), medium ('m') or hard ('h)?")
            if new_difficulty == 'e':
                 play_game_easy()
            elif new_difficulty == 'm':
                 play_game_medium()
            elif new_difficulty =='h':
                 play_game_hard()
        else:
            print("Thanks for playing!") 

difficulty = ''

while difficulty not in ('e', 'm', 'h'):
    difficulty = input("\nWould you like to play easy (enter 'e'), medium ('m') or hard ('h)?")
    if difficulty not in ('e', 'm', 'h'):
        print(f"Sorry, {difficulty} isn't one of the options, try again.")

if difficulty == 'e':
    play_game_easy()
elif difficulty == 'm':
    play_game_medium()
elif difficulty == 'h':
    play_game_hard()


