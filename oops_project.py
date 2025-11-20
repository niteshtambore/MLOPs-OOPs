import random

class ChatBox:
    def __init__(self):
        self.user_id = ""
        self.user_name = ""
        self.user_password = ""
        self.is_loggedin = False

    def menu(self):
        user_input = input(("""Welcome to ChatBox..!, How would you like to proceed :
                                 Press - 1 to SignUp
                                 Press - 2 to Login
                                 Press - 3 to Chat with a friend
                                 Press - 4 to Write a Post
                                 Press - 5 to Exit
                                 =>"""))
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.chat()
        elif user_input == "4":
            self.my_post()
        else:
            exit()

    def signup(self):
        self.user_id = random.randint(1,10)
        self.user_name = input("\nPlease enter user name : ")
        self.user_password = input("\nPlease enter password : ")
        print(self.user_name," you signed up successfully..")
        print("Your user id :", self.user_id)
        print("Your user name :", self.user_name)
        print("Your user password :", self.user_password)
        self.menu()

    def signin(self):
        if self.user_name=="" and self.user_password=="":
            print("Please signup first")
        else:
            u_name = input("Please enter you registered user name :")
            u_pass = input("Please enter you password :")
            if u_name == self.user_name and u_pass == self.user_password:
                self.is_loggedin = True
                print(u_name,", you logged in successfully")
                self.menu()
            else:
                print("Please input correct credentials..!")
        return self.menu()
    
    def my_post(self):
        if self.is_loggedin == True:
            post = input("What you want to post :")
            print("This is posted on you page : ", post)
        else:
            print("Please login first..!")
        return self.menu()
        
    def chat(self):
        if self.is_loggedin:
            chat = input("Enter your message :")
            frnd = input("Please enter your friend's name : ")
            print("Message ", chat, " sent to ", frnd)
        else:
            print("Please login first..!")
        return self.menu()

chat = ChatBox()