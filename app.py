import json
import os


def main_menu(log):
    print("What would you like to do.\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Veiw transactions")
    choice = input("")
    
def save_file(data, filename = "accounts.json"):
    with open(filename,"w") as file:
        file.write(json.dumps(data, indent=4))



def main():
    if not os.path.exists("accounts.json"):
        print("No accounts found.")
        exit()

    while True:
        try:
            Acc_numb = input("Enter an account number: ").lower()
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


        except:
            if Acc_numb == "q":
                exit()
            elif  Acc_numb != int:
                print("That's not an integer.")




if __name__ ==  "__main__":
    main()