import os
import json

# Define the file path for the phone book data
phonebook_file = 'phonebook.json'

# Function to load phone book data from a file
def load_phonebook():
    if os.path.exists(phonebook_file):
        with open(phonebook_file, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save phone book data to a file
def save_phonebook(phonebook_data):
    with open(phonebook_file, 'w') as file:
        json.dump(phonebook_data, file, indent=4)

# Function to add a contact to the phone book
def add_contact(name, number):
    phonebook = load_phonebook()
    phonebook[name] = number
    save_phonebook(phonebook)
    print(f"Contact '{name}' added successfully.")

# Function to search for a contact in the phone book
def search_contact(name):
    phonebook = load_phonebook()
    if name in phonebook:
        print(f"Contact: {name}\nPhone Number: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found in the phone book.")

# Function to update a contact's phone number
def update_contact(name, new_number):
    phonebook = load_phonebook()
    if name in phonebook:
        phonebook[name] = new_number
        save_phonebook(phonebook)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found in the phone book.")

# Function to delete a contact from the phone book
def delete_contact(name):
    phonebook = load_phonebook()
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in the phone book.")

# Main program loop
while True:
    print("\nPhone Book Options:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's phone number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Enter the contact's name to search: ")
        search_contact(name)
    elif choice == '3':
        name = input("Enter the contact's name to update: ")
        new_number = input("Enter the new phone number: ")
        update_contact(name, new_number)
    elif choice == '4':
        name = input("Enter the contact's name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
