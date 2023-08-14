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
def change_phone(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec: Record = adress_book.get_record(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    raise KeyError


@input_error
def whose_phone(*args):
    for key, value in adress_book.items():
        if args[0] == str(key):
            return value
    raise KeyError


# @input_error
def add(*args):
    if len(args) == 1:
        name = Name(args[0])
        rec: Record = adress_book.get(str(name))
        if rec:
            return 'That name is alresdy in your contacts'
        else:
            rec = Record(name)
            return adress_book.add_record(rec)
    else:
        name = Name(args[0])
        phone = Phone(args[1])
        rec: Record = adress_book.get(str(name))
        if rec:
            return rec.add_phone(phone)
        rec = Record(name, phone)
        return adress_book.add_record(rec)


def show_all(*args):
    return adress_book
    # for n, p in adress_book.items():
    #     return n, p
            


def hello(*args):
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
}

COMMANDS_EXIT = ['exit', 'quit', 'good bye', 'q']


def parser(text: str) -> tuple[callable, list]:
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
            if comand and len(args) > 1:
                result = comand(*args)
            else:
                result = comand(args[0])

            print(result)
            # print(adress_book)


if __name__ == '__main__':
    main()
