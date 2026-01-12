phone_book = {}

while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phone_book:
            print("Phone Number:", phone_book[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Exiting Phone Book.")
        break

    else:
        print("Invalid choice. Try again.")
