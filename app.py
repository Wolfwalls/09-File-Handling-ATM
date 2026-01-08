import json
import os


def deposit(log):
    print("Do you want to add to your savings or checkings \n1. Checking \n2. Saving")
    option = input()
    if option == "1":
        print("Enter an amout to deposit")
        amount = input()
        true_amount = float(amount)
        if true_amount <= 0:
            print("invalid amount")
        elif true_amount > 0:
            log["checkingBalance"] += true_amount
            print(log["checkingBalance"])
            save_file(log)
    elif option == "2":
        print("Enter an amout to deposit")
        amount = input()
        true_amount = float(amount)
        if true_amount <= 0:
            print("invalid amount")
        elif true_amount > 0:
            log["savingsBalance"] += true_amount
            print(log["savingsBalance"])
            save_file(log)

        



def main_menu(log):
    print("What would you like to do.\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Veiw transactions")
    choice = input("")
    if choice ==  "1":
        deposit(log)
    
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