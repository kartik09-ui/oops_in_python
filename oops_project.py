class chatbook:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input('''welcom to chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to messege a friend
                           5. Press any other key to exit \n''') 
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_messege()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here -->")
        password = input("setup your passwod here -->")
        self.username = email
        self.password = password
        print("You have signed up successfully!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password =='':
            print('Please signup first by pressing 1 in the menu')
        else:
            username = input('enter your email/username here -->')
            password = input("enter your password here -->")
            if self.username == username and self.password == password:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please input correct credentials...")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your messege here -->")
            print(f"Following content is posted {txt}")
        else:
            print("you need to signin first to post something...")
        print("\n")
        self.menu()

    def send_messege(self):
        if self.loggedin == True:
            txt = input("Enter you messege here -->")
            frnd = input("Whom to send a messege? -->")
            print(f"Your messege has been send to {frnd}")
        else:
            print("You need to signun first...")
        print("\n")
        self.menu()

obj = chatbook()

