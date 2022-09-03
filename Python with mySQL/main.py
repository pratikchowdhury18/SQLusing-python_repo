from dbhelper import DBHelper

def main():
    db= DBHelper()
    while True:
        print("************WELCOME**********")
        print()
        print("Press 1 to insert user")
        print("Press 2 to display all users")
        print("Press 3 to display one user")
        print("Press 4 to delete user")
        print("Press 5 to update user")
        print("Press 6 to exit program")
        print()
        try:
            choice=int(input())
            if choice==1:
                #insert user
                uid=int(input("Enter new userid: "))
                username=input("Enter new username: ")
                phone=input("Enter new phone no.: ")
                db.insert_user(uid,username,phone)

            elif choice==2:
                #display all the users
                db.fetch_all()
                print()

            elif choice==3:
                #display specific user
                uid=int(input("Enter the userid to be displayed: "))
                db.fetch_one(uid)
                print()

            elif choice==4:
                #delete user
                uid=int(input("Enter the userid to be deleted: "))
                db.delete_user(uid)


            elif choice==5:
                #update user
                uid=int(input("Enter userid to be updated: "))
                username=input("Enter new username: ")
                phone=input("Enter new phone number: ")
                db.update_user(uid,username,phone)

            elif choice==6:
                #exit program
                print("Program exitted successfully :)")
                break
            else:
                print("Invalid input! Try again")
        except Exception as e:
            print(e)
            print("Invalid details... try again")

if __name__== "__main__":
    main()
