import bot_data_handler as data_file


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_string = f"\033[91mError in {func.__name__}:\x1b[0m {e}\n"
            if str(func.__name__) == "add_contact":
                error_string += "Wrong arguments count, pls use \033[96madd [username] [phone]\x1b[0m."
            elif str(func.__name__) == "change_contact":
                error_string += "Wrong arguments count, pls use \033[96mchange [username] [phone]\x1b[0m."
            elif str(func.__name__) == "show_phone":
                error_string += (
                    "Wrong arguments count, pls use \033[96mphone [username]\x1b[0m."
                )
            return error_string

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        while True:
            user_input = str(
                input(
                    f"Contact \033[96m{name}\x1b[0m already have \33[96m{contacts[name]}\x1b[0m number, it will be replaced\nAre you shure? \33[96mY/N\x1b[0m: "
                )
            )
            if user_input in ["Y", "y"]:
                return change_contact(args, contacts)
            elif user_input in ["N", "n"]:
                return "Contact not changed."
            else:
                print("Invalid command.")
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts.update({name: phone})
        return "Contact updated."
    else:
        print(f"Contact \033[96m{name}\x1b[0m does not exist, it will be created.")
        return add_contact(args, contacts)


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"\033[96m{name}'s\x1b[0m phone is: \033[96m{contacts[name]}\x1b[0m"
    else:
        return f"Contact \033[96m{name}\x1b[0m does not exist. Check your spelling."


def show_all(contacts: dict):
    phonebook = ""
    for name in contacts.keys():
        phonebook += f"{name}: {contacts[name]}\n"
    phonebook = phonebook.removesuffix("\n")
    if phonebook == "":
        return "Phonebook is empty."
    else:
        return phonebook


def show_help():
    help = (
        "\nAvailable commands:\n"
        "\033[96mhelp\x1b[0m, \033[96m?\x1b[0m - this help\n"
        "\033[96mclose\x1b[0m, \033[96mexit\x1b[0m, \033[96mquit\x1b[0m, \033[96mbye\x1b[0m - close application\n"
        "\033[96madd [username] [phone]\x1b[0m - adding contact to the phonebook\n"
        "\033[96mchange [username] [phone]\x1b[0m - changing contact in the phonebook\n"
        "\033[96mphone [username]\x1b[0m - show phone of the contact\n"
        "\033[96mall\x1b[0m - show all contacts in phonebook\n"
        "\033[96mhello\x1b[0m, \033[96mhi\x1b[0m - just a greeting"
    )
    return help


def main():
    print("\nWelcome to the assistant bot!")
    contacts = data_file.load_from_file()
    dirty = False
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                data_file.save_to_file(contacts)
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            dirty = True
            print(add_contact(args, contacts))
        elif command == "change":
            dirty = True
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["help", "?"]:
            print(show_help())
        else:
            print(
                "Invalid command. Use \033[96mhelp\x1b[0m or \033[96m?\x1b[0m to see all available commands."
            )


if __name__ == "__main__":
    main()
