contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added!")

def view_contacts():
    for name, phone in contacts.items():
        print(name, ":", phone)

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
