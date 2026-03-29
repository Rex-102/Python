menu = {"pizza": 3.00,
        "nachos": 4.50,
        "burger": 10.00,
        "fries": 5.99,
        "chips": 3.50,
        "coke": 2.00}
cart = []
total = 0
print("------------MENU---------------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("-------------------------------")
while True:
    food = input("Enter your choice of foods(enter q to quit ): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
print("-----------YOUR ORDER----------")
for food in cart:
    print(food, end=" ")
print()
print(f"Your total is ${total}")
