from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
   
    def __init__(self, value):
        super().__init__(value) 
        self.name = value


class Phone(Field):
    def __init__(self, value):
        self.value = value
        if len(value) != 10:                  # Функция валидации номера(строго 10 цифр)
            raise ValueError(f"The number should contains 10 digits" )
        if not value.isdigit():
            raise ValueError(f"The number should contains 10 digits" )
        

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone) == None:
            raise ValueError(F" Please, check if the phone number is correct?")
        self.phones.insert(self.phones.index(self.find_phone((old_phone))), Phone(new_phone)) 
        self.phones.remove(self.find_phone(old_phone))

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return (i)  
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find(self, name):
            return self.data.get(name)
            
    def delete(self,name):
        self.data.pop(name,None)
                
    
    def __str__(self):
            return f"Contacts info: {'; '.join(str(p) for p in self.data.values())} "    
  

           
                
book = AddressBook()
john_record = Record("John")
jane_record = Record("Jane")
vasya = Record("Vasya")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("1234567891")
# john_record.remove_phone("1234567890")
book.add_record(john_record)
jane_record.add_phone("9876543210")
book.add_record(jane_record)
book.add_record(vasya)
vasya.add_phone("9876543200")
print(book)
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")
print(book)


