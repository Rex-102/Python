foods = []
price = []
total = 0
while True:
    food = input("Enter your desired food(enter q to exit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        prices = float(input("Enter the price of your item : $"))
        price.append(prices)
print("-----YOUR LIST-----")
for food in foods:
    print(food)
for prices in price:
    total += prices
print()
print(f"Your total would be ${total:.2f}")
