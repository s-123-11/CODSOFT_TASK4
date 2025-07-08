# contact_book.py
contacts = {}

def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Show All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for name in contacts:
                print(name, ":", contacts[name])

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
