"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
        

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    # check for duplicate names
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists.")
                return
    # adding contacts
    with open(FILENAME, "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
        
        
def view_contacts():
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)        
        
        if len(rows) < 1:
            print("No contacts found")
            return
        
        print("Your Contacts: \n")
        for row in rows[1:]:    # slicing: [start:end]
            print(f"{row[0]} | {row[1]} | {row[2]}")


def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False
    
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if term == row["Name"].lower():
                print(f"{row['Name']} | 📞 {row['Phone']} | ✉️ {row['Email']}")
                found = True
    
    if not found:
        print("No matching contact found")
        
        

def main():
    while True:
        print("\n📔Contact Book:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our program")
            break
        else:
            PermissionError("Invalid choice of number")
            


if __name__ == "__main__":
    main()
    



"""
add update the contact (update_contact)
delete the contact  (delete_contact)

"""