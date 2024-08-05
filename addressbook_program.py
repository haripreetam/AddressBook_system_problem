class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")

class AddressBook:
    def __init__(self):
        self.contacts:list = []

class Contact:
    '''Add a new contact to the address book
    '''
    def __init__(self, first_name:str, last_name:str, address:str, city:str, state:str, zip_code:str, phone_number:str, email:str):
        self._first_name:str = first_name
        self._last_name:str = last_name
        self._address:str = address
        self._city:str = city
        self._state:str = state
        self._zip_code:str = zip_code
        self._phone_number:str = phone_number
        self._email:str = email

    def __str__(self):
        return f"{self._first_name} {self._last_name}, {self._address}, {self._city}, {self._state}, {self._zip_code}, {self._phone_number}, {self._email}"


if __name__ == "__main__":
    AddressBookMain()
    address_book1 = AddressBook()
    contact1 = Contact(first_name="Haripreetam", last_name="Reddy", address="Tata La montena", city="Talegaon Dabhade", state="MH", zip_code="410506", phone_number="91 7264861580", email="haripreetam333@gmail.com")
    address_book1.contacts.append(contact1)
    print(address_book1.contacts[0])