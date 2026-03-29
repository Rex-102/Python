import random
board = ("rock", "paper", "scissors")
print("Rock, paper and scissors game!")
running = True
while running:
    computer = random.choice(board)
    user_choice = None
    while user_choice not in board:
        user_choice = input(
            "Enter your choice, rock, paper or scissors: ")
    print(f"Player:{user_choice} Computer:{computer}")
    if user_choice == computer:
        print("It's a tie!")
    elif user_choice == "rock" and computer == "paper":
        print("Computer wins")
    elif user_choice == "paper" and computer == "scissors":
        print("Computer wins")
    elif user_choice == "scissors" and computer == "paper":
        print("Computer wins")
    else:
        print("Player wins")
    if not input("Do you still want to play(y/n): ").lower() == "y":
        running = False
print("Thanks for playing!")
