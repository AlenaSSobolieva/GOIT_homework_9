ADDRESS_BOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please"
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Give me name and phone please"
        except TypeError:
            return "Give me name and phone please"
    return wrap


@input_error
def hello_handler(data):
    return 'How can I help you?'


@input_error
def add_handler(data):
    name = data[0].title()
    phone = data[1]
    ADDRESS_BOOK[name] = phone
    return f'Contact {name} was saved with phone number {phone}.'


@input_error
def change_handler(data):
    if data[0].title() in ADDRESS_BOOK:
        ADDRESS_BOOK[data[0].title()] = data[1]
    return f'Contact {data[0].title()} was changed. The new phone number is {data[1]}.'


@input_error
def phone_handler(data):
    return f'Contact {data[0].title()} has number {ADDRESS_BOOK.get(data[0].title())}.'


@input_error
def show_handler(data):
    base = []
    count = 0
    for i in ADDRESS_BOOK.keys():
        count += 1
        log = f'Contact {i} has phone number {ADDRESS_BOOK[i]}'
        base.append(log)

    for el in base:
        print(el)
    return f'Total amount {count} contacts'


@input_error
def exit_handler(data):
    return 'Good buy!'

@input_error
def command_parser(raw_str):
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key, elements[1:]
    return 'Unknown command'


COMMANDS = {
    hello_handler: ['hello'],
    add_handler: ['add'],
    change_handler: ['change'],
    phone_handler: ['phone'],
    show_handler: ['show'],
    exit_handler: ['exit', 'good bye', 'close']
}


def main():
    while True:
        user_input = input('>>> ')

        if not user_input:
            continue

        func, data = command_parser(user_input)
        result = func(data)
        print(result)

        if result == 'Good buy!':
            break



if __name__ == '__main__':
    main()