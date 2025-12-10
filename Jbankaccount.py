

balance = 0 

def deposit(amount):
    global balance 
    balance += amount
    print(amount, "added to your account .")

def withdraw(amount):
    global balance 
    if amount > balance :
        print("not enough balance, cannot withdraw.")
    else :
        balance -= amount 
        print(amount , "withdraw from your account.")

def check_balance():
    print("your balance is :" , balance)
def main():
    while True:
        print("\n 1.deposit")
        print(" 2.withdraw")
        print("3. check balance")
        print("4.exit")

        choice = input("choose 1-4 : ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            deposit(amt)

        elif choice == "2":
            amt = float(input("Enter withdraw amount: "))
            withdraw(amt)

        elif choice == "3":
            check_balance()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

main()