import random
from users import users


def __main__():
    while True:
        print("Enter your credential to signup or login to your accounts:'login' 'signup' 'exit' ")
        print('\n')
        my_code = input().lower()
        print('\n')

        if my_code == 'signup':
            print("create usernane")
            created_users_name = input()

            print("create password")
            created_users_password = input()
            print("you account has been successfully created")


            print("login")
            print("Enter username")
            entered_username = input()

            print("please enter you password")
            entered_password = input()



            while entered_username != created_users_name or  entered_password != created_users_password:
                print('\n')
                print("invalid Username or password")

                print("Enter correct username")
                
                entered_username = input()
                print('\n')
                print("Enter correct password")
                entered_password = input()
              

            else:
                print(f"Hello {entered_username} you have login to your new account succesfully")
            
        elif my_code == 'login':
            print("Enter your username")
            print('\n')

            default_user = input()

            print("Please Enter your password")
            print('\n')

            default_password = input()

            while default_user != "David" and default_password != "1234":
                print("invalid password or username")
                print("Enter your username")


                default_user = input()

                print("enter your password")

                default_password = input()

            else:
                print(f"Hello {default_user}. welcome back") 

                break   
            


        elif my_code == 'exit':
            print("Thank you ")
            break

if __name__ == "__main__":
    __main__()