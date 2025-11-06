
CONTACTS: dict[str, str] = {}


def parse_input(user_input: str) -> tuple[str, list[str]]:

    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def hello() -> str:
    return "How can I help you?"

def add_contact(*args: str) -> str:
    if len(args) != 2:
        return "Usage: add <username> <phone>"
    name, phone = args
    if name in CONTACTS:
        return f"Contact '{name}' already exists. Use: change {name} <new_phone>"
    CONTACTS[name] = phone
    return "Contact added."

def change_contact(*args: str) -> str:
    if len(args) != 2:
        return "Usage: change <username> <phone>"
    name, phone = args
    if name not in CONTACTS:
        return f"No contact named '{name}'. Use: add {name} <phone>"
    CONTACTS[name] = phone
    return "Contact updated."

def show_phone(*args: str) -> str:
    if len(args) != 1:
        return "Usage: phone <username>"
    name = args[0]
    if name not in CONTACTS:
        return f"No contact named '{name}'."
    return CONTACTS[name]

def show_all() -> str:
    if not CONTACTS:
        return "No contacts yet."
    lines = [f"{name}: {phone}" for name, phone in sorted(CONTACTS.items())]
    return "\n".join(lines)

def goodbye() -> str:
    return "Good bye!"


def main() -> None:
    print("Welcome to the assistant bot! Type 'help' to see commands.")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print(goodbye())
            break
        elif command == "hello":
            print(hello())
        elif command == "add":
            print(add_contact(*args))
        elif command == "change":
            print(change_contact(*args))
        elif command == "phone":
            print(show_phone(*args))
        elif command == "all":
            print(show_all())
        elif command in ("help", "?"):
            print(
                "Commands:\n"
                "  hello                      → How can I help you?\n"
                "  add <username> <phone>     → add new contact\n"
                "  change <username> <phone>  → update existing contact\n"
                "  phone <username>           → show contact phone\n"
                "  all                        → list all contacts\n"
                "  close | exit               → quit"
            )
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
