import random
import time


def spin_row():
    symbols = ['🍒', '🍉', '🍌', '🍋', '⭐']
    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print("**************************")
    for rows in row:
        print(rows, end=" | ")
        time.sleep(1)
    print()
    print("**************************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet*2
        elif row[0] == '🍉':
            return bet*3
        elif row[0] == '🍌':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        else:
            return bet*10
    return 0


def main():
    balance = 100
    print("**************************")
    print("   Python slot machine    ")
    print("Symbols: 🍒 🍉 🍌 🍋 ⭐")
    print("**************************")

    while balance > 0:
        print(f"Your balance is ${balance}")
        bet = input("Place your bet: $")
        if not bet.isdigit():
            print("Enter a valid bet: $")
            continue
        bet = int(bet)
        if bet > balance:
            print(
                f"You have insufficient funds to bet ${bet}, your current balance is ${balance}")
            continue
        if bet <= 0:
            print("Enter a bet greater than zero")
            continue
        balance -= bet

        row = spin_row()
        time.sleep(1)
        print("Spinning....\n")
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You have won ${payout}")
        else:
            print("You have lost the round!")

        balance += payout
        print(f"Your current balance is ${balance}")
        play_again = input("Do you want to spin again (Y to spin): ").upper()
        if play_again != 'Y':
            break
    print("********************************************")
    print(f"Game Over! Your final balance is ${balance}")
    print("********************************************")


if __name__ == '__main__':
    main()
