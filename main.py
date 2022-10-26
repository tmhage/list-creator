if __name__ == '__main__':
    print('''
        Use the following commands to construct the array: 
        !!!  Type the commands without brackets, seperating the arguments with spaces
                eg. "insert 3 5" == insert(3, 5)
          -  append(obj)
          -  insert(idx, obj)
          -  pop()
          -  remove(obj)
        Type the 'print' command to print the current array.
        Type 'exit' to quit.
    ''')
    elements = []
    while True:
        # Seperate args as list from the whole command
        command, *args = input("Type your command: ").split()
        # Turn first argument into int for insert(int, obj) if multiple args
        if len(args) > 1:
            args[0] = int(args[0])
        if command == 'exit':
            print(elements)
            break
        if command == 'print':
            print(elements)
        # Check to see if command is available for the list element
        elif not hasattr(elements, command):
            print("%s is not a valid command" % command)
            # TODO only be able to use specified commands.
        else:
            try:
                getattr(elements, command)(*args)
            except TypeError:
                print("You did not use the right arguments.")
                # TODO tell user the correct arguments


