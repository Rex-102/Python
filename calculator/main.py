num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Menu: \n" "1. Enter + for addition\n" "2. Enter - for substraction\n" "3. Enter * for multiplication\n" "4. Enter / for division\n")
choice = input("Enter your choice: ")
if choice == "+":
    add = num1 + num2
    print(f"The addition of {num1} and {num2} is {add}")
elif choice == "-":
    sub = num1 - num2
    print(f"The substraction of {num1} and {num2} is {sub}")
elif choice == "*":
    mul = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {mul}")
elif choice == "/":
    div = num1 / num2
    print(f"The division of {num1} and {num2} is {div}")
else:
    print("Enter a valid choice")
