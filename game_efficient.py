
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if not started:
            print("Car Started...Ready to go")
            started = True
        else:
            print("Car already started!...")

    elif command == "stop":
        if started:
            print("Car Stopped...")
            started = False
        else:
            print("Car already stopped!...")

    elif command == "help":
        print("""
start --- Starts the car
stop --- Stops the car
help --- Displays command options
quit --- Terminates program     
                """)
    elif command == "quit":
        break
    else:
        print("I don't understand....Type 'Help' for options")
