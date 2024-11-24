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
        # self.validation(value) 
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
        self.phones.append((Phone(phone)))

    def remove_phone(self, phone):
        self.phone = Phone(phone)
        
        for i in self.phones:
            if str(i)== str((self.phone)):
                self.phones.remove(i)


    def edit_phone(self, old_phone, new_phone):

        self.old_phone = Phone(old_phone)
        self.new_phone = Phone(new_phone)
        b = []
        
        try:
            [b.append(str(i))for i in self.phones]
            b.insert(b.index(old_phone), ((new_phone))) # Вставка нового номера телефона в список на место старого
            b.remove(old_phone) # Удаление старого номера телефона
            self.phones.clear()
            [self.phones.append(Phone(i))for i in b]
        except:
            ValueError(F" Please, check if the phone number is correct?")
       

    def find_phone(self, phone):
        self.phone = Phone(phone)
        for i in self.phones:
            if str(i)== str((self.phone)):
                return (i)  

    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.record = record
        self.data[record.name.value] = self.record

    def find(self, name):
        self.name = name
        for key in self.data:
            if key == self.name:
                self.record = self.data.get(key)
                return self.record 
            
    def delete(self,name):
        self.name = name        
        for key in self.data:
            if key == self.name:
                self.data.pop(key,None)
                return self.data
    
    def __str__(self):
        for k,v in self.data.items():
            return f"Contact name: {k}, phones: {'; '.join(p.value for p in v.phones) } "    
  

           
                
book = AddressBook()
john_record = Record("John")
jane_record = Record("Jane")
vasya = Record("Vasya")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
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

