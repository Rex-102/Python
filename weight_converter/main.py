weight = float(input("Enter your weight: "))
unit = input("Enter K for kilograms and P for pounds: ")
if unit == "K":
    weight = weight * 2.205
    print(f"Your weight in pounds is {round({weight})}lbs")
elif unit == "P":
    weight = weight / 2.205
    print(f"Your weight in kilograms is {round({weight})}kgs")
else:
    print("Enter a valid option")
