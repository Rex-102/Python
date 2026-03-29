import random
print("Python number guessing game!")
low = int(input("Enter the low part of the range: "))
high = int(input("Enter the high part of the range: "))
number = random.randint(low, high)
guesses = 0
while True:
    guess = input("Enter your guess(enter q to exit): ").lower()
    if guess == "q":
        break
    elif guess.isdigit():
        guess = int(guess)
        guesses += 1
        if int(guess) > high or int(guess) < low:
            print("Enter a valid option inside the range with no other alphabets than q")
            print(
                f"The range is {low} to {high}, please enter inside the range or q to quit")
        elif int(guess) == number:
            print(f"Your guess {number} was correct!")
            break
        elif int(guess) != number:
            print("Your guess was Incorrect")
            if guess > number:
                print("Too high!!")
            else:
                print("Too low!!")
    else:
        print("Invalid guess")
        print(f"The range is {low} to {high}, please enter inside the range")
