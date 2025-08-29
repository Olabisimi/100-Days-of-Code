from random import randint

attempts_easy = 10
attempts_hard = 5
turns = 0

def compare_answer(user_guess, computer_number, turns):
    if user_guess > computer_number:
        print("Too high.")
        return turns - 1
    elif user_guess < computer_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it ! The answer was {computer_number}")

#Level of difficulty
def difficulty():
    level_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level_difficulty == "easy":
        return attempts_easy
    else:
        return attempts_hard
def guessing_number():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    #Computer is thinking of a random integer between 1 and 100.
    computer_number = randint(1, 100)
    print(f"Pssst, the correct answer is {computer_number}")

    turns = difficulty()

    user_guess = 0
    while user_guess != computer_number:
        print(f"You have {turns} attempts left to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns = compare_answer(user_guess, computer_number, turns)
        if turns == 0:
            print("You runt out of guesses, you lose.")
            return
        elif user_guess != computer_number:
            print("Guess Again.")
guessing_number()