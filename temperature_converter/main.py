temperature = float(input("Enter the temperature: "))
unit = input(
    "Enter the current unit C for celcius, F for fahrenheit and K for kelvin: ")
if unit == "C":
    fahrenheit = (temperature * (9/5)) + 32
    print(f"The temperature in fahrenheit is {round({fahrenheit}, 1)}°F")
    kelvin = temperature + 273.15
    print(f"The temperature in kelvin is {round({kelvin}, 1)}°K")
elif unit == "K":
    celsius = temperature - 273.15
    print(f"The temperature in celcius is {round({celsius}, 1)}°C")
    fahrenheit = (celsius * (9/5)) + 32
    print(f"The temperature in fahrenheit is {round({fahrenheit}, 1)}°F")
elif unit == "F":
    celsius = (temperature - 32) * (5/9)
    print(f"The temperature in celsius is {round({celsius}, 1)}°C")
    kelvin = celsius + 273.15
    print(f"The temperature in kelvin is {round({kelvin}, 1)}°K")
else:
    print("Enter a valid unit")
