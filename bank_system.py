# --- Bank Account Mini System ---

balance = 0   # balance starts at 0

def deposit(amount):
    global balance
    balance += amount
    print(f"₹{amount} deposited.")

def withdraw(amount):
    global balance
    if amount > balance:
        print("❗ Not enough balance!")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn.")

def check_balance():
    print(f"Your current balance: ₹{balance}")

# ----- Main loop -----
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you! Exiting system.")
        break

    else:
        print("Invalid choice, try again.")


