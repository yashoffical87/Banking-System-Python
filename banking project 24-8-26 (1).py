print("Welcome To Yashpython Bank")
print("*** 1 Deposit, 2 Withdraw, 3 Balance Check, 4 Exit ***")

balance = 23000
choice = int(input("Enter your choice: "))

if choice == 1:
    deposit = float(input("Enter the amount to be deposited: "))
    if deposit > 0:
        balance += deposit
        print("Rs", deposit, "has been deposited successfully. Now Balance is Rs", balance)
    else:
        print("Invalid amount")

elif choice == 2:
    withdraw = float(input("Enter the amount to be withdrawn: "))
    if withdraw > 0:
        if withdraw <= balance:
            balance -= withdraw
            print("Rs", withdraw, "has been withdrawn successfully. Now Balance is Rs", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid amount")

elif choice == 3:
    print("Your balance is Rs", balance)

elif choice == 4:
    print("Thank you for banking with us")

else:
    print("Invalid choice")

import tkinter as tk
from tkinter import messagebox

balance = 23000

def deposit():
    global balance
    amount = float(entry.get())
    if amount > 0:
        balance += amount
        messagebox.showinfo("Deposit", f"Rs {amount} deposited successfully.\nBalance: Rs {balance}")
    else:
        messagebox.showerror("Error", "Invalid amount")

def withdraw():
    global balance
    amount = float(entry.get())
    if amount > 0:
        if amount <= balance:
            balance -= amount
            messagebox.showinfo("Withdraw", f"Rs {amount} withdrawn successfully.\nBalance: Rs {balance}")
        else:
            messagebox.showerror("Error", "Insufficient balance")
    else:
        messagebox.showerror("Error", "Invalid amount")

def check_balance():
    messagebox.showinfo("Balance", f"Your balance is Rs {balance}")

root = tk.Tk()
root.title("Yashpython Bank")

label = tk.Label(root, text="Enter Amount:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_deposit = tk.Button(root, text="Deposit", command=deposit)
btn_deposit.pack(pady=5)

btn_withdraw = tk.Button(root, text="Withdraw", command=withdraw)
btn_withdraw.pack(pady=5)

btn_balance = tk.Button(root, text="Balance Check", command=check_balance)
btn_balance.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=5)

root.mainloop()
