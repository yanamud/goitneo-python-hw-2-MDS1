from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not all((len(value) == 10, value.isdigit())):
            raise ValueError("The number should contain 10 digits") 
        super().__init__(value)

class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [phone] if phone else []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f"Phone number {phone} add success to contact {self.name}"

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                del self.phones[self.phones.index(p)]
            return 'the phone was removed'
        else:
            return "The entered phone was not found"

    def edit_phone(self, old_phone,new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.insert(self.phones.index(p)+1,Phone(new_phone))
                del self.phones[self.phones.index(p)]
            return 'the phone was changed'
        else:
            return "The entered phone was not found"
               
    def find_phone(self, found_phone):
        for p in self.phones:
            if p.value == found_phone:
                return found_phone

    def __str__(self):
       return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return "The entered name was not found"

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "The record was removed"
        else:
            return "The entered name was not found"
       
if __name__ == '__main__':

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
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    
    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)