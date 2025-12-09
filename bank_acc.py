
amount = 0

def deposit():
        global amount
        deposit = float(input("Enter the amount to deposit: "))
        if deposit <= 0:
            print("Amount must be greater than 0.")
        else:
            amount += deposit
            print("Your",deposit,"has been deposited to your account.")


def withdraw():
        global amount
        withdraw = float(input("Enter the amount to withdraw: "))
        if withdraw > amount:
               print("Insufficient Balance.")
        elif withdraw <= 0:
               print("Amount must be more than 0.")
        else:
            amount -= withdraw
            print("Amount has been withdrawed successfully.")

def checkbalance():
        global amount
        print("your current balance is:",amount)


while True:
    print("\n-----------------MENU BAR-----------------")
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. CHECK BALANCE")
    print("4. EXIT")
    choice = input("Enter your choice: ")
    

    match choice:
           case "1" :
                  deposit()
           case "2":
                  withdraw()
           case "3":
                  checkbalance()
           case "4":
                  print("Exiting the program..")
                  break
           case _:
                  print("Invalid choice ")
            
        


        