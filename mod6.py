from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        updated_phones = []
        for phone in self.phones:
            if phone.value != number:
                updated_phones.append(phone)
        self.phones = updated_phones

    def edit_phone(self, old_number, new_number):
        if not any(phone.value == old_number for phone in self.phones):
            raise ValueError("Old phone number is not exist")    
        
        if len(new_number) != 10 or not new_number.isdigit():
            raise ValueError("New phone number must be 10 digits")
        
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                break

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def __str__(self):
        phones = "; ".join([phone.value for phone in self.phones])
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
