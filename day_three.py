# TASK ONE: BIRTHDAY REMINDER APP
def birthday_reminder():
    birthdays = {
        "Angelus": "March 11",
        "Johnson": "January 4",
        "Daniel": "February 28",
        "Chisom": "March 14",
        "Zara": "April 19",
        "Nathaniel": "May 2",
        "Aisha": "June 21",
        "Michael": "July 6",
        "Peter": "August 12",
        "Benson": "September 25",
        "Oladele": "October 10",
        "Sophia": "November 8",
        "David": "December 1",
        "Chioma": "January 22",
        "Jason": "February 17",
        "Fatima": "March 9",
        "Samuel": "April 3",
        "Blessing": "May 15",
        "Victor": "June 30",
        "Adaora": "July 27",
        "Olamide": "August 4",
        "Stella": "September 13",
        "Benjamin": "October 28",
        "Eniola": "November 19",
        "Gloria": "December 24",
        "Martins": "January 7",
        "Lilian": "February 5",
        "Ibrahim": "March 29",
        "Rita": "April 14",
        "Kelvin": "May 26",
        "Ngozi": "June 11"
    }

    name = input("Whose birthday do you want to look up? ").title()

    if name in birthdays.keys():
        print(f"{name}'s birthday is on {birthdays[name]}.")
    else:
        answer = input(f"I don't have {name}'s birthday. Add it? (y/n): ")
        if answer == "y":
            birthdays[name] = input(f"What is {name}'s birthday? ")
            print("Birthday added.")
            print(f"{name}'s birthday is {birthdays[name]}.")
        else:
            print("Got it.")

#TASK TWO: SHOPPING LIST APP
def shopping_app():
    shopping_list = set()
    print("Enter an item and hit 'Enter' to add to your shopping list. (type done to finish)")
    while True:
        item = input("- ")
        if item.lower() == 'done':
            print("Great! Here is your shopping list:")
            for i in sorted(shopping_list, key=str.lower):
                print(i)

            answer = input("Do you want to remove anything? (y/n): ")
            if answer.lower() == 'y':
                answer2 = input("By name or index? (N/I): ")
                if answer2.lower() == "n":
                    try:
                        # shopping_list.remove(f"{input("Type item name: ")}")
                        item_name = input("Type item name: ")
                        shopping_list.remove(item_name)
                        print("Item removed. New list is: ")
                        for i in sorted(shopping_list, key=str.lower):
                            print(i)
                        break
                    except KeyError:
                        print("Item not found.")
                        break

                elif answer2.lower() == "i":
                    try:
                        index_no = int(input("Input the index number: "))
                    except TypeError:
                        print("You need to put a number.")
                        break
                    temp_list = list(shopping_list)
                    del temp_list[index_no]
                    shopping_list = set(sorted(temp_list))
                    print("Deleted. New list is: ")
                    for i in sorted(shopping_list, key=str.lower):
                        print(i)
                    break
                else:
                    print("You need to answer either with N for name or I for index number.")
                    break
            elif answer.lower() == 'n':
                print("Got it")
                break
            else:
                print("You need to answer with either y for yes or n for no.")
                break
        else:
            if item not in shopping_list:
                shopping_list.add(item)
            else:
                print(f"{item} already in list.")

#TASK THREE: STUDENT GRADE DATABASE
def student_grade_average():
    student_database = {
        "Mark Tombson":(70, 40, 60, 84),
        "Amelia Johnson": (95, 98, 92, 88),
        "Benjamin Smith": (88, 91, 94, 97),
        "Charlotte Williams": (100, 85, 95, 93),
        "Daniel Brown": (92, 77, 89, 94),
        "Katherine Thomas": (90, 92, 88, 94),
        "Liam Jackson": (40, 79, 91, 55),
        "Madeline White": (100, 99, 87, 96),
        "Nathan Harris": (94, 95, 77, 92),
        "Olivia Martin": (89, 91, 90, 88),
        "Peter Thompson": (70, 68, 72, 65),
        "Quinn Garcia": (60, 62, 58, 75),
        "Victoria Lewis": (66, 70, 71, 52),
        "William Lee": (50, 55, 78, 60),
        "Xavier Walker": (77, 73, 75, 54),
        "Yasmin Hall": (62, 64, 68, 71),
        "Zachary Allen": (54, 79, 57, 52),
        "Alice Young": (78, 74, 59, 72),
        "Brian King": (65, 67, 63, 58),
        "Georgia Gonzalez": (76, 74, 61, 70),
        "Harper Nelson": (68, 50, 70, 72),
        "Ian Carter": (71, 75, 73, 69),
        "Nora Phillips": (27, 25, 22, 30),
        "Oscar Campbell": (34, 37, 19, 31),
        "Paige Parker": (49, 45, 47, 20),
        "Ryan Evans": (20, 18, 25, 60),
        "Sophia Edwards": (38, 35, 51, 37),
        "Thomas Collins": (26, 28, 24, 29),
    }
    print("Names of students in 200L")
    for names in student_database.keys():
        print(names)
    print("Pick a student to see his/her result:")
    try:
        student_picked = input("").strip().lower()
        if student_picked in [k.lower() for k in student_database.keys()]:
            student_average_score = sum(student_database[student_picked])/4
            print(f"Average score for {student_picked} is {student_average_score}")
        else:
            print("Not found. Check your spelling.")
    except KeyError:
        print(f"{student_picked} not in list. Check again.")
    try:
        if student_average_score >= 50:
            print("Status: Passed!")
        else:
            print("Status: Failed.")
    except UnboundLocalError:
        return None

#more complex
def student_grade_average_nested():
    students = {
        "Emily Davis": {
            "Math": 98,
            "English": 99,
            "Science": 84,
            "History": 96
        },
        "Frederick Miller": {
            "Math": 91,
            "English": 94,
            "Science": 95,
            "History": 72
        },
        "Grace Wilson": {
            "Math": 87,
            "English": 89,
            "Science": 93,
            "History": 90
        },
        "Henry Moore": {
            "Math": 96,
            "English": 100,
            "Science": 94,
            "History": 81
        },
        "Isabella Taylor": {
            "Math": 93,
            "English": 91,
            "Science": 92,
            "History": 95
        },
        "Tiffany Clark": {
            "Math": 72,
            "English": 74,
            "Science": 50,
            "History": 68
        },
        "Yasmin Hall": {
            "Math": 62,
            "English": 64,
            "Science": 68,
            "History": 71
        },
        "Zachary Allen": {
            "Math": 54,
            "English": 79,
            "Science": 57,
            "History": 52
        },
        "Alice Young": {
            "Math": 78,
            "English": 74,
            "Science": 59,
            "History": 72
        },
        "Brian King": {
            "Math": 65,
            "English": 67,
            "Science": 63,
            "History": 58
        },
        "Paige Parker": {
            "Math": 49,
            "English": 45,
            "Science": 47,
            "History": 20
        },
        "Ryan Evans": {
            "Math": 20,
            "English": 18,
            "Science": 25,
            "History": 60
        },
        "Sophia Edwards": {
            "Math": 38,
            "English": 35,
            "Science": 51,
            "History": 37
        },
        "Thomas Collins": {
            "Math": 26,
            "English": 28,
            "Science": 24,
            "History": 29
        },
    }
    print("Name of students in SS3")
    for names in students.keys():
        print(names)
    print("Select a student to view grades")
    student = input("")
    try:
        result = sum(students[student.title()].values())/4
        print(f"Student Name: {student.title()}")
        print("Result:")
        for subject, scores in students[student.title()].items():
            print(f"{subject}: {scores}")
        print(f"Average Score: {result}")
        if result < 50:
            print("Remark: Failed.")
        else:
            print("Remark: Passed!")
    except KeyError:
        print(f"{student} not found. Check your spelling.")

#TASK FOUR: WORD FREQUENCY COUNTER
def word_frequency_counter():
    import string
    word_count = {}
    sentence = input("Write a sentence to count: ")
    sentence_lower = sentence.lower()

    for word in sentence_lower.split():
        word = word.strip(string.punctuation)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word}:{count}")

#TASK FIVE: QUIZ GAME
def quiz_game():
    #useful imports
    import random
    from string import ascii_uppercase

    #dictionaries of questions
    question_1 = {
        "question": "Which planet is best known as the 'Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer": "Mars"
    }
    question_2 = {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Jane Austen"],
        "answer": "William Shakespeare"
    }
    question_3 = {
        "question": "What is the capital city of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    }
    question_4 = {
        "question": "In computing, what does 'CPU' stand for?",
        "options": ["Central Processing Unit", "Computer Processing Utility", "Control Power Unit",
                    "Central Program Utility"],
        "answer": "Central Processing Unit"
    }
    question_5 = {
        "question": "Which gas do plants primarily absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Carbon dioxide"
    }

    #list of dictionary of questions
    questions_list = [question_1, question_2, question_3, question_4, question_5]

    print("Answer the following questions with the correct option.")
    random.shuffle(questions_list)
    score = 0

    for item in questions_list:
        print(f"Question: {item['question']}")
        print("Options:")
        options = item["options"]
        shuffled = random.sample(options, k=len(options))
        for idx, options in enumerate(shuffled):
            print(f"{ascii_uppercase[idx]}. {options}")

        if str(input("Your Answer: ").upper()) == ascii_uppercase[shuffled.index(item["answer"])]:
            score += 1

    print(f"You answered {score} questions correctly.")


#BONUS CHALLENGE: SET PUZZLE GAME
def set_puzzle_game():
    import random
    num_list = []
    for i in range(20):
        num_list.append(random.randint(1,10))

    unique_num = set(num_list)
    try:
        guess = int(input("Guess how many unique numbers: "))
        if guess == len(unique_num):
            print("Correct!")
        else:
            print("Wrong.")
        print(f"There were {len(unique_num)} unique numbers in the list.")
    except ValueError:
        print("You need to put numbers.")
    print(f"The unique numbered numbers are: {unique_num}")

