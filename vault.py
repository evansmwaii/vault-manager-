                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
import json

master_pin="0000"


myvault= []


master_pin="0000"


myvault= []

def load_vault():
        global myvault
        try:
           with open("vault.json","r") as file:
             myvault= json.load(file)
        except FileNotFoundError:
          myvault= []

def save_vault():
      with open("vault.json","w") as file:
        json.dump(myvault,file)



def show_menu():
      print("\n welcome to the vault were your passwords are safe!!enter an option: ")
      print("1. view accounts ")
      print("2. add account")
      print("3. remove account")
      print("4. exit")
      print("5. reveal passwords")
      print("6.search account")

def view_accounts():
     if not myvault:
      print("no accounts available")
     else:
         for i,acc in enumerate(myvault,1):
           masked = "*" * len(acc['passwords'])
           print(f"{i}. {acc['site']} | {acc['username']} | {masked}")

def add_account():
     site= input("enter site name:  ")
     username= input("enter username: ")
     passwords= input("enter password: ")
     myvault.append({"site":site,"username":username,"passwords":passwords})
     save_vault()
     print(" account added!!")

def remove_account():
    view_accounts()
    try:
        index= int(input("enter account to delet: ")) - 1
        if 0 <= index < len(myvault):
             removed= myvault.pop(index)
             save_vault()
             print(f"Removed: {removed['site']}")
        else:
             print("invalid option")
    except valueError:
       print("enter number")

def reveal_password():
   pin=input("enter password: ")
   if pin !=master_pin:
        print("wrong pin,try again")
        return


def load_vault():
        global myvault
        try:
           with open("vault.json","r") as file:
             myvault= json.load(file)
        except FileNotFoundError:
          myvault= []

def save_vault():
      with open("vault.json","w") as file:
        json.dump(myvault,file)



def show_menu():
      print("\n welcome to the vault were your passwords are safe!!enter an option: ")
      print("1. view accounts ")
      print("2. add account")
      print("3. remove account")
      print("4. exit")
      print("5. reveal passwords")
      print("6.search account")

def view_accounts():
     if not myvault:
      print("no accounts available")
     else:
         for i,acc in enumerate(myvault,1):
           masked = "*" * len(acc['passwords'])
           print(f"{i}. {acc['site']} | {acc['username']} | {masked}")

def add_account():
     site= input("enter site name:  ")
     username= input("enter username: ")
     passwords= input("enter password: ")
     myvault.append({"site":site,"username":username,"passwords":passwords})
     save_vault()
     print(" account added!!")

def remove_account():
    view_accounts()
    try:
        index= int(input("enter account to delet: ")) - 1
        if 0 <= index < len(myvault):
             removed= myvault.pop(index)
             save_vault()
             print(f"Removed: {removed['site']}")
        else:
             print("invalid option")
    except valueError:
       print("enter number")

def reveal_password():
   pin=input("enter password: ")  
   if pin !=master_pin:
        print("wrong pin,try again")
        return  

   view_accounts()
   try:
      index= int(input("which password do you want to see? ")) - 1
      if 0 <= index < len(myvault):
         account= myvault[index]
         print(f"\n {account['site']} | {account['username']} | {account['passwords']}")
      else:
         print("invalid option")

   except ValueError:
         print("enter a number")


def search_account():
     pin=input("enter password: ")
     if pin!= master_pin:
        print("invalid password")
        return

     search_term= input ("enter site to search: ").lower()
     found= False

     for account in myvault:
       if account['site'].lower()== search_term:
          print("found")
          print(f"\n{account['site']} | {account['username']} | {account['passwords']}")
          found= True 
          break

       if not found:
          print("not found")

load_vault()

while True:
    show_menu()
    choice=input("pick a number: ")

    if choice=="1":
        view_accounts()
    elif choice== "2":
         add_account()
    elif choice== "3":
         remove_account()
    elif choice== "4":
        print("Adios muchacho!!")
        break
    elif choice== "5":
         reveal_password()
    elif choice == "6":
         search_account() 
    else:
        print("invalid choice")

