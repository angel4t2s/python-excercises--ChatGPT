# Task 1: Simple Calculator
def simple_calculator():
    print("===== SIMPLE CALCULATOR =====")

    try:
        num_1 = float(input("Input the first number: "))
        num_2 = float(input("Great! Now input the second number: "))
        operator = input("Excellent! Now input the operator sign (+, -, *, %, /):")

        if operator == "+":
            print(f"Result: {num_1 + num_2}.")
        elif operator == "-":
            print(f"Result: {num_1 - num_2}.")
        elif operator == "*":
            print(f"Result: {num_1 * num_2}.")
        elif operator == "/":
            if num_2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Result: {num_1 / num_2}.")
        elif operator == "%":
            print(f"Result: {num_1 % num_2}.")
        else:
            print("Invalid operator!")

    except ValueError:
        print("Invalid input. Please enter numbers.")

# Task 2: Age in Months
def age_in_months():
    print(f"==== Age Calculator ====")
    print("What is your name?:")
    name = input().title()

    print(f"Hi {name}, How old are you?")
    age_in_years = int(input())

    age_in_months = age_in_years * 12

    print(f"{name}, you are {age_in_months} months old!")


# Task 3: Area of a circle
def area_circle_calculator():
    print("=== Area of A Circle ===")
    pi = 3.1416
    radius = float(input("input the radius of the circle:"))
    area = round(pi * radius ** 2, 2)
    print(f"The area of the circle is: {area}")


# Task 4: Temperature Converter
def temp_converter():
    print("=== Temperature Converter ===")
    temp_cel = float(input("What is the temperature in Celsius?"))
    temp_far = round((temp_cel * 1.8) + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp_far}")

# Task 5: Self Introduction Script
def introduction():
    print("===== SELF INTRODUCTION APP =====")

    print("What is your name?:")
    name_intro = input()

    print(f"Hi {name_intro}, How old are you?")
    age_intro = int(input())

    print(f"Cool. So, what's your favorite food?")
    fav_food_intro = input()

    print(f"Hi, I'm {name_intro}. I'm {age_intro} years old and I love {fav_food_intro}!")


# simple_calculator()
# age_in_months()
# area_circle_calculator()
# temp_converter()
# introduction()

##### EXTRA OPTIONAL PRACTICES!!!!
# One: Simple Interest Calculator
def simple_interest_calculator():
    principal = float(input("Input the principal amount (initial money): "))

    answer = input("is the annual interest rate in percentage? (Y/N): ")

    if answer.lower() in ["yes", "y"]:
        annual_interest_percent = float(input("Input the annual interest rate: "))
        annual_interest = annual_interest_percent / 100
    elif answer.lower() in ["no", "n"]:
        annual_interest_decimal = float(input("input the annual interest rate: "))
        annual_interest = annual_interest_decimal
    else:
        print("You need to answer with either 'y', 'n', 'yes', or 'no'!")

    print("""
    Enter the time for interest calculation:
    - Example: For 3 years, 2 months, 3 weeks, and 10 days, enter:
    Years: 3
    Months: 2
    Weeks: 2
    Days: 10
    """)
    years = int(input("Years: "))
    months = int(input("Months: "))
    weeks = int(input("Weeks: "))
    days = int(input("Days: "))

    time_taken = float((
        years +
        (months/12) +
        (weeks/52) +
        (days/365)
    ))

    print(f"The simple interest is: N{round(principal * annual_interest * time_taken, 2)}")


# simple_interest_calculator()


# Two: Simple Interest Calculator
def bmi_calculator():
    print("===== Body Mass Index (bmi) Calculator =====")
    w_answer = input("Is the weight in kilograms (kg) or pounds (lbs)? (kg, lbs): ")
    if w_answer.lower() in ["kg", "kilogram"]:
        weight = float(input("Input your weight in kg: "))
    elif w_answer.lower() in ["lbs", "pounds"]:
        weight_in_pounds = float(input("Enter your weight in lbs: "))
        weight = weight_in_pounds * 0.4536
    else:
        print("Please read the instruction well and try again!")
        exit()

    h_answer = input("Is the height in meter (m) or inches (in)? (m, in): ")
    if h_answer.lower() in ["m", "meter", "metre"]:
        height = float(input("Input the height in (m): "))
    elif h_answer.lower() in ["in", "inches", "inch"]:
        height_in_pounds = float(input("Enter the height in (in): "))
        height = height_in_pounds * 39.3700787
    else:
        print("Please read the instruction well and try again!")
        exit()

    bmi = float(
        round(weight / height ** 2, 2)
    )
    print(f"Your bmi is: {bmi}.")
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are healthy weighted.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")


# bmi_calculator()

# Three: Unit Converter
def length_converter(number, unit_from, unit_to):
    # units = ["cm", "km", "in", "ft", "m"]

    # Centimeter outward
    if unit_from == "cm":
        if unit_to == "km":
            result = number / 100000
            return result
        elif unit_to == "m":
            result = number / 100
            return result
        elif unit_to == "in":
            result = number / 2.54
            return result
        elif unit_to == "ft":
            result = number / 30.48
            return result
        elif unit_to == "cm":
            return number
        else:
            return "Nan"
    # Kilometer Outward
    elif unit_from == "km":
        if unit_to == "cm":
            result = number * 100000
            return result
        elif unit_to == "m":
            result = number * 1000
            return result
        elif unit_to == "in":
            result = number * 39370
            return result
        elif unit_to == "ft":
            result = number * 3280.84
            return result
        elif unit_to == "km":
            return number
        else:
            return "Nan"
    # Inches Outward
    elif unit_from == "in":
        if unit_to == "cm":
            result = number * 2.54
            return result
        elif unit_to == "m":
            result = number / 39.37
            return result
        elif unit_to == "km":
            result = number / 39370
            return result
        elif unit_to == "ft":
            result = number / 12
            return result
        elif unit_to == "in":
            return number
        else:
            return "Nan"
    # Foot Outward
    elif unit_from == "ft":
        if unit_to == "cm":
            result = number * 30.48
            return result
        elif unit_to == "m":
            result = number / 3.281
            return result
        elif unit_to == "km":
            result = number / 3281
            return result
        elif unit_to == "in":
            result = number * 12
            return result
        elif unit_to == "ft":
            return number
        else:
            return "Nan"
    # Meter outward
    elif unit_from == "m":
        if unit_to == "cm":
            result = number * 100
            return result
        elif unit_to == "ft":
            result = number * 3.281
            return result
        elif unit_to == "km":
            result = number / 1000
            return result
        elif unit_to == "in":
            result = number * 39.37
            return result
        elif unit_to == "m":
            return number
        else:
            return "Nan"
    else:
        return "Nan"
    return None
def weight_converter(number, unit_from, unit_to):
    # units = ["kg", "g", "mg", "lb", "oz"]
    # Kilogram outward
    if unit_from == "kg":
        if unit_to == "g":
            result = number * 1000
            return result
        elif unit_to == "mg":
            result = number * (10**6)
            return result
        elif unit_to == "lb":
            result = number * 2.205
            return result
        elif unit_to == "oz":
            result = number * 35.274
            return result
        elif unit_to == "kg":
            return number
        else:
            return "Nan"
    # Gram outward
    elif unit_from == "g":
        if unit_to == "kg":
            result = number / 1000
            return result
        elif unit_to == "mg":
            result = number * 1000
            return result
        elif unit_to == "lb":
            result = number / 453.6
            return result
        elif unit_to == "oz":
            result = number / 28.35
            return result
        elif unit_to == "g":
            return number
        else:
            return "Nan"
    # Milligram outward
    elif unit_from == "mg":
        if unit_to == "kg":
            result = number / (10**6)
            return result
        elif unit_to == "g":
            result = number / 1000
            return result
        elif unit_to == "lb":
            result = number / 453600
            return result
        elif unit_to == "oz":
            result = number / 28350
            return result
        elif unit_to == "mg":
            return number
        else:
            return "Nan"
    # Pounds outward
    elif unit_from == "lb":
        if unit_to == "kg":
            result = number / 2.205
            return result
        elif unit_to == "g":
            result = number * 453.6
            return result
        elif unit_to == "mg":
            result = number * 453600
            return result
        elif unit_to == "oz":
            result = number * 16
            return result
        elif unit_to == "lb":
            return number
        else:
            return "Nan"
    # Pounds outward
    elif unit_from == "oz":
        if unit_to == "kg":
            result = number / 35.274
            return result
        elif unit_to == "g":
            result = number * 28.35
            return result
        elif unit_to == "mg":
            result = number * 28350
            return result
        elif unit_to == "lb":
            result = number / 16
            return result
        elif unit_to == "oz":
            return number
        else:
            return "Nan"
    return None
def volume_converter(number, unit_from, unit_to):
    # units = ["L", "mL", "gal", "fl oz"]
    if unit_from == "l":
        if unit_to == "ml":
            result = number * 1000
            return result
        elif unit_to == "gal":
            result = number / 4.546
            return result
        elif unit_to == "fl oz":
            result = number * 35.195
            return result
        elif unit_to == "l":
            return number
        else:
            return "Nan"
    elif unit_from == "ml":
        if unit_to == "l":
            result = number / 1000
            return result
        elif unit_to == "gal":
            result = number / 4546
            return result
        elif unit_to == "fl oz":
            result = number * 28.413
            return result
        elif unit_to == "ml":
            return number
        else:
            return "Nan"
    elif unit_from == "gal":
        if unit_to == "l":
            result = number * 4.546
            return result
        elif unit_to == "fl oz":
            result = number * 160
            return result
        elif unit_to == "ml":
            result = number * 4546
            return result
        elif unit_to == "gal":
            return number
        else:
            return "Nan"
    elif unit_from == "fl oz":
        if unit_to == "l":
            result = number / 35.195
            return result
        elif unit_to == "ml":
            result = number * 28.413
            return result
        elif unit_to == "gal":
            result = number / 160
        elif unit_to == "fl oz":
            return number
        else:
            return "Nan"
    return None
def temperature_converter(number, unit_from, unit_to):
    # units = ["C", "F", "K"]
    if unit_from == "c":
        if unit_to == "f":
            result = (number * (9/5)) + 32
            return result
        elif unit_to == "k":
            result = number + 273.15
            return result
        elif unit_to == "c":
            return number
        else:
            return "Nan"
    elif unit_from == "f":
        if unit_to == "c":
            result = (number - (32)) * 5/9
            return result
        elif unit_to == "k":
            result = (number - 32) * 5/9 + 273.15
            return result
        elif unit_to == "f":
            return number
        else:
            return "Nan"
    elif unit_from == "k":
        if unit_to == "c":
            result = number - 273.15
            return result
        elif unit_to == "f":
            result = (number - 273.15) * 9/5 + 32
            return result
        elif unit_to == "k":
            return number
        else:
            return "Nan"
    return None

def unit_converter():
    print("|===== UNIT CONVERTER =====|")
    print("""What is the category of the unit?
1. Length
2. Mass/Weight
3. Volume
4. Temperature """)
    try:
        category = int(input("input 1, 2, 3, or 4: "))
        if category == 1:
            print("What unit are you converting from?")
            unit_from = str(input("input cm, km, in, ft, or m: "))

            print("What unit are you converting to?")
            unit_to = str(input("input cm, km, in, ft, or m: "))

            unit = float(input("Input the unit to be converted: "))

            result = round(length_converter(unit, unit_from.lower(), unit_to.lower()), 3)

            print(f"Result: {result}")
        elif category == 2:
            print("What unit are you converting from?")
            unit_from = str(input("input kg, g, mg, lb, or oz: "))

            print("What unit are you converting to?")
            unit_to = str(input("input kg, g, mg, lb, or oz: "))

            unit = float(input("Input the unit to be converted: "))

            result = round(weight_converter(unit, unit_from.lower(), unit_to.lower()), 3)

            print(f"Result: {result}")
        elif category == 3:
            print("What unit are you converting from?")
            unit_from = str(input("input L, mL, gal, or fl oz: "))

            print("What unit are you converting to?")
            unit_to = str(input("input L, mL, gal, or fl oz: "))

            unit = float(input("Input the unit to be converted: "))

            result = round(volume_converter(unit, unit_from.lower(), unit_to.lower()), 3)

            print(f"Result: {result}")
        elif category == 4:
            print("What unit are you converting from?")
            unit_from = str(input("input C, F, or K: "))

            print("What unit are you converting to?")
            unit_to = str(input("input C, F, or K: "))

            unit = float(input("Input the unit to be converted: "))

            result = round(temperature_converter(unit, unit_from.lower(), unit_to.lower()), 3)

            print(f"Result: {result}")
        else:
            print("You need to put 1, 2, 3, or 4.")
    except ValueError:
        print("You need to put a number!")

unit_converter()



