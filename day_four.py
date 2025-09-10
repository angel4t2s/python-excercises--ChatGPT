
#TASK ONE: DIARY APP (FILE WRITER)
def diary_app__file_writer():
    import time

    with open("diary.txt", 'a') as diary:
        message = input("Write your diary: ").strip()
        #time something here [2025-08-18 14:35]
        time_object = time.localtime()
        diary.write(time.strftime("\n[%Y-%m-%d %H:%M]\n", time_object))
        diary.write(f"{message}\n")

#TASK TWO: NOTE READER
def notes_reader():
    try:
        with open("diary.txt") as note:
            print(note.read())
    except FileNotFoundError:
        print("No diary entries yet.")

#TASK THREE: CONTACT BOOK
def contact_book():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")

    with open("contacts.txt", 'a') as contacts:
        contacts.write(f"{name}, {phone}, {email}\n")
def search_name(name):
    search_word = name.title()
    with open("contacts.txt") as f:
        student = [line.strip() for line in f if search_word.lower() in line.lower()]
        print(student)
def contact_menu():
    print("Select option to continue:")
    print("1. Add contact")
    print("2. Search contact")
    try:
        option = int(input("Enter option: "))
        if option == 1:
            contact_book()
        elif option == 2:
            search_name(input("Enter contact name: "))
        else:
            print("Invalid option. Put 1 or 2.")
    except ValueError:
        print("Please enter a valid option (1-2).")

#TASK FOUR: WORD COUNTER (FILE ANALYZER)
def word_counter_file_analyzer():
    import string

    word_count = 0
    line_count = 0
    word_count_dict = {}
    try:
        filename = input("Enter file name: ")
        with open(filename, 'r') as file:
            word_file = file.read()

            # Getting total words
            for word in word_file.split():
                word_count +=1

            # Getting total lines
            for line in word_file.splitlines():
                line_count += 1

            # Converting to dictionary to count for most used word
            word_lower = word_file.lower()
            for word in word_lower.split():
                word = word.strip(string.punctuation)
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

        word_count_dict.pop('')
        most_used_word_number = max(word_count_dict.values())
        most_used_word = []
        for k in word_count_dict:
            if word_count_dict[k] == most_used_word_number:
                most_used_word.append(k)
            else:
                pass

        print(f"Total words: {word_count}.")
        print(f"Total lines: {line_count}.")
        if len(most_used_word) > 1:
            # print(f"Most used words: '{most_used_word}', used {most_used_word_number} times.")
            print(f"Most used words: ", end='')
            for word in most_used_word:
                print(word, end=', ')
            print(f"used {most_used_word_number} times.")
        else:
            print(f"Most used words is '{most_used_word[0]}', used {most_used_word_number} times.")
    except FileNotFoundError:
        print("File not found.")

#TASK FIVE: ERROR LOGGER
def error_logger():
    from datetime import datetime
    now = datetime.now().isoformat()

    number = input("Enter a number: ")
    try:
        compute = 100/int(number)
    except ValueError as e:
        with open("errors.log", 'a') as error:
            error.write(f"{e}\n{now}\n\n\n")
        print("You need to put number.")
    except ZeroDivisionError as e:
        with open("errors.log", 'a') as error:
            error.write(f"{e}\n{now}\n\n\n")
        print("Can't divide by zero.")

#BONUS CHALLENGE: STUDENT RECORDS DATABASE
def student_records_database():
    print("Select option to: ")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by name")
    print("4. Delete a student")
    try:
        option = int(input("Option: "))
        if option == 1:
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
                score = float(input("Enter student score: "))
            except ValueError:
                print("You need to put number.")

            with open("students.txt", 'a') as students:
                students.write(f"\n{name}, {age}, {score}")

            print("Student added successfully.")
        elif option == 2:
            with open("students.txt", 'r') as students:
                print(students.read())
        elif option == 3:
            name = input("Enter student name to search: ").title()
            with open("students.txt") as f:
                student = [line.strip() for line in f if name in line]
                print(student)
        elif option == 4:
            name = input("Enter student name to delete: ")
            with open("students.txt") as f:
                student = [line.strip() for line in f]
                try:
                    match = [item for item in student if name.lower() in item.lower()]
                    student.remove(match[0])
                    with open("students.txt", 'w') as students:
                        students.write(f"\n".join(student))
                        print(f"{name} deleted successfully.")
                    print("New records:")
                    print("\n".join(student))
                except FileNotFoundError:
                    print(f"{name} not found in records.")
                except ValueError:
                    print(f"{name} not found.")
                except IndexError:
                    print(f"{name} not found.")
        else:
            print("Invalid option.")
    except ValueError:
        print("You need to put a number (1 - 4).")
    except NameError:
        print("You need to select option (1 - 4).")

