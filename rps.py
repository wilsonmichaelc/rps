import random
import time
import sys

# Print text on character at a time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

delay_print("Shall we play a game?\n\n")

# input yes or no to play
user_play = input("Please answer: Y or N\n")


# For loop to see if user wants to play RPS
for instance in user_play:
    if user_play == "Y":
        print("""
Let's play Rock, Paper, Scissors.\n
Rock breaks scissors, scissors cuts paper, paper covers rock.\n
We will be playing best out of 3.\n
        """)
    else: 
        print("Goodbye")

user_keep_playing = True

# Keep while rolling
while user_keep_playing == True:
    user_score = 0
    comp_score = 0
    for i in range(3):
        user_input = input("Please indicate: rock, paper, or scissors... \n")
        comp_input = random.choice(["rock", "paper", "scissors"])
        print("User Played:", user_input, "\t", "Computer Played:", comp_input, "\n")
        if comp_input == "rock":
            if user_input == "scissors":
                comp_score += 1
            if user_input == "paper":
                user_score += 1
        elif comp_input == "paper":
            if user_input == "rock":
                comp_score += 1
            if user_input == "scissors":
                user_score += 1
        elif comp_input == "scissors":
            if user_input == "paper":
                comp_score += 1
            if user_input == "rock":
                user_score += 1
        else:
            if comp_input == user_input:
                print("We chose the same. No score.\n")

        print("User Score:", user_score, "\t", "Computer Score:", comp_score, "\n")

    if user_score > comp_score:
        print("""You Win! :) 
Would you like to play again?\n""")
        user_play_again = input("Please answer: Y or N\n\n")
        if user_play_again == "Y":
            user_keep_playing = True
        else:
            user_keep_playing = False
    elif user_score < comp_score:
        print("""You Lose! :( 
Would you like to play again?\n""")
        user_play_again = input("Please answer: Y or N\n\n")
        if user_play_again == "Y":
            user_keep_playing = True
        else:
            user_keep_playing = False
    else:
        print("""We tied. 
Would you like to play again?\n""")
        user_play_again = input("Please answer: Y or N\n\n")
        if user_play_again == "Y":
            user_keep_playing = True
        else:
            user_keep_playing = False
# while loop ends

print("\nDave. This conversation can serve no perpose anymore. Goodbye")
