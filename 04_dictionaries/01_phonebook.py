# ------------------------PROBLEM STATEMENT:
'''
In this program we show an example of using dictionaries to keep track of information in a phonebook.
'''

def read_phone_numbers():
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Enter name (or leave blank to finish): ")
        if name == "":  # Stop if the user enters an empty string
            break
        number = input("Enter phone number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("Phonebook entries: ")
        for name, number in phonebook.items():
            print(f"Name: {name}, Phone Number: {number}")

def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup (or leave blank to stop): ")
        if name == "":  # Stop if the user enters an empty string
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"Phone number for {name}: {phonebook[name]}")

def add_contact(phonebook):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    phonebook[name] = phone
    print("Contact added successfully!")

def main():
    phonebook = read_phone_numbers()  # Collect initial contacts

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            print_phonebook(phonebook)
        elif choice == "3":
            lookup_numbers(phonebook)
        elif choice == "4":
            print("Thank you! Have a nice day.")
            break
        else:
            print("Invalid choice. Please try again.")

# Python boilerplate.
if __name__ == '__main__':
    main()
