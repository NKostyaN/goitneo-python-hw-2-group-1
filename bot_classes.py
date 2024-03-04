# this classes will be added in bot after 3-rd HW
import bot_utils as utils
from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.data = UserDict()

    def add_record(self, record):
        self.data.update({str(record.name): record})

    def delete(self, record):
        self.data.pop(record)

    def find(self, name):
        return self.data.get(name)


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        name = name.capitalize()  # just for exemple
        self.name = name
        super().__init__(name)

    def __str__(self):
        return str(self.name)


class Phone(Field):
    def __init__(self, phone):
        phone = utils.strip_phone_number(phone)
        self.phone = phone
        super().__init__(phone)

    def set_phone(self, phone):
        self.value = phone

    def __str__(self):
        return str(self.phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.set_phone(new_phone)

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item


def main():
    book = AddressBook()

    oleh_record = Record("oLeh")
    oleh_record.add_phone("380-50-123-45-67")
    oleh_record.add_phone("+(380)-67-61-888-67")
    book.add_record(oleh_record)

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    john.remove_phone("5555555555")

    book.delete("Jane")

    for name, record in book.data.items():
        print(record)


if __name__ == "__main__":
    main()
