
# Importing the Modules to be Used :-

import os
import pickle


# Adding an Account to the bank :-

def main_add() :
    f = open("bank.dat" , "ab")
    accountnumber = int(input("Enter Account Number : "))
    name = input("Enter Account Holder's Name : ")
    DOB = input("Enter the Account Holder's Date of Birth : ")
    aadharnumber = int(input("Enter Account Holder's Aadhar Number : "))
    phone_number = int(input("Enter Account Holder's Phone Number : "))
    balance = int(input("Enter the Bank Balance : "))
    rec = [accountnumber , name , DOB , aadharnumber , phone_number , balance]

    pickle.dump(rec , f)
    f.close()



# Displaying the Account Details of all Users of the bank :-

import os
import pickle
def main_disp():
    f = open("bank.dat" , "rb")
    try :
        while True :
            rec = pickle.load(f)
            print(rec[0] , rec[1] , rec[2] , rec[3] , rec[4] , rec[5])

    except EOFError :
        f.close()

    

# Seaching the Details in bank :-

def main_search() :
    print("\n \t \t \t \t \t ☆ SEARCH ☆ ")
    print("\t \t \t \t ------------------------- ")
    print("\t \t 1. Search for Account details if you have Account Number ")
    print("\t \t 2. Search for Account details if you have Account Holder's Name ")
    print("\t \t 3. Search for Account details if you have Account Holder's Aadhar Number ")
    print("\t \t 4. EXIT (If you don't want any Data) ")

    c = int(input("Enter your choice : "))

# By Account Number :
    if c == 1 :
        fl = 0
        m = int(input("Enter the Account Holder's Account Number : "))
        def search() :
            f = open("bank.dat" , "rb")
            try :
                while True :
                    rec = pickle.load(f)
                    if rec[0] == m :
                        print(rec[0] , rec[1] , rec[2] , rec[3] , rec[4] , rec[5])
                        fl = 1

            except EOFError :
                f.close()

            if fl == 0 :
                print("Data does not Exist or invalid input !")

        search()
            
# By Name :
    elif c == 2 :
        fl = 0
        m = input("Enter the Account Holder's Name : ")
        def search() :
            f = open("bank.dat" , "rb")
            try :
                while True :
                    rec = pickle.load(f)
                    if rec[1] == m :
                        print(rec[0] , rec[1] , rec[2] , rec[3] , rec[4] , rec[5])
                        fl = 1

            except EOFError :
                f.close()

            if fl == 0 :
                print("Data does not Exist or invalid input !")

        search()

# By Aadhar Number :
    elif c == 3 :
        fl = 0
        m = int(input("Enter the Account Holder's Aadhar Number : "))
        def search() :
            f = open("bank.dat" , "rb")
            try :
                while True :
                    rec = pickle.load(f)
                    if rec[3] == m :
                        print(rec[0] , rec[1] , rec[2] , rec[3] , rec[4] , rec[5])
                        fl = 1

            except EOFError :
                f.close()

            if fl == 0 :
                print("Data does not Exist or invalid input !")

        search()

# Exiting :
    elif c == 4 :
        exit()

    else :
        print("Wrong input !! ")
        


# Updating the Details in bank :-

def main_modify() :
    print("\n \t \t \t \t \t ☆ UPDATE ☆ ")
    print("\t \t \t \t ------------------------- ")
    print("\t \t 1. Modify the Phone Number ")
    print("\t \t 2. Modify the balance if money is Credited ")
    print("\t \t 3. Modify the balance if money is Debited ")
    print("\t \t 4. EXIT (If you don't want any Data) ")

    n = int(input("Enter your choice : "))


# Updating Phone Number :
    if n == 1 :
        print("\n \t \t \t \t \t ○ PHONE NO. ○ ")
        print("\t \t \t \t ------------------------- ")
        print("\t \t 1. Modify if you have Account Number ")
        print("\t \t 2. Modify if you have Name ")
        print("\t \t 3. Modify if you have Aadhar Number ")
        print("\t \t 4. EXIT (If you don't need to Update) ")

        d = int(input("Enter your choice : "))

# Update Using Account No. :
        if d == 1 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = int(input("Enter the account number of the user whose phone number is to be updated : "))
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[0] == r :
                            rec[4] = int(input("Enter the New Phone Number : "))

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Phone Number Updated !!")

            modify()

# Update using Name :
        elif d == 2 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = input("Enter the Name of the user whose phone number is to be updated : ")
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[1] == r :
                            rec[4] = int(input("Enter the New Phone Number : "))

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Phone Number Updated !!")

            modify()

# Update using Aadhar No. :
        elif d == 3 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = int(input("Enter the Aadhar Number of the user whose phone number is to be updated : "))
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[3] == r :
                            rec[4] = int(input("Enter the New Phone Number : "))

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Phone Number Updated !!")

            modify()

# Exiting :
        elif c == 4 :
            exit()

        else :
            print("Wrong input !! ")


# Updating Amount Credited :        
    elif n == 2 :
        print("\n \t \t \t \t \t ○ CREDIT ○ ")
        print("\t \t \t \t ------------------------- ")
        print("\t \t 1. Modify if you have Account Number ")
        print("\t \t 2. Modify if you have Name ")
        print("\t \t 3. Modify if you have Aadhar Number ")
        print("\t \t 4. EXIT (If you don't need to Update) ")

        d = int(input("Enter your choice : "))

# Update using Account No. :
        if d == 1 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = int(input("Enter the account number of the user whose amount is to be updated (Credit) : "))
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[0] == r :
                            cre = int(input("Enter the amount Credited : "))
                            rec[5] = rec[5] + cre

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Amount Updated !!")

            modify()

# Update using Name :    
        elif d == 2 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = input("Enter the Name of the user whose amount is to be updated (Credit) : ")
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[1] == r :
                            cre = int(input("Enter the amount Credited : "))
                            rec[5] = rec[5] + cre

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Amount Updated !!")

            modify()

# Update using Aadhar No. :
        elif d == 3 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = int(input("Enter the Aadhar Number of the user whose amount is to be updated (Credit) : "))
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[3] == r :
                            cre = int(input("Enter the amount Credited : "))
                            rec[5] = rec[5] + cre

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Amount Updated !!")

            modify()

# Exiting :
        elif d == 4 :
            exit()

        else :
            print("Wrong input !! ")


# Updating Amount Debited :
    if n == 3 :
        print("\n \t \t \t \t \t ○ DEBIT ○ ")
        print("\t \t \t \t ------------------------- ")
        print("\t \t 1. Modify if you have Account Number ")
        print("\t \t 2. Modify if you have Name ")
        print("\t \t 3. Modify if you have Aadhar Number ")
        print("\t \t 4. EXIT (If you don't need to Update) ")

        d = int(input("Enter your choice : "))

# Update using Account No. :
        if d == 1 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = int(input("Enter the account number of the user whose amount is to be updated (Debit) : "))
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[0] == r :
                            deb = int(input("Enter the amount Debited : "))
                            rec[5] = rec[5] - deb

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Amount Updated !!")

            modify()

# Update using Name :
        elif d == 2 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = input("Enter the Name of the user whose amount is to be updated (Debit) : ")
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[1] == r :
                            deb = int(input("Enter the amount Debited : "))
                            rec[5] = rec[5] - deb

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Amount Updated !!")

            modify()

# Update using Aadhar No. :
        elif d == 3 :
            def modify() :
                fl = 0
                f1 = open("bank.dat" , "rb")
                f2 = open("temp.dat" , "wb")
                r = int(input("Enter the Aadhar Number of the user whose amount is to be updated (Debit) : "))
                try :
                    while True :
                        rec = pickle.load(f1)
                        if rec[3] == r :
                            deb = int(input("Enter the amount Debited : "))
                            rec[5] = rec[5] - deb

                            fl = 1
                        pickle.dump(rec ,f2)
                except EOFError :
                    f1.close()
                    f2.close()

                os.remove("bank.dat")
                os.rename("temp.dat" , "bank.dat")

                if fl == 0 :
                    print("Record not found !!")

                else :
                    print("Amount Updated !!")

            modify()

# Exiting :
        elif d == 4 :
            exit()

        else :
            print("Wrong input !! ")
                


# Deleting the Details in bank :-

def main_delete() :
    print("\n \t \t \t \t \t ☆ DELETE ☆ ")
    print("\t \t \t \t ------------------------- ")
    print("\t \t 1. Delete the Account Details if you have Account Number ")
    print("\t \t 2. Delete the Account Details if you have Account Holder's Name ")
    print("\t \t 3. Delete the Account Details details if you have Account Holder's Aadhar Number ")
    print("\t \t 4. EXIT (If you don't have to Delete) ")

    e = int(input("Enter your choice : "))

# Deleting using Account No. :
    if e == 1 :
        def delete() :
            fl =0
            f1 = open("bank.dat" , "rb")
            f2 = open("temp.dat" , "wb")
            s = int(input("Enter the Account Number of User whose data is to be Deleted : "))
            try :
                while True :
                    rec = pickle.load(f1)
                    if rec[0] != s :
                        pickle.dump(rec , f2)

                    else :
                        fl = 1

            except EOFError :
                f1.close()
                f2.close()

            os.remove("bank.dat")
            os.rename("temp.dat" , "bank.dat")

            if fl == 0 :
                print("Record not Found !!")

            else :
                print("Record Deleted !!")

        delete()
            
# Deleting using Name :
    elif e == 2 :
        def delete() :
            fl =0
            f1 = open("bank.dat" , "rb")
            f2 = open("temp.dat" , "wb")
            s = input("Enter the Name of User whose data is to be Deleted : ")
            try :
                while True :
                    rec = pickle.load(f1)
                    if rec[1] != s :
                        pickle.dump(rec , f2)

                    else :
                        fl = 1

            except EOFError :
                f1.close()
                f2.close()

            os.remove("bank.dat")
            os.rename("temp.dat" , "bank.dat")

            if fl == 0 :
                print("Record not Found !!")

            else :
                print("Record Deleted !!")

        delete()
    
# Deleting using Aadhar No. :-
    elif e == 3 :
        def delete() :
            fl =0
            f1 = open("bank.dat" , "rb")
            f2 = open("temp.dat" , "wb")
            s = int(input("Enter the Aadhar Number of User whose data is to be Deleted : "))
            try :
                while True :
                    rec = pickle.load(f1)
                    if rec[3] != s :
                        pickle.dump(rec , f2)

                    else :
                        fl = 1

            except EOFError :
                f1.close()
                f2.close()

            os.remove("bank.dat")
            os.rename("temp.dat" , "bank.dat")

            if fl == 0 :
                print("Record not Found !!")

            else :
                print("Record Deleted !!")

        delete()
            
# Exiting :
    elif e == 4 :
        exit()

    else :
        print("Wrong input !! ")
        


# Main Program to handle the Details :-

def main():
    while True :
        print("\n \t \t \t \t \t ☆ MENU ☆ ")
        print("\t \t \t \t ------------------------- ")
        print("\t \t 1. Add Account ")
        print("\t \t 2. Display Data of the Accounts ")
        print("\t \t 3. Search for Account Details ")
        print("\t \t 4. Update the Account Details ")
        print("\t \t 5. Delete Account Details ")
        print("\t \t 6. EXIT (If you don't want to do any changes) ")

        choice = int(input("Enter your Choice : "))

        if choice == 1 :
            main_add()

        elif choice == 2 :
            main_disp()

        elif choice == 3 :
            main_search()

        elif choice == 4 :
            main_modify()

        elif choice == 5 :
            main_delete()

        elif choice == 6 :
            exit()

        else :
            print("Wrong input !! ")

main()

