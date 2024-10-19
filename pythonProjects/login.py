


def fivelines():
    print()
    print()
    print()
    print()
    print()







name           = ""
email          = ""
password       = ""
age            = ""
birthday       = ""
favoriteColor  = ""
favoriteFood   = ""

askName        = ""
askPass        = ""
logout         = ""

account        = input("Do you have an account (N/Y) ? ")

while True:

    if (account == "Y"  or logout == "Y") and name != "" and age != "" and birthday != "" and favoriteColor != "" and favoriteFood != "" and email != "":

        askEmail = input("Enter your email: ")
        askPass = input("Enter your password: ")
        print()
        print()

        if askEmail == email and askPass == password:

            while True:
                print("Account Information")
                print("===============================")
                print(f"Name: {name}")
                print(f"Age: {age} Years Old")
                print(f"Birthday: {birthday}")
                print(f"Favorite Color: {favoriteColor}")
                print(f"Favorite Food: {favoriteFood}")
                print(f"Email: {email}")
                print(f"Password: {password}")

                print()
                print()

                logout = input("Do you want to logout (Y/N)? ")

                if logout == "Y":

                    fivelines()

                    break

                edit = input("Do you wanna edit your info (Y/N)?")

                if edit == "Y":

                    edit2 = input(
                        "What part do you want to edit? {Name, Age, Favorite Color, Favorite Food, Birthday, Password, Email}: ")
                    print()

                    if edit2 == "Name":

                        name = input("Enter your new name: ")
                        print()
                        print()


                    elif edit2 == "Age":
                        age = int(input("Enter your new age: "))
                        print()
                        print()

                    elif edit2 == "Favorite Color":
                        favoriteColor = input("Enter your new favorite color: ")
                        print()
                        print()


                    elif edit2 == "Favorite Food":
                        favoriteFood = input("Enter your new favorite Food: ")
                        print()
                        print()

                    elif edit2 == "Birthday":
                        birthday = input("Enter your new birthday: ")
                        print()
                        print()

                    elif edit2 == "Password":
                        password = input("Enter your new password: ")
                        print()
                        print()

                    elif edit2 == "Email":
                        email = input("Enter your new email: ")


                else:
                    continue


        else:
            print("Invalid username or password!")
            print("Please try again")
            print()

    else:

        fivelines()

        print("Sign Up")
        print("==================================")
        email    = input("Enter email: ")
        password = input("Enter password: ")

        fivelines()

        print("Enter Account Info")
        print("==================================")


        name             = input("Enter your name: ")
        age              = int(input("Enter your age: "))
        favoriteColor    = input("Enter your favorite color: ")
        favoriteFood     = input("Enter your favorite Food: ")
        birthday         = input("Enter your birthday: ")

        fivelines()

        fivelines()

        while True:

         print("Account Information")
         print("===============================")
         print(f"Name: {name}")
         print(f"Age: {age} Years Old")
         print(f"Birthday: {birthday}")
         print(f"Favorite Color: {favoriteColor}")
         print(f"Favorite Food: {favoriteFood}")
         print(f"Email: {email}")
         print(f"Password: {password}")

         fivelines()

         logout = input("Do you want to logout (Y/N)? ")

         if logout == "Y":
             fivelines()

             break

         edit = input("Do you wanna edit your info (Y/N)?")

         if edit == "Y":

            edit2 = input("What part do you want to edit? {Name, Age, Favorite Color, Favorite Food, Birthday, Password, Email}: ")
            print()

            if edit2 == "Name":

                name = input("Enter your new name: ")
                print()
                print()


            elif edit2 == "Age":
                age = int(input("Enter your new age: "))
                print()
                print()

            elif edit2 == "Favorite Color":
                favoriteColor = input("Enter your new favorite color: ")
                print()
                print()


            elif edit2 == "Favorite Food":
                favoriteFood = input("Enter your new favorite Food: ")
                print()
                print()

            elif edit2 == "Birthday":
                birthday = input("Enter your new birthday: ")
                print()
                print()

            elif edit2 == "Password":
                password = input("Enter your new password: ")
                print()
                print()

            elif edit2 == "Email":
                email = input("Enter your new email: ")
















