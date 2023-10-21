contacts = dict()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct user name"
        except IndexError:
            return "The entered value is outside the valid range"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts.keys():
        return "Name not found!"
    else:
        contacts[name] = phone
        return "Contact updated."

@input_error
def show_phone(arg, contacts):
    name = arg
    return contacts[name]


def show_all(contacts):
    return [f"name: {name}, phone: {phone}" for name, phone in contacts.items()]

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args[0], contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
             print("Invalid command.")



if __name__ == "__main__":
    main()
