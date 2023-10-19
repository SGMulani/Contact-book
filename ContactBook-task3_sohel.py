
#Task 3:- ContactBook

#--Contact Information: Store name, phone number, email, and address for each contact.
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


def add_contact(contact_list, name, phone, email, address):
    contact = Contact(name, phone, email, address)
    contact_list.append(contact)
    print(f"Contact '{name}' added successfully.")


def view_contacts(contact_list):
    if not contact_list:
        print("No contacts found.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contact_list, start=1):
        print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")


def search_contact(contact_list, search_term):
    matching_contacts = []
    for contact in contact_list:
        if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
            matching_contacts.append(contact)
    return matching_contacts


def update_contact(contact_list, old_name, new_name, new_phone, new_email, new_address):
    for contact in contact_list:
        if contact.name == old_name:
            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            contact.address = new_address
            print(f"Contact '{old_name}' updated successfully.")
            return
    print(f"Contact '{old_name}' not found.")


def delete_contact(contact_list, name):
    for contact in contact_list:
        if contact.name == name:
            contact_list.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print(f"Contact '{name}' not found.")


def main():
    contacts = []

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_contact(contacts, name, phone, email, address)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_term = input("Enter a name or phone number to search: ")
            matching_contacts = search_contact(contacts, search_term)
            if matching_contacts:
                view_contacts(matching_contacts)
            else:
                print("No matching contacts found.")
        elif choice == "4":
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new Name: ")
            new_phone = input("Enter new Phone: ")
            new_email = input("Enter new Email: ")
            new_address = input("Enter new Address: ")
            update_contact(contacts, old_name, new_name, new_phone, new_email, new_address)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
