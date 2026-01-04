import datetime

def add_study_session():
    subject = input("Enter subject name: ")
    time_spent = input("Enter time studied (in minutes): ")
    topic = input("Enter covered Topic:")
       
    date = datetime.date.today()

    record = f"{date} | {subject} | {time_spent}|{topic} minutes\n"

    file = open("study_data.txt", "a")
    file.write(record)
    file.close()

    print("Study session saved successfully 👍")

def view_study_history():
    try:
        file = open("study_data.txt", "r")
        data = file.read()
        file.close()

        if data == "":
            print("No study records found.")
        else:
            print("\n--- Study History ---")
            print(data)

    except FileNotFoundError:
        print("No study data file found.")

def motivation():
    messages = [
        "Small steps every day lead to big success.",
        "Consistency is more important than speed.",
        "You are building your future right now."
    ]

    print("Motivation for you:")
    print(messages[datetime.datetime.now().second % 3])

while True:
    print("\nSMART STUDY COMPANION")
    print("1. Add Study Session")
    print("2. View Study History")
    print("3. Get Motivation")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_study_session()
    elif choice == "2":
        view_study_history()
    elif choice == "3":
        motivation()
    elif choice == "4":
        print("Keep studying. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
