class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")
        self.address_book: AddressBook = AddressBook()
        self.__run()

    def __menu(self) -> None:
        print(f'{"-"*10} Select Option {"-"*10}')
        print('1. Add Contact')
        print('2. Add Multiple Contacts')
        print('3. Show All Contacts')
        print('4. Edit Contact')
        print('5. Delete Contact')
        print('6. Exit')

    def __run(self) -> None:
        while True:
            self.__menu()
            option: int = self.__get_valid_int_input('Enter your option: ')
            if option == 1:
                self.__add_contact()
            elif option == 2:
                self.__add_multiple_contacts()
            elif option == 3:
                self.__show_all_contacts()
            elif option == 4:
                self.__edit_contact()
            elif option == 5:
                self.__delete_contact()
            elif option == 6:
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

    def __add_contact(self) -> None:
        self.address_book.add_contact()

    def __add_multiple_contacts(self) -> None:
        num_contacts: int = self.__get_valid_int_input("Enter the number of contacts to add: ")
        for _ in range(num_contacts):
            print(f"\nAdding contact {_ + 1}:")
            self.address_book.add_contact()

    def __show_all_contacts(self) -> None:
        contacts: list[Contact] = self.address_book.get_all_contacts()
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(contact)

    def __edit_contact(self) -> None:
        first_name: str = input("Enter the First Name of the contact to edit: ")
        last_name: str = input("Enter the Last Name of the contact to edit: ")
        success: bool = self.address_book.edit_contact(first_name, last_name)
        if success:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def __delete_contact(self) -> None:
        first_name: str = input("Enter the First Name of the contact to delete: ")
        last_name: str = input("Enter the Last Name of the contact to delete: ")
        success: bool = self.address_book.delete_contact(first_name, last_name)
        if success:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")


class AddressBook:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def add_contact(self) -> None:
        '''Add a new contact to the address book
        '''
        first_name: str = input("Enter First Name: ")
        last_name: str = input("Enter Last Name: ")
        address: str = input("Enter Address: ")
        city: str = input("Enter City: ")
        state: str = input("Enter State: ")
        zip_code: int = int(input("Enter Zip Code: "))
        phone_number: int = int(input("Enter Phone Number: "))
        email: str = input("Enter Email: ")
        contact: Contact = Contact(first_name, last_name, address, city,
                                   state, zip_code, phone_number, email)
        for c in self.__contacts:
            if contact == c:
                print(
                    f"Sorry, the contact with first name: {first_name} and last name: {last_name} already exists in AddressBook")
                return
        self.__contacts.append(contact)
        print("Contact added successfully.")

    def add_multiple_contacts(self, num_contacts: int) -> None:
        '''Add multiple contact to the address book
        '''
        for _ in range(num_contacts):
            print(f"\nAdding contact {_ + 1}:")
            self.add_contact()

    def get_all_contacts(self):
        return self.__contacts

    def edit_contact(self, first_name: str, last_name: str) -> bool:
        '''Edit a contact in the address book
        '''
        for i, contact in enumerate(self.__contacts):
            if contact.get_first_name() == first_name and contact.get_last_name() == last_name:
                print("Contact found. Enter new details:")
                new_first_name: str = input("Enter new First Name (leave blank to keep current): ") or contact.get_first_name()
                new_last_name: str = input("Enter new Last Name (leave blank to keep current): ") or contact.get_last_name()
                new_address: str = input("Enter new Address (leave blank to keep current): ") or contact.get_address()
                new_city: str = input("Enter new City (leave blank to keep current): ") or contact.get_city()
                new_state: str = input("Enter new State (leave blank to keep current): ") or contact.get_state()
                new_zip_code: int = int(input("Enter new Zip Code (leave blank to keep current): ") or contact.get_zip_code())
                new_phone_number: int = int(input("Enter new Phone Number (leave blank to keep current): ") or contact.get_phone_number())
                new_email: str = input("Enter new Email (leave blank to keep current): ") or contact.get_email()

                updated_contact = Contact(new_first_name, new_last_name, new_address, new_city, new_state, new_zip_code, new_phone_number, new_email)
                self.__contacts[i] = updated_contact
                return True
        return False

    def delete_contact(self, first_name: str, last_name: str) -> bool:
        '''Delete a contact from the address book by name'''
        for i, contact in enumerate(self.__contacts):
            if contact.get_first_name() == first_name and contact.get_last_name() == last_name:
                del self.__contacts[i]
                return True
        return False


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


if __name__ == "__main__":
    AddressBookMain()