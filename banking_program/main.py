def show_balance(balance):
    print("***************************")
    print(f"Your balance is ${balance:.2f}")
    print("***************************")


def deposit(balance):
    print("***************************")
    deposit_amount = float(input("Enter the amount you want to deposit: $"))
    print("***************************")
    if deposit_amount > 0:
        return (deposit_amount)
    else:
        print("Enter a valid deposit amount")
        return 0
    print("***************************")
    print("***************************")


def withdraw(balance):
    print("***************************")
    withdraw_amount = float(input("Enter the amount you want to withdraw: $"))
    print("***************************")
    if withdraw_amount > 0:
        return (withdraw_amount)
    elif withdraw_amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        print("Enter a valid withdrawal amount")
        return 0
    print("***************************")
    print("***************************")


def main():
    balance = 10000.65
    running = True
    while running:
        print("***************************")
        print("*****BANKING PROGRAM*******")
        print("***************************")
        print("1.Show balance\n2.Deposit\n3.Withdraw\n4.Quit")
        choice = int(input("Enter your choice (1 to 4): "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit(balance)
            print(f"Your balance is ${balance:.2f}")
        elif choice == 3:
            balance -= withdraw(balance)
            print(f"Your balance is {balance:.2f}")
        elif choice == 4:
            running = False
        else:
            print("Enter a valid option")
    print("Thank you! Have a nice day!")


if __name__ == '__main__':
    main()
