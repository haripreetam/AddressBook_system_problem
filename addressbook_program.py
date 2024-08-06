class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")

class AddressBook:
    def __init__(self):
        self.__contacts: list = []

    def add_contact(self):
        '''Add a new contact to the address book
        '''
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        contact = Contact(first_name, last_name, address, city,
                          state, zip_code, phone_number, email)
        for c in self.__contacts:
            if contact == c:
                print(
                    f"Sorry these contact with frist name: {first_name} and last name: {last_name} allready exist in AddressBook")
                return
        self.__contacts.append(contact)

    def get_all_contacts(self):
        return self.__contacts


class Contact:
    def __init__(self, first_name: str, last_name: str, address: str, city: str, state: str, zip_code: str, phone_number: str, email: str):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__address: str = address
        self.__city: str = city
        self.__state: str = state
        self.__zip_code: str = zip_code
        self.__phone_number: str = phone_number  # TODO ph no in int
        self.__email: str = email

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}, {self.__address}, {self.__city}, {self.__state}, {self.__zip_code}, {self.__phone_number}, {self.__email}"

    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.__first_name == other.__first_name and self.__last_name == other.__last_name
        return False


if __name__ == "__main__":
    AddressBookMain()
    address_book1 = AddressBook()
    address_book1.add_contact()
    print(address_book1.get_all_contacts()[0])