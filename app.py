import json
import os


def withdraw(log):
    print("Do you want to take from your savings or checkings \n1. Checking \n2. Saving")
    option = input("> ")
    if option == "1":
        print("Enter an amount to withdraw")
        amount = input("> ")
        true_amount = float(amount)
        if true_amount <= 0:
            print("invalid amount")
        elif true_amount > 0:
            log["checkingBalance"] -= true_amount
            log["transactions"].append(f"Withdrawal from Checkings in amount of ${true_amount}")
            print(log["checkingBalance"])
            save_file(log)
    elif option == "2":
        print("Enter an amount to withdraw")
        amount = input("> ")
        true_amount = float(amount)
        if true_amount <= 0:
            print("invalid amount")
        elif true_amount > 0:
            log["savingsBalance"] -= true_amount
            log["transactions"].append(f"Withdrawal from Savings in amount of ${true_amount}")
            print(log["savingsBalance"])
            save_file(log)

def check_balance(log):
    print("Which balance would you like to see. \n1. Checkings \n2. Savings")
    option = input("-> ")
    if option == "1":
        print( print(log["checkingBalance"]))
        go_back = input("Want to head back (y/n): ").lower()
        if go_back == "y":
            main_menu(log)
    elif option == "2":
            print( print(log["savingsBalance"]))
            go_back = input("Want to head back (y/n): ").lower()
            if go_back == "y":
                main_menu(log)
    

def view_transaction(log):
    print(log["transactions"])


def deposit(log):
    print("Do you want to add to your savings or checkings \n1. Checking \n2. Saving")
    option = input("> ")
    if option == "1":
        print("Enter an amount to deposit")
        amount = input("> ")
        true_amount = float(amount)
        if true_amount <= 0:
            print("invalid amount")
        elif true_amount > 0:
            log["checkingBalance"] += true_amount
            log["transactions"].append(f"Deposited ${true_amount} into Checking")
            print(log["checkingBalance"])
            save_file(log)
    elif option == "2":
        print("Enter an amount to deposit")
        amount = input("> ")
        true_amount = float(amount)
        if true_amount <= 0:
            print("invalid amount")
        elif true_amount > 0:
            log["savingsBalance"] += true_amount
            log["transactions"].append(f"Deposited ${true_amount} into Savings")
            print(log["savingsBalance"])
            save_file(log)





def main_menu(log):
    print("What would you like to do.\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Veiw transactions\n5. Quit")
    choice = input("")
    if choice ==  "1":
        deposit(log)
    if choice == "2":
        withdraw(log)
    if choice == "3":
        check_balance(log)
    if choice == "4":
        view_transaction(log)
    if choice == "5":
        exit()
    
def save_file(data, filename = "accounts.json"):
    with open(filename,"w") as file:
        file.write(json.dumps(data, indent=4))



def main():
    go = True
    if not os.path.exists("accounts.json"):
        print("No accounts found.")
        exit()


    while go == True:
        Acc_numb = input("Enter an account number: ").lower()
        if Acc_numb == "q":
            go = False
            break
        Pin_numb = input("Enter your 4-digit pin: ").lower()
        with open("accounts.json", "r")as file:

            log = json.load(file)
            #log["firstName"] = "Jason"
            #save_file(log)
        if Acc_numb != log["accountNumber"]:
            print("Your account number does not match.")
        if Pin_numb != log["pin"]:
            print("Your pin number does not match.")
        elif Acc_numb == log["accountNumber"] and Pin_numb == log["pin"]:
            print(f"Welcome {log["firstName"]} {log["lastName"]}")
            main_menu(log)
            break






if __name__ ==  "__main__":
    main()