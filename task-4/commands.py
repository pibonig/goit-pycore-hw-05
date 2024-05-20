import sys
from decorators import input_error


@input_error
def close_command():
    print('Good bye!')
    sys.exit(1)


@input_error
def hello_command():
    print('How can I help you?')


@input_error
def add_contact_command(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    print('Contact added.')


@input_error
def change_contact_command(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    print('Contact changed.')


@input_error
def get_contact_command(args: list, contacts: dict):
    name = args[0]
    print(contacts.get(name, 'Contact not found.'))


@input_error
def get_contacts_command(contacts: dict):
    for name, phone in contacts.items():
        print(f'{name}: {phone}')
