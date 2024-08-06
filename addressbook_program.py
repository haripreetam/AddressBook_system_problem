import json
import os
from typing import List


class Contact:
    def __init__(self, first_name: str, last_name: str, address: str, city: str, state: str, zip_code: int, phone_number: int, email: str):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__address: str = address
        self.__city: str = city
        self.__state: str = state
        self.__zip_code: int = zip_code
        self.__phone_number: int = phone_number
        self.__email: str = email

    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name} {self.__address} {self.__city} {self.__state} {self.__zip_code} {self.__phone_number} {self.__email}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Contact):
            return self.__first_name == other.__first_name and self.__last_name == other.__last_name
        return False

    def to_dict(self) -> dict:
        """Convert the contact to a dictionary format."""
        return {
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "address": self.__address,
            "city": self.__city,
            "state": self.__state,
            "zip_code": self.__zip_code,
            "phone_number": self.__phone_number,
            "email": self.__email
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a contact object from a dictionary."""
        return cls(
            data["first_name"],
            data["last_name"],
            data["address"],
            data["city"],
            data["state"],
            data["zip_code"],
            data["phone_number"],
            data["email"]
        )

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_address(self) -> str:
        return self.__address

    def get_city(self) -> str:
        return self.__city

    def get_state(self) -> str:
        return self.__state

    def get_zip_code(self) -> int:
        return self.__zip_code

    def get_phone_number(self) -> int:
        return self.__phone_number

    def get_email(self) -> str:
        return self.__email

    def get_full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"


class AddressBook:
    def __init__(self, name: str):
        self.__name = name
        self.__file_path = f'{self.__name}.json'

    def __str__(self) -> str:
        return self.__name

    def add_contact(self) -> None:
        first_name: str = input("Enter First Name: ")
        last_name: str = input("Enter Last Name: ")
        address: str = input("Enter Address: ")
        city: str = input("Enter City: ")
        state: str = input("Enter State: ")
        zip_code: int = int(input("Enter Zip Code: "))
        phone_number: int = int(input("Enter Phone Number: "))
        email: str = input("Enter Email: ")

        contact: Contact = Contact(
            first_name, last_name, address, city, state, zip_code, phone_number, email)

        if self.is_duplicate_contact(contact):
            print(
                f"Sorry, the contact with first name: {first_name} and last name: {last_name} already exists.")
        else:
            contacts = self.load_contacts_from_file()
            contacts.append(contact)
            self.save_contacts_to_file(contacts)
            print("Contact added successfully.")

    def is_duplicate_contact(self, new_contact: Contact) -> bool:
        '''Check if the contact already exists in the file.'''
        contacts = self.load_contacts_from_file()
        for contact in contacts:
            if contact == new_contact:
                return True
        return False

    def add_multiple_contacts(self, num_contacts: int) -> None:
        '''Add multiple contact to the address book'''
        for _ in range(num_contacts):
            print(f"\nAdding contact {_ + 1}:")
            self.add_contact()

    def load_contacts_from_file(self) -> List[Contact]:
        '''Load contacts from a JSON file.'''
        contacts = []
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for contact_data in data:
                        contact = Contact.from_dict(contact_data)
                        contacts.append(contact)
                except json.JSONDecodeError:
                    print("Error decoding JSON from file.")
        return contacts

    def show_all_contacts(self) -> None:
        '''Displaying all contacts'''
        contacts = self.load_contacts_from_file()
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(contact)

    def edit_contact(self) -> None:
        first_name: str = input(
            "Enter the First Name of the contact to edit: ")
        last_name: str = input("Enter the Last Name of the contact to edit: ")

        contacts = self.load_contacts_from_file()
        for i, contact in enumerate(contacts):
            if contact.get_first_name() == first_name and contact.get_last_name() == last_name:
                print("Contact found. Enter new details:")

                new_first_name: str = input(
                    "Enter new First Name (leave blank to keep current): ") or contact.get_first_name()
                new_last_name: str = input(
                    "Enter new Last Name (leave blank to keep current): ") or contact.get_last_name()
                new_address: str = input(
                    "Enter new Address (leave blank to keep current): ") or contact.get_address()
                new_city: str = input(
                    "Enter new City (leave blank to keep current): ") or contact.get_city()
                new_state: str = input(
                    "Enter new State (leave blank to keep current): ") or contact.get_state()
                new_zip_code: int = int(input(
                    "Enter new Zip Code (leave blank to keep current): ") or contact.get_zip_code())
                new_phone_number: int = int(input(
                    "Enter new Phone Number (leave blank to keep current): ") or contact.get_phone_number())
                new_email: str = input(
                    "Enter new Email (leave blank to keep current): ") or contact.get_email()

                updated_contact = Contact(new_first_name, new_last_name, new_address,
                                          new_city, new_state, new_zip_code, new_phone_number, new_email)

                contacts[i] = updated_contact

                self.save_contacts_to_file(contacts)
                print("Contact updated successfully.")
                return

        print("Contact not found.")

    def save_contacts_to_file(self, contacts: List[Contact]) -> None:
        '''Save contacts to a JSON file.'''
        data = [contact.to_dict() for contact in contacts]
        with open(self.__file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def delete_contact(self) -> None:
        first_name: str = input(
            "Enter the First Name of the contact to delete: ")
        last_name: str = input(
            "Enter the Last Name of the contact to delete: ")

        contacts = self.load_contacts_from_file()
        for i, contact in enumerate(contacts):
            if contact.get_first_name() == first_name and contact.get_last_name() == last_name:
                del contacts[i]
                self.save_contacts_to_file(contacts)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    def search_contacts_by_city_or_state(self, search_term: str) -> List[Contact]:
        contacts = self.load_contacts_from_file()
        return [contact for contact in contacts if contact.get_city() == search_term or contact.get_state() == search_term]

    def count_contacts_by_city(self, city: str) -> int:
        contacts = self.load_contacts_from_file()
        return sum(1 for contact in contacts if contact.get_city() == city)

    def count_contacts_by_state(self, state: str) -> int:
        contacts = self.load_contacts_from_file()
        return sum(1 for contact in contacts if contact.get_state() == state)

    def sort_contacts(self, key_func) -> List[Contact]:
        contacts = self.load_contacts_from_file()
        return sorted(contacts, key=key_func)

    def sort_contacts_by_city(self) -> None:
        '''Sorting contacts by city.'''
        sorted_contacts = self.sort_contacts(
            lambda contact: contact.get_city())
        for contact in sorted_contacts:
            print(contact)

    def sort_contacts_by_state(self) -> None:
        '''Sorting contacts by state.'''
        sorted_contacts = self.sort_contacts(
            lambda contact: contact.get_state())
        for contact in sorted_contacts:
            print(contact)

    def sort_contacts_by_zip(self) -> None:
        '''Sorting contacts by Zipcode.'''
        sorted_contacts = self.sort_contacts(
            lambda contact: contact.get_zip_code())
        for contact in sorted_contacts:
            print(contact)

    def sort_contacts_by_name(self) -> None:
        sorted_contacts = self.sort_contacts(
            lambda contact: contact.get_full_name())
        for contact in sorted_contacts:
            print(contact)


class AddressBookMain:
    def __init__(self):
        self.__address_books: List[AddressBook] = []

    def add_address_book(self) -> None:
        '''Adding new address book'''
        name: str = input("Enter the name of the new address book: ")
        address_book = AddressBook(name)
        self.__address_books.append(address_book)
        print("Address book created successfully.")

    def get_address_book(self, name: str) -> AddressBook:
        for address_book in self.__address_books:
            if str(address_book) == name:
                return address_book
        print(f"Address book with name {name} not found.")
        return None  # type: ignore

    def delete_address_book(self) -> None:
        name: str = input("Enter the name of the address book to delete: ")
        address_book = self.get_address_book(name)
        if address_book:
            self.__address_books.remove(address_book)
            os.remove(f'{name}.json')
            print("Address book deleted successfully.")
        else:
            print("Address book not found.")

    def show_all_address_books(self) -> None:
        if not self.__address_books:
            print("No address books found.")
        else:
            print("Available Address Books:")
            for address_book in self.__address_books:
                print(f"- {address_book}")

    def load_all_address_books(self) -> None:
        '''Load all address books from the current directory.'''
        for file_name in os.listdir('.'):
            if file_name.endswith('.json'):
                name = file_name.split('.')[0]
                address_book = AddressBook(name)
                self.__address_books.append(address_book)


def main():
    address_book_main = AddressBookMain()
    address_book_main.load_all_address_books()

    while True:
        print("\n--- Address Book Management ---")
        print("1. Create a new address book")
        print("2. Delete an address book")
        print("3. Show all address books")
        print("4. Access an address book")
        print("5. Exit")

        choice: str = input("Enter your choice (1-5): ")

        if choice == '1':
            address_book_main.add_address_book()
        elif choice == '2':
            address_book_main.delete_address_book()
        elif choice == '3':
            address_book_main.show_all_address_books()
        elif choice == '4':
            address_book_name = input(
                "Enter the name of the address book to access: ")
            address_book = address_book_main.get_address_book(
                address_book_name)
            if address_book:
                while True:
                    print(f"\n--- Address Book: {address_book_name} ---")
                    print("1. Add a contact")
                    print("2. Add multiple contacts")
                    print("3. Show all contacts")
                    print("4. Edit a contact")
                    print("5. Delete a contact")
                    print("6. Search contacts by city/state")
                    print("7. Count contacts by city/state")
                    print("8. Sort contacts by name")
                    print("9. Sort contacts by city")
                    print("10. Sort contacts by state")
                    print("11. Sort contacts by zip")
                    print("12. Back to main menu")

                    choice: str = input("Enter your choice (1-12): ")

                    if choice == '1':
                        address_book.add_contact()
                    elif choice == '2':
                        num_contacts: int = int(
                            input("Enter the number of contacts to add: "))
                        address_book.add_multiple_contacts(num_contacts)
                    elif choice == '3':
                        address_book.show_all_contacts()
                    elif choice == '4':
                        address_book.edit_contact()
                    elif choice == '5':
                        address_book.delete_contact()
                    elif choice == '6':
                        search_term: str = input(
                            "Enter city or state to search contacts: ")
                        results = address_book.search_contacts_by_city_or_state(
                            search_term)
                        if results:
                            for contact in results:
                                print(contact)
                        else:
                            print("No contacts found.")
                    elif choice == '7':
                        city: str = input("Enter city to count contacts: ")
                        count_city = address_book.count_contacts_by_city(city)
                        print(f"Number of contacts in {city}: {count_city}")

                        state: str = input("Enter state to count contacts: ")
                        count_state = address_book.count_contacts_by_state(
                            state)
                        print(f"Number of contacts in {state}: {count_state}")
                    elif choice == '8':
                        address_book.sort_contacts_by_name()
                    elif choice == '9':
                        address_book.sort_contacts_by_city()
                    elif choice == '10':
                        address_book.sort_contacts_by_state()
                    elif choice == '11':
                        address_book.sort_contacts_by_zip()
                    elif choice == '12':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()