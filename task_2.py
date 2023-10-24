from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):   
    def check_phone(self,phone):
        if len(phone) != 10:
            return "The number should contain 10 digits"
        else:
            self.phone = phone

class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phone = Phone(phone)
        self.phones.append(self.phone)
        return self.phones

    def remove_phone(self,phone):
        self.phone = Phone(phone)

        for k, v in AddressBook.items():
            if v == self.phone:  
                AddressBook[k] = []
            return 'the phone was emoved'
        else:
            return "The entered phone was not found"

    def edit_phone(self,old_phone,new_phone):

        self.old_phone = old_phone
        self.new_phone = new_phone

        result = AddressBook.find.name

        for k, v in AddressBook.items():
            if v == old_phone and k == result:  
                AddressBook[k] = new_phone
            return 'the phone was updated'
        else:
            return "The entered phone was not found"
               
    def find_phone(self,found_phone):
        found_phone = Phone.check_phone
        if found_phone in AddressBook.keys():
            return found_phone
        else:
            return "The entered name was not found"

    def __str__(self):
       return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self,phone):
        key = Record(self.name)
        self.phone = Record.add_phone(phone)
  
        AddressBook[key] = self.phone
        return AddressBook
    
    def find(self, name):
        self.name = name
        if self.name in AddressBook.keys():
            return self.name
        else:
            return "The entered name was not found"

    def delete(self,name):
        self.name = name
        if self.name in AddressBook.keys():
            del AddressBook[self.name]
            return "The record was removed"
        else:
            return "The entered name was not found"

       