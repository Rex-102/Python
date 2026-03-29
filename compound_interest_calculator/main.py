p = 0
r = 0
t = 0
while True:
    p = float(input("Enter the initial principal: "))
    if p < 0:
        print("Principal can't be less than zero")
        p = float(input("Enter the initial principal: "))
    else:
        break

while True:
    r = float(input("Enter the interest rate: "))
    if r < 0:
        print("Interest rate can't be less than zero")
        r = float(input("Enter the rate of increment: "))
    else:
        break
while True:
    t = int(input("Enter the time in years: "))
    if t < 0:
        print("Time can't be less than zero")
        t = int(input("Enter the time: "))
    else:
        break

total = p * pow(1 + (r/100), t)
print(f"The total money after {t} year/s is ${total:.2f}")
