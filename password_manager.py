main_password = ("dbk")
main_password_input = input("Enter the main password: ")
if main_password_input == main_password:
    while True:
        def add_password():
            username = input("Enter username: ")
            password = input("Enter Password: ")
            with open('password_manager_data.txt', 'a') as f:
                f.write("Username: " + username + " | " + "Password: " + password + '\n')
            print("Password successfully added")
        def view_password():
            with open("password_manager_data.txt", 'r') as f:
                for lines in f.readlines():
                    data = lines.rstrip()
                    username_1, pwd_1 = data.split(" | ")
                    print(username_1 , pwd_1)
            
        pick = input("""Do you want to view the password or add a password (view/add)?
or do you want to quit (quit)? """).lower()
        if pick == "view":
            view_password()
        elif pick == "add":
            add_password()
        if pick == "quit":
            print("Thanks for using the password manager!")
            break
else:
    print("Invalid")
                        

        

