# =========== TASK ONE: STUDENT GRADES AVERAGER =============

# ===> Creating a function to calculate the students grade average
def grade_averager():
    num_students = 0
    try:
        num_students = int(input("How many students are there?: "))
    except ValueError:
        print("You need to put numbers!")

    for i in range(num_students):
        stud_name = input("Enter student name: ")
        try:
            test1 = float(input("Enter Test 1 score: "))
        except ValueError:
            print("You need to put numbers!")
        try:
            test2 = float(input("Enter Test 2 score: "))
        except ValueError:
            print("You need to put numbers!")
        try:
            test3 = float(input("Enter Test 3 score: "))
        except ValueError:
            print("You need to put numbers!")

        test_average = round((test1 + test2 + test3) / 3, 2)

        if test_average >= 50:
            pass_mark = "Passed!"
        else:
            pass_mark = "Failed."

        print(f"{stud_name}'s average score is {test_average} - {pass_mark}")

# Another method - Using list
def grade_averager_list():
    num_students = 0
    try:
        num_students = int(input("How many students are there?: "))
    except ValueError:
        print("You need to put numbers!")

    for i in range(num_students):
        stud_scores = []
        stud_name = input("Enter student name: ")
        try:
            stud_scores.append(float(input("Enter Test 1 score: ")))
        except ValueError:
            print("You need to put numbers!")
        try:
            stud_scores.append(float(input("Enter Test 2 score: ")))
        except ValueError:
            print("You need to put numbers!")
        try:
            stud_scores.append(float(input("Enter Test 3 score: ")))
        except ValueError:
            print("You need to put numbers!")

        avg_scores = round(sum(stud_scores)/3, 2)

        if avg_scores < 50:
            pass_rate = "Failed."
        else:
            pass_rate = "Passed!"

        print(f"{stud_name} average score is {avg_scores} - {pass_rate}")

# Another method - using dictionary
def grade_averager_dict():
    num_students = 0
    try:
        num_students = int(input("Enter number of student: "))
    except ValueError:
        print("You need to put numbers!")

    for i in range(num_students):
        student_details = {
            "name" : input("Enter student name: "),
            "Test_scores" : {}
        }
        try:
            student_details["Test_scores"]["Test 1"] = float(input("Enter Test 1 score: "))
        except ValueError:
            print("You need to put numbers!")
        try:
            student_details["Test_scores"]["Test 2"] = float(input("Enter Test 2 score: "))
        except ValueError:
            print("You need to put numbers!")
        try:
            student_details["Test_scores"]["Test 3"] = float(input("Enter Test 3 score: "))
        except ValueError:
            print("You need to put numbers!")

        average_score = round(sum(student_details["Test_scores"].values())/3, 2)

        if average_score >= 50:
            pass_mark = "Passed!"
        else:
            pass_mark = "Failed."

        print(student_details["name"], "'s average score is ", average_score, " - ", pass_mark)

# <=========== TASK TWO: PASSWORD STRENGTH CHECKER =============>
def password_strength_checker():

    # COMPUTING THE ANALYSIS AND DISPLAYING THE RESULT


    while True:
        strength_score = 0
        password = input("Enter password to analyze: ")
        # LENGTH
        if len(password) >= 8:
            strength_score += 25
        else:
            strength_score += 0

        # UPPERCASE CHARACTERS
        upper_count = 0
        for char in password:
            if char.isupper():
                upper_count += 1
        if upper_count >= 1:
            strength_score += 12.5
        else:
            strength_score += 0

        # LOWERCASE CHARACTERS
        lower_count = 0
        for char in password:
            if char.islower():
                lower_count += 1
        if lower_count >= 1:
            strength_score += 12.5
        else:
            strength_score += 0

        # NUMERIC CHARACTERS
        num_count = 0
        for num in password:
            if num.isnumeric():
                num_count += 1
        if num_count >= 1:
            strength_score += 25
        else:
            strength_score += 0

        # SPECIAL CHARACTERS
        special_char = 0
        for char in password:
            if not char.isalnum():
                special_char += 1
        if special_char >= 1:
            strength_score += 25
        else:
            strength_score += 0

        # Computing and Displaying Result
        print(f"Password Strength: {round(strength_score, 2)}%")
        if strength_score == 100:
            print(f"Remark: Strong Password!")
            break
        else:
            print("Remark: Weak Password. Try again.")
            strength_score = 0


# <=========== TASK THREE: MULTIPLICATION TABLE GENERATOR =============>
def multi_table(num):
    for i in range(1,13):
        print(f"{num} x {i} = {num * i}")


# <=========== TASK FOUR: NUMBER GUESSING GAME =============>
import random #Imported it here  instead of at the top for clarity and to show that it is workings of the tasks... if you get what I mean, lol.
def num_guessing_game():
    number = random.randint(1,20)
    tries_left = 5

    while tries_left >= 1:
        try:
            guess = int(input("Guess the number: "))

            if guess < number:
                print("Too low!")
                tries_left -= 1
            elif guess > number:
                print("Too High")
                tries_left -= 1
            else:
                print("Correct!")
                break
        except ValueError:
            print("You need to put number.")

        if tries_left == 0:
            print(f"You have used up your tries. The correct number is {number}")


# <=========== TASK FIVE: COUNTER TIMER =============>
import time
def countdown_timer():
    timer = int(input("Enter a number of seconds: "))
    while timer >= 0:
        print(f"{timer} second{'s' if timer!=1 else ''} left.")
        time.sleep(1)
        timer -=1


# <=========== BONUS CHALLENGE =============>


def bank_atm_simulator():
    transact_again = True
    balance = 71245.64
    pin_trial = 3
    while transact_again == True and pin_trial != 0:
        try:
            user_pin = input("Input pin: ")
        except ValueError:
            print("You need to put numbers.")
        if user_pin != "1234":
            print("Pin incorrect. Try again.")
            pin_trial -=1
        else:
            print("====== Select to proceed ======")
            print("""
    a. Check balance          b. Deposit
    
    c. Withdraw               d. Exit""")
            try:
                menu = input("Select 'a,b,c, or d' to proceed: ")
            except ValueError:
                print("You need to put numbers.")
            if menu.lower() == "a":
                print(f"Balance: {balance: .2f}")
            elif menu.lower() == "b":
                try:
                    deposit_amount = float(input("Enter amount to deposit: "))
                except ValueError:
                    print("You need to put numbers.")
                balance += deposit_amount
                print(f"{deposit_amount} deposited to account. Balance: {balance: .2f}")
            elif menu.lower() == "c":
                try:
                    withdraw_amount = float(input("Enter amount to withdraw: "))
                except ValueError:
                    print("You need to put numbers.")
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} withdrawn from the account. Balance: {balance: .2f}")
                else:
                    print("Insufficient balance")
            elif menu.lower() == "d":
                print("Thanks for banking with us.")
                break
            else:
                print("You need to select either 'a,b,c or d' to proceed.")
        if pin_trial == 0:
            print("Maximum attempts reached. Card blocked. Contact your bank.")
            break
        else:
            try:
                answer = input("Would you like to make another transaction? (yes/no): ")
            except ValueError:
                print("You need to put yes/no.")
            if answer.lower() == "yes":
                transact_again = True
            elif answer.lower() == "no":
                print("Thanks for banking with us.")
                transact_again = False
            else:
                print("You need to put yes or no.")

bank_atm_simulator()
