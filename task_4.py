#--------task4---------------

comands = {'hello':'hello (cmd)', 
           'add':'create a new contact', 
           'change':'change the contact', 
           'show':'show contacts phone ', 
           'all':'show all contacts', 
           'close': 'close aplication', 
           'exit':'exit'}


Contacts_path = r"source/contacts.txt"
old_dict = {}
contacts_dict = {}

def question(ask:str, args=(), error_answer=""):
    while True:
        answer=input(ask)
        if answer and not args or answer in args:
            break
        else: print(error_answer)
    return answer

def read_from_file(path:str,dic:dict):
    try:
        with open(path,"r+") as fr:
            for line in fr.readlines():
                contact=line.split()
                dic[contact[0]]=contact[1]
    except Exception as e:
        print(e)
        if save_to_file(path):
            print(f"File {path}\nCreated")
            # old_dict=contacts_dict.copy()
        else: return False
    return True

def save_to_file(path:str):
    try:
        with open(path,"w+") as wf:
            wf.writelines(k+" "+ v +"\n" for k,v in contacts_dict.items())
    except Exception as e:
            print(e)
            return False
    return True

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(contact_name:str, contact_phone:str) -> bool:
    if contact_name in contacts_dict:
        return "",""
    else:
        contact_name=contact_name.strip().title()
        contact_phone = contact_phone.strip()
        contacts_dict[contact_name]=contact_phone
        return contact_name, contact_phone

def change_contact(contact_name:str, contact_phone:str):
    if contact_name in contacts_dict and question(f"Change from {contacts_dict[contact_name]} to {contact_phone} Continue? Y/N: ",
                                                  ('Y','y','N','n'),"Enter Y or N").upper()=='Y':
        contacts_dict[contact_name]=contact_phone.strip()
        return contact_name, contact_phone
    else:
        return "",""

def show_phone(contact_name:str):
    if contact_name in contacts_dict:
        print(f"{contact_name} {"-"*(50-len(contact_name))}tel: {contacts_dict[contact_name]}")
        return True
    else:
        print("Record not founded!")
        return False

def show_all():
    for name, phone in contacts_dict.items():
        print(f"{name}{"-"*(50-len(name))}tel: {phone}")

def main():
    print("\nWelcome to the assistant bot!\n\n        COMMANDS:")
    for command in comands:
        print(f"{command} {"-"*(20-len(command))}{comands[command]}")
    activ = read_from_file(Contacts_path,contacts_dict)
    if activ: old_dict=contacts_dict.copy()
    
    while activ:
        command = question("Enter command:", tuple(comands.keys()),"Unknown command!")
        match command:            
            case "hello": print("\nHow can I help you?\n")
            
            case "add":
                name, phone = add_contact(contact_name=question(ask="Enter Name: "),
                               contact_phone=question(ask="Enter Phone: "))
                if name and phone:
                    print(f'Contact added: (Name: {name}-----tel: {phone})')
                else: print(f"Contact not added!")
            
            case "change":
                name, phone = change_contact(contact_name=question("Enter Name: ", 
                                                                   tuple(contacts_dict.keys()),
                                                                   "Name incorrect!"),
                                             contact_phone=question(ask="Change Phone: "))
                if phone:
                    print(f'Phone changed: {name}-----tel: {phone}')
                else: print(f"Contact not changed!")            
            
            case "show": 
                show_phone(contact_name=question("Enter Name: ", tuple(contacts_dict.keys()), "Contact Name not fouded!"))
            
            case "all": show_all()
            
            case "close":            
                if contacts_dict!=old_dict and question("Save to file? (save: Y/N: ",('Y','y','N','n'),"Enter Y or N").upper()=="Y":
                    if save_to_file(Contacts_path): old_dict=contacts_dict.copy()
                print("\nGood bye!\n")
                break
            
            case "exit":
                if contacts_dict!=old_dict and question("Save to file? (save: Y/N: ", ('Y','y','N','n'),"Enter Y or N").upper()=="Y":
                    if save_to_file(Contacts_path): old_dict=contacts_dict.copy()       
                print("\nGood bye!\n")
                break
            
            case _: print("Unknown command!\n")
       
if __name__ == "__main__":
    main()
