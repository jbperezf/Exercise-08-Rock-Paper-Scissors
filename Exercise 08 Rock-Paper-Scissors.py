# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of
# congratulations to the winner, and ask if the players want to start a new game)

print("\nWelcome, to Rock, Paper, Scissors.\n")
player_1 = str(input("Player 1, please enter your name: "))
player_2 = str(input("\n" + "Player 2, please enter your name: "))
first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                       "Enter 'r', 'p' or 's': " % player_1))
second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                        "Enter 'r', 'p' or 's': " % player_2))
p1_score = 0
p2_score = 0

while True:
    if first_play == "r" and second_play == "s":
        print(player_1 + " Wins.")
        p1_score += 1
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    elif first_play == "r" and second_play == "p":
        print(player_2 + " Wins.")
        p2_score += 1
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    elif first_play == "p" and second_play == "r":
        print(player_1 + " Wins.")
        p1_score += 1
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    elif first_play == "p" and second_play == "s":
        print(player_2 + " Wins.")
        p2_score += 1
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    elif first_play == "s" and second_play == "p":
        print(player_1 + " Wins.")
        p1_score += 1
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    elif first_play == "s" and second_play == "r":
        print(player_2 + " Wins.")
        p2_score += 1
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    elif first_play == second_play:
        print("It's a draw.")
        print(player_1 + ": " + str(p1_score) + "\n" + player_2 + ": "+ str(p2_score))
        if str(input("Want a rematch? 'yes'/'no': ")) == "yes":
            first_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                   "Enter 'r', 'p' or 's': " % player_1))
            second_play = str(input("\n%s, What's your pick?\nr = Rock\np = Paper\ns = Scissors\n\n"
                                    "Enter 'r', 'p' or 's': " % player_2))
            continue
        else:
            print("Thanks for playing.")
            break
    else:
        print("invalid input")
        break
