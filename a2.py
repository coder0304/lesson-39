import tkinter as tk
from tkinter import messagebox
import math

def calculate_interest():
    try:
       
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        
      
        if principal <= 0 or rate <= 0 or time <= 0:
            messagebox.showerror("Error", "All values must be positive numbers")
            return
        
        
        simple_interest = (principal * rate * time) / 100
        
        
        compound_interest = principal * (math.pow((1 + rate / 100), time)) - principal
        
        
        simple_result.config(text=f"Simple Interest: ${simple_interest:.2f}")
        compound_result.config(text=f"Compound Interest: ${compound_interest:.2f}")
        total_simple.config(text=f"Total Amount (Simple): ${principal + simple_interest:.2f}")
        total_compound.config(text=f"Total Amount (Compound): ${principal + compound_interest:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")
root.resizable(False, False)


input_frame = tk.LabelFrame(root, text="Enter Details", padx=10, pady=10)
input_frame.pack(pady=10)


tk.Label(input_frame, text="Principal Amount ($):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
principal_entry = tk.Entry(input_frame)
principal_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(input_frame, text="Interest Rate (%):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
rate_entry = tk.Entry(input_frame)
rate_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Label(input_frame, text="Time Period (years):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
time_entry = tk.Entry(input_frame)
time_entry.grid(row=2, column=1, padx=5, pady=5)


calculate_btn = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_btn.pack(pady=10)


result_frame = tk.LabelFrame(root, text="Results", padx=10, pady=10)
result_frame.pack(pady=10)


simple_result = tk.Label(result_frame, text="Simple Interest: $0.00")
simple_result.pack(anchor="w")

compound_result = tk.Label(result_frame, text="Compound Interest: $0.00")
compound_result.pack(anchor="w")

total_simple = tk.Label(result_frame, text="Total Amount (Simple): $0.00")
total_simple.pack(anchor="w")

total_compound = tk.Label(result_frame, text="Total Amount (Compound): $0.00")
total_compound.pack(anchor="w")


root.mainloop()