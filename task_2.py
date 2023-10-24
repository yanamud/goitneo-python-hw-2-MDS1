from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...
    # def __init__(self, name):
    #     self.name = name


class Phone(Field):
    def __init__(self, value):
        if not all((len(value) == 10, value.isdigit())):
            raise ValueError("The number should contain 10 digits") 
        super().__init__(value)
    # def check_phone(self, phone):
    #     if len(phone) != 10:
    #         return 
    #     else:
    #         self.phone = phone


class Record:

    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [phone] if phone else []

    def add_phone(self, phone):
        # phone = Phone(phone)
        self.phones.append(Phone(phone))
        return f"Phone number {phone} add success to contact {self.name}"

    def remove_phone(self, phone):
        # self.phone = Phone(phone)

        # for k, v in AddressBook.items():
        for p in self.phones:
            if p.value == phone:
                del self.phones[self.phones.index(p)]
            # if v == self.phone:  
            #     AddressBook[k] = []
            return 'the phone was emoved'
        else:
            return "The entered phone was not found"

    def edit_phone(self, old_phone,new_phone):
        ...
        # self.old_phone = old_phone
        # self.new_phone = new_phone

        # result = AddressBook.find.name

        # for k, v in AddressBook.items():
        #     if v == old_phone and k == result:  
        #         AddressBook[k] = new_phone
        #     return 'the phone was updated'
        # else:
        #     return "The entered phone was not found"
               
    def find_phone(self, found_phone):
        ...
        # found_phone = Phone.check_phone
        # if found_phone in AddressBook.keys():
        #     return found_phone
        # else:
        #     return "The entered name was not found"

    def __str__(self):
       return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        # key = Record(self.name)
        # self.phone = Record.add_phone(phone)
  
        # AddressBook[key] = self.phone
        # return AddressBook
    
    def find(self, name):
        # self.name = name
        if name in self.data:
            return self.data[name]
        else:
            return "The entered name was not found"

    def delete(self, name):
        # self.name = name
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
    jane_record.add_phone("9876543217")
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