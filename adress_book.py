from collections import UserDict


class Field:
    

    def __init__(self, value:str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.value
    

class Name(Field):
    ...


class Phone(Field):
    ...


class Record:


    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def __str__(self) -> str:
        return f'{self.name}: {", ".join(str(p) for p in self.phones)}'

    # def __repr__(self):
    #     return str(self)

    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f'{phone} added to contact {self.name}'
        return f'{phone} is already in {self.name} list'
    
    def remove_phone(self, phone: Phone):
        if phone.value in [p.value for p in self.phones]:
            self.phones.remove(phone)
            return f'{phone} removed'
        return f'{phone} is not in your address book'
        
    def change_phone(self, old_phone: Phone, new_phone:Phone):
        for num, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[num] = new_phone
                return f'An old phone {old_phone} chenged for a new one:{new_phone}'
        return f'{old_phone} is not in {self.name}"s contacts'



class Adress_book(UserDict):


    def add_record(self, record: Record):
        key = record.name.value
        self.data[key] = record
        return f'{key} added succesfuly'
    # # else:
    #     key = record.name
    #     self.data[key] = []
    #     return f'only name {key} added'

    def get_record(self, key):
        return self.data[key]

    # def __repr__(self) -> str:
    #     return str(self)

    def __str__(self) -> str:
        return '\n'.join(str(i) for i in self.data.values())


