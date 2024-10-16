from colorama import Fore, init
init(autoreset=True)
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return("ПОМИЛКА:Введіть: <add> <ім'я> <номер телефону> ")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return("ПОМИЛКА:Введіть: <change> <ім'я> <новий номер телефону> ")
    name, new_phone = args
    if name not in contacts:
        return f"ПОМИЛКА: Контакт {name} не знайдено"
    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return("ПОМИЛКА:Введіть: <phone> <ім'я>")
    name = args[0]
    if name in contacts:
        return(f"Мобільний теелефон для {name}: {contacts[name]}")
    else:
        return(f"ПОМИЛКА: Контакт {name} не знайдено")
    

def show_all(args, contacts):
    if not contacts:
        return("Немає збережених контактів")
    resoult = ("Всі бережені контакти:\n")
    for name, phone in contacts.items():
        resoult += f"{name} {phone}\n"
    return resoult.strip()
 
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "chenge":
            print(change_contact(args, contacts))  
        elif command == "phone":
            print(show_phone(args, contacts))  
        elif command == "all":
            print(show_all(args, contacts))        
        else:
            print("Invalid command.")    
if __name__ == "__main__":
   main()            

