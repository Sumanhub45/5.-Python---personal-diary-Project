

import os

class PersonalDiary:
    def __init__(self):
        self.diary_folder = "diary_entries"
        if not os.path.exists(self.diary_folder):
            os.mkdir(self.diary_folder)

    def add_entry(self):
        entry_date = input("Enter the date (e.g., YYYY-MM-DD): ")
        entry_text = input("Enter your diary entry: ")

        entry_filename = os.path.join(self.diary_folder, f"{entry_date}.txt")
        with open(entry_filename, "w") as file:
            file.write(entry_text)

        print("Diary entry added successfully!\n")

    def view_entries(self):
        print("Diary Entries:")
        for entry_filename in os.listdir(self.diary_folder):
            with open(os.path.join(self.diary_folder, entry_filename), "r") as file:
                entry_date = entry_filename.split(".")[0]
                entry_text = file.read()
                print(f"{entry_date}:\n{entry_text}\n")

    def edit_entry(self):
        entry_date = input("Enter the date of the entry you want to edit (e.g., YYYY-MM-DD): ")
        entry_filename = os.path.join(self.diary_folder, f"{entry_date}.txt")

        if os.path.exists(entry_filename):
            with open(entry_filename, "r") as file:
                current_entry_text = file.read()
                print(f"Current Diary Entry for {entry_date}:\n{current_entry_text}\n")

            new_entry_text = input("Enter the edited diary entry: ")
            with open(entry_filename, "w") as file:
                file.write(new_entry_text)

            print("Diary entry edited successfully!\n")
        else:
            print("Diary entry for the specified date does not exist.\n")

    def menu(self):
        while True:
            print("Personal Diary Menu:")
            print("1. Add Diary Entry")
            print("2. View Diary Entries")
            print("3. Edit Diary Entry")
            print("4. Exit")
            
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.view_entries()
            elif choice == '3':
                self.edit_entry()
            elif choice == '4':
                print("Exiting the Personal Diary Application.")
                break
            else:
                print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    diary = PersonalDiary()
    diary.menu()
