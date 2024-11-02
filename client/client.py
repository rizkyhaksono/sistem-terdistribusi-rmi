import Pyro4

def create_file(server, command):
    if len(command) == 2:
        filename = command[1]
        print(server.create_file(filename))
    else:
        print("Invalid arguments for create_file")

def rename_file(server, command):
    if len(command) == 3:
        old_name = command[1]
        new_name = command[2]
        print(server.rename_file(old_name, new_name))
    else:
        print("Invalid arguments for rename_file")

def delete_file(server, command):
    if len(command) == 2:
        filename = command[1]
        print(server.delete_file(filename))
    else:
        print("Invalid arguments for delete_file")

def create_directory(server, command):
    if len(command) == 2:
        dirname = command[1]
        print(server.create_directory(dirname))
    else:
        print("Invalid arguments for create_directory")

def rename_directory(server, command):
    if len(command) == 3:
        old_name = command[1]
        new_name = command[2]
        print(server.rename_directory(old_name, new_name))
    else:
        print("Invalid arguments for rename_directory")

def delete_directory(server, command):
    if len(command) == 2:
        dirname = command[1]
        print(server.delete_directory(dirname))
    else:
        print("Invalid arguments for delete_directory")

def list_directory(server, command):
    path = command[1] if len(command) == 2 else "."
    contents = server.list_directory(path)
    if isinstance(contents, list):
        print("Directory contents:", contents)
    else:
        print("Error:", contents)

def main():
    server = Pyro4.Proxy("PYRONAME:rmi.s3")
    
    print("Available Commands:")
    print("1. create_file <filename>")
    print("2. rename_file <old_name> <new_name>")
    print("3. delete_file <filename>")
    print("4. create_directory <dirname>")
    print("5. rename_directory <old_name> <new_name>")
    print("6. delete_directory <dirname>")
    print("7. list_directory <path>")
    
    command_handlers = {
        "create_file": create_file,
        "rename_file": rename_file,
        "delete_file": delete_file,
        "create_directory": create_directory,
        "rename_directory": rename_directory,
        "delete_directory": delete_directory,
        "list_directory": list_directory
    }
    
    while True:
        command = input("\nEnter command: ").strip().split()
        
        if not command:
            continue
        
        operation = command[0]
        
        try:
            if operation in command_handlers:
                command_handlers[operation](server, command)
            else:
                print("Invalid command or arguments.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
