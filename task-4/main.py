import inspect

from commands import add_contact_command, close_command, change_contact_command, get_contacts_command, \
    get_contact_command, hello_command


def parse_input(user_input: str) -> tuple:
    command, *args = user_input.lower().split()
    return command, args


commands = {
    'close': close_command,
    'exit': close_command,
    'hello': hello_command,
    'add': add_contact_command,
    'change': change_contact_command,
    'phone': get_contact_command,
    'all': get_contacts_command,
}


def main():
    contacts = {}

    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        command, args = parse_input(user_input)

        if command in commands:
            unwrapped_function = inspect.unwrap(commands[command])
            sig = inspect.signature(unwrapped_function)
            if len(sig.parameters) == 0:
                commands[command]()
            elif len(sig.parameters) == 1:
                commands[command](contacts)
            elif len(sig.parameters) == 2:
                commands[command](args, contacts)
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
