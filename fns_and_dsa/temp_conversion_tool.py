FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    print(f"{fahrenheit}°F is {Converted_to_c}°C")

def convert_to_fahrenheit(celsius):
    Converted_to_f = (celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {Converted_to_f}°F")


temperature = float(input("Enter the temperature to convert:"))
C_or_F = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if C_or_F == "C":
    convert_to_fahrenheit(temperature)
elif C_or_F == "F":
    convert_to_celsius(temperature)

else : 
    raise ValueError("Invalid temperature. Please enter a numeric value.")
