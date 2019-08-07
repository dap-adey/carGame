
command_list = ["start", "stop", "help", "Help", "Start", "Stop", "STOP", "START", "HELP"]
command_input = ""
while command_input != "quit":
    # command_input = input(">  ")
    attempt = 1
    while attempt == 1:
        command_input = input(">  ")
        if command_input == "start" or command_input == "START" or command_input == "Start":
            # if command_input
            print("Car started ......Ready to GO!")
            attempt += 1
            continue
        elif command_input == "stop" or command_input == "STOP" or command_input == "Stop":
            print("Car stopped ......")
            attempt += 1
            continue
        elif command_input == "Help" or command_input == "HELP" or command_input == "help":
            print("Use the following Commands:")
            print("> start")
            print("> stop")
            print("> quit")
            attempt += 1
        elif command_input not in command_list:
            print("I don't understand what you mean!")
            attempt += 1
    else:
        command_input = input(">  ")
        if command_input == "start" or command_input == "START" or command_input == "Start":
            # if command_input
            print("Car Already started ......Ready to GO!")

            continue
        elif command_input == "stop" or command_input == "STOP" or command_input == "Stop":
            print("Car Already stopped ......")

            continue
        elif command_input == "Help" or command_input == "HELP" or command_input == "help":
            print("Use the following Commands:")
            print("> start")
            print("> stop")
            print("> quit")

        elif command_input not in command_list:
            print("I don't understand what you mean!")

    attempt += 1
