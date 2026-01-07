import json
import os
if not os.path.exists("accounts.json"):
    print("No accounts found.")
    exit()

while True:
    Acc_numb = input("Enter an account number: ").lower()
    if Acc_numb == "q":
        exit()
    elif  Acc_numb != int:
        print("That's not an integer.")
    pin = int(input("Enter your 4-digit pin: "))
    with open("accounts.json", "r")as file:
        log = json.load(file)