from collections import defaultdict
from typing import Callable


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
    def __init__(self):
        self.__contacts: list[Contact] = []
        self.__contacts_by_city: defaultdict[str,
                                             list[Contact]] = defaultdict(list)
        self.__contacts_by_state: defaultdict[str,
                                              list[Contact]] = defaultdict(list)

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
        if any(contact == c for c in self.__contacts):
            print(
                f"Sorry, the contact with first name: {first_name} and last name: {last_name} already exists.")
        else:
            self.__contacts.append(contact)
            self.__contacts_by_city[city].append(contact)
            self.__contacts_by_state[state].append(contact)
            print("Contact added successfully.")

    def add_multiple_contacts(self, num_contacts: int) -> None:
        '''Adding mutiple contacts'''
        for _ in range(num_contacts):
            print(f"\nAdding contact {_ + 1}:")
            self.add_contact()

    def show_all_contacts(self) -> None:
        '''Displaying all contacts'''
        if not self.__contacts:
            print("No contacts found.")
        else:
            for contact in self.__contacts:
                print(contact)

    def edit_contact(self) -> None:
        '''Editing contacts'''
        first_name: str = input(
            "Enter the First Name of the contact to edit: ")
        last_name: str = input("Enter the Last Name of the contact to edit: ")
        success: bool = self.edit_contact_details(first_name, last_name)
        if success:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def edit_contact_details(self, first_name: str, last_name: str) -> bool:
        '''Editing contacts by firstname and lastname'''
        for i, contact in enumerate(self.__contacts):
            if contact.get_first_name() == first_name and contact.get_last_name() == last_name:
                print("Contact found. Enter new details:")
                old_city, old_state = contact.get_city(), contact.get_state()

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
                self.__contacts[i] = updated_contact

                # Update dictionaries
                self.__contacts_by_city[old_city].remove(contact)
                self.__contacts_by_state[old_state].remove(contact)
                self.__contacts_by_city[new_city].append(updated_contact)
                self.__contacts_by_state[new_state].append(updated_contact)

                return True
        return False
    

    def sort_contacts(self, key_func) -> None:
        sorted_contacts = sorted(self.__contacts, key=key_func)
        for contact in sorted_contacts:
            print(contact)

    def sort_contacts_by_city(self) -> None:
        '''sorting contacts by city'''
        self.sort_contacts(lambda contact: contact.get_city())

    def sort_contacts_by_state(self) -> None:
        '''sorting contacts by state'''
        self.sort_contacts(lambda contact: contact.get_state())

    def sort_contacts_by_zip(self) -> None:
        '''sorting contacts by zipcode.'''
        self.sort_contacts(lambda contact: contact.get_zip_code())

    def delete_contact(self) -> None:
        first_name: str = input(
            "Enter the First Name of the contact to delete: ")
        last_name: str = input(
            "Enter the Last Name of the contact to delete: ")
        success: bool = self.delete_contact_details(first_name, last_name)
        if success:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def delete_contact_details(self, first_name: str, last_name: str) -> bool:
        '''deleting contacts by firstname and lastname'''
        for i, contact in enumerate(self.__contacts):
            if contact.get_first_name() == first_name and contact.get_last_name() == last_name:
                self.__contacts_by_city[contact.get_city()].remove(contact)
                self.__contacts_by_state[contact.get_state()].remove(contact)
                del self.__contacts[i]
                return True
        return False

    def search_contacts_by_city_or_state(self, search_term: str) -> list[Contact]:
        return [contact for contact in self.__contacts if contact.get_city() == search_term or contact.get_state() == search_term]

    def get_contacts_by_city(self, city: str) -> list[Contact]:
        return self.__contacts_by_city[city]

    def get_contacts_by_state(self, state: str) -> list[Contact]:
        return self.__contacts_by_state[state]

    def count_contacts_by_city(self, city: str) -> int:
        return len(self.__contacts_by_city[city])

    def count_contacts_by_state(self, state: str) -> int:
        return len(self.__contacts_by_state[state])

    def sort_contacts_by_name(self) -> None:
        sorted_contacts = sorted(
            self.__contacts, key=lambda contact: contact.get_full_name())
        for contact in sorted_contacts:
            print(contact)


class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")
        self.__address_books: dict[str, AddressBook] = {}
        self.__run()

    def __menu(self) -> None:
        print(f'{"-"*10} Select Option {"-"*10}')
        print('1. Create New Address Book')
        print('2. Select Address Book')
        print('3. Show All Address Books')
        print('4. Delete Address Book')
        print('5. Search Contacts by City or State')
        print('6. View Contacts by City')
        print('7. View Contacts by State')
        print('8. Count Contacts by City')
        print('9. Count Contacts by State')
        print('10. Sort Contacts by Name')
        print('11. Exit')

    def __run(self) -> None:
        while True:
            self.__menu()
            option: int = self.__get_valid_int_input('Enter your option: ')
            if option == 1:
                self.__create_address_book()
            elif option == 2:
                self.__select_address_book()
            elif option == 3:
                self.__show_all_address_books()
            elif option == 4:
                self.__delete_address_book()
            elif option == 5:
                self.__search_contacts_by_city_or_state()
            elif option == 6:
                self.__view_contacts_by_city()
            elif option == 7:
                self.__view_contacts_by_state()
            elif option == 8:
                self.__count_contacts_by_city()
            elif option == 9:
                self.__count_contacts_by_state()
            elif option == 10:
                self.__sort_contacts_by_name()
            elif option == 11:
                print("Exiting Address Book Program")
                break
            else:
                print("Invalid option, please try again.")

    def __get_valid_int_input(self, prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def __create_address_book(self) -> None:
        name: str = input("Enter the name of the new Address Book: ")
        if name in self.__address_books:
            print(f"An Address Book with the name '{name}' already exists.")
        else:
            self.__address_books[name] = AddressBook()
            print(f"Address Book '{name}' created successfully.")

    def __select_address_book(self) -> None:
        name: str = input("Enter the name of the Address Book to select: ")
        if name not in self.__address_books:
            print(f"Address Book '{name}' not found.")
            return

        address_book = self.__address_books[name]
        print(f"Selected Address Book: {name}")
        self.__manage_address_book(address_book)

    def __manage_address_book(self, address_book: AddressBook) -> None:
        while True:
            print(f'{"-"*10} Manage Address Book {"-"*10}')
            print('1. Add Contact')
            print('2. Add Multiple Contacts')
            print('3. Show All Contacts')
            print('4. Edit Contact')
            print('5. Delete Contact')
            print('6. Sort Contacts by Name')
            print('7. Sort Contacts by City')
            print('8. Sort Contacts by State')
            print('9. Sort Contacts by Zip')
            print('10. Back to Main Menu')
            option: int = self.__get_valid_int_input('Enter your option: ')
            if option == 1:
                address_book.add_contact()
            elif option == 2:
                num_contacts: int = self.__get_valid_int_input("Enter the number of contacts to add: ")
                address_book.add_multiple_contacts(num_contacts)
            elif option == 3:
                address_book.show_all_contacts()
            elif option == 4:
                address_book.edit_contact()
            elif option == 5:
                address_book.delete_contact()
            elif option == 6:
                address_book.sort_contacts_by_name()
            elif option == 7:
                address_book.sort_contacts_by_city()
            elif option == 8:
                address_book.sort_contacts_by_state()
            elif option == 9:
                address_book.sort_contacts_by_zip()
            elif option == 10:
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid option, please try again.")
                
    def __show_all_address_books(self) -> None:
        if not self.__address_books:
            print("No address books found.")
        else:
            print("Available Address Books:")
            for name in self.__address_books:
                print(f"- {name}")

    def __delete_address_book(self) -> None:
        name: str = input("Enter the name of the Address Book to delete: ")
        if name in self.__address_books:
            del self.__address_books[name]
            print(f"Address Book '{name}' deleted successfully.")
        else:
            print(f"Address Book '{name}' not found.")

    def __search_contacts_by_city_or_state(self) -> None:
        search_term: str = input(
            "Enter the City or State to search for contacts: ")
        found_contacts: list[Contact] = []

        for address_book in self.__address_books.values():
            found_contacts.extend(
                address_book.search_contacts_by_city_or_state(search_term))

        if found_contacts:
            print(
                f"Found {len(found_contacts)} contact(s) in '{search_term}':")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found in '{search_term}'.")

    def __view_contacts_by_city(self) -> None:
        city: str = input("Enter the city to view contacts: ")
        found_contacts: list[Contact] = []

        for address_book in self.__address_books.values():
            found_contacts.extend(address_book.get_contacts_by_city(city))

        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s) in '{city}':")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found in '{city}'.")

    def __view_contacts_by_state(self) -> None:
        state: str = input("Enter the state to view contacts: ")
        found_contacts: list[Contact] = []

        for address_book in self.__address_books.values():
            found_contacts.extend(address_book.get_contacts_by_state(state))

        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s) in '{state}':")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found in '{state}'.")

    def __count_contacts_by_city(self) -> None:
        city: str = input("Enter the city to count contacts: ")
        total_contacts: int = 0

        for address_book in self.__address_books.values():
            total_contacts += address_book.count_contacts_by_city(city)

        print(f"Total contacts in '{city}': {total_contacts}")

    def __count_contacts_by_state(self) -> None:
        state: str = input("Enter the state to count contacts: ")
        total_contacts: int = 0

        for address_book in self.__address_books.values():
            total_contacts += address_book.count_contacts_by_state(state)

        print(f"Total contacts in '{state}': {total_contacts}")

    def __sort_contacts_by_name(self) -> None:
        address_book_name: str = input(
            "Enter the name of the Address Book to sort contacts: ")
        if address_book_name not in self.__address_books:
            print(f"Address Book '{address_book_name}' not found.")
            return

        address_book = self.__address_books[address_book_name]
        address_book.sort_contacts_by_name()


if __name__ == "__main__":
    AddressBookMain()