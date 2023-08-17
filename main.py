from adress_book import Adress_book, Name, Phone, Record


adress_book = Adress_book()


def input_error(func):
    def inner_func(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Please enter command, name, phone number'
        except ValueError:
            return 'Pleease enter correct number'
        except KeyError:
            return 'Name is not in phone book'
        except TypeError:
            return 'Unknown comand'
    return inner_func


@input_error
def del_phone(name, phone):
    rec: Record = adress_book.get_record(str(name))
    if rec:
        return rec.remove_phone(Phone(phone))
    raise KeyError


@input_error
def change_phone(name, old_phone, new_phone):
    rec: Record = adress_book.get_record(str(name))
    if rec:
        return rec.change_phone(Phone(old_phone), Phone(new_phone))
    raise KeyError


@input_error
def whose_phone(name):
    for key, value in adress_book.items():
        if Name(name).value == str(key):
            return value
    raise KeyError


@input_error
def add(name, phone = None):
        rec: Record = adress_book.get(str(name))
        if rec:
            return rec.add_phone(Phone(phone))
        rec = Record(Name(name), Phone(phone))
        return adress_book.add_record(rec)
   

def show_all(args):
    return adress_book            


def hello(args):
    return 'How can I help you?'


def no_comand():
    return 'Please enter your comand'


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change_phone,
    'phone': whose_phone,
    'show all': show_all,
    'no comands': no_comand,
    'del': del_phone,
}

COMMANDS_EXIT = ['exit', 'quit', 'good bye', 'q']


def parser(text: str):
    for kwd, comand in COMMANDS.items():
        if text.lower().startswith(kwd):
            args = text[len(kwd):].strip().split(' ')
            return comand, args
    return no_comand, []


def main():
    while True:
        user_input = input('Please enter comand:')
        if not user_input:
            no_comand()
        elif user_input.lower() in COMMANDS_EXIT:
            break
        else:
            comand, args = parser(user_input)
            result = comand(*args)
            print(result)


if __name__ == '__main__':
    main()
