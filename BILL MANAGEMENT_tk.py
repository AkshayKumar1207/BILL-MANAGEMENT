import tkinter as tk
from tkinter import messagebox

# Item prices
PRICES = {
    "Dosa": 60,
    "Cookies": 30,
    "Tea": 7,
    "Coffee": 100,
    "Juice": 20,
    "Pancakes": 15,
    "Eggs": 7
}

# Main window
root = tk.Tk()
root.title("Bill Management")
root.geometry("500x400")
root.configure(bg="#fcfc2f")
root.resizable(False, False)

# Heading
tk.Label(root, text="BILL MANAGEMENT", font=("Arial", 18, "bold"), bg="#dff0d8").pack(pady=10)

# Frames
menu_frame = tk.Frame(root, bg="#d0e9c6")
menu_frame.place(x=10, y=60, width=200, height=230)

entry_frame = tk.Frame(root, bg="#f2dede")
entry_frame.place(x=220, y=60, width=120, height=230)

bill_frame = tk.Frame(root, bg="#fcf8e3")
bill_frame.place(x=350, y=60, width=130, height=230)

# Menu
tk.Label(menu_frame, text="Menu", font=("Arial", 14, "bold"), bg="#d0e9c6").pack()
for item, price in PRICES.items():
    tk.Label(menu_frame, text=f"{item} - Rs.{price}", font=("Arial", 10), bg="#d0e9c6").pack(anchor="w", padx=10)

# Entry Labels and Fields
entries = {}
for i, item in enumerate(PRICES.keys()):
    tk.Label(entry_frame, text=item, font=("Arial", 10), bg="#f2dede").place(x=10, y=i*30)
    entry = tk.Entry(entry_frame, width=5)
    entry.place(x=60, y=i*30)
    entries[item] = entry

# Total calculation function
def calculate_total():
    try:
        total = 0
        for item in PRICES:
            qty = entries[item].get()
            qty = int(qty) if qty else 0
            total += qty * PRICES[item]
        total_var.set(f"Rs. {total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers only.")

# Reset function
def reset_fields():
    for entry in entries.values():
        entry.delete(0, tk.END)
    total_var.set("Rs. 0.00")

# Total and Reset Buttons
tk.Button(root, text="Total", command=calculate_total, bg="lightblue").place(x=220, y=310)
tk.Button(root, text="Reset", command=reset_fields, bg="lightgray").place(x=290, y=310)

# Total Display
tk.Label(bill_frame, text="Bill", font=("Arial", 12, "bold"), bg="#fcf8e3").pack(pady=5)
tk.Label(bill_frame, text="Total", font=("Arial", 10, "bold"), bg="#fcf8e3").pack()
total_var = tk.StringVar(value="Rs. 0.00")
tk.Label(bill_frame, textvariable=total_var, font=("Arial", 14, "bold"), fg="green", bg="#fcf8e3").pack(pady=10)

root.mainloop()