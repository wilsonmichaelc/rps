import random

#print("Shall we play a game.")

#print("Let's play Rock, Paper, Scissors.")
#print("Rock breaks scissors, scissors cuts paper, paper covers rock.")

print("""
Shall we play a game.
Let's play Rock, Paper, Scissors.
Rock breaks scissors, scissors cuts paper, paper covers rock.
""")

# user_score = 0
# comp_score = 0

# for i in range(3):
#     user_input = input("Please indicate: rock, paper, or scissors... ")
#     comp_input = random.choice(["rock", "paper", "scissors"])
#     print("User Played:", user_input, "\t", "Computer Played:", comp_input)
#     if comp_input == "rock":
#         if user_input == "scissors":
#             comp_score += 1
#         if user_input == "paper":
#             user_score += 1
#     elif comp_input == "paper":
#         if user_input == "rock":
#             comp_score += 1
#         if user_input == "scissors":
#             user_score += 1
#     elif comp_input == "scissors":
#         if user_input == "paper":
#             comp_score += 1
#         if user_input == "rock":
#             user_score += 1
#     else:
#         if comp_input == user_input:
#             print("We chose the same. No score.")

#     print("User Score:", user_score, "\t", "Computer Score:", comp_score)

# if user_score > comp_score:
#     print("You Win!! :)")
# elif user_score < comp_score:
#     print("You Lose. :(")
# else:
#     print("We tied. Would you like to play again?")
