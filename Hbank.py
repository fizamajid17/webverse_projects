 balance = 0  83848


def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)


def withdraw(amount):
    global balance
    if amount > balance:
        print("Not enough money!")
    else:
        balance -= amount
        print("Withdrew:", amount)


def check_balance():
    print("Current balance:", balance)


def main():
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)

        elif choice == "3":
            check_balance()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
            

main()
