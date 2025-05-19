### ✅ `gui_version.py` — GUI Using Tkinter

import tkinter as tk
from tkinter import messagebox
from main import calculate_probabilities

def compute():
    try:
        prevalence = float(entry_prevalence.get())
        sensitivity = float(entry_sensitivity.get())
        specificity = float(entry_specificity.get())

        if not (0 <= prevalence <= 1 and 0 <= sensitivity <= 1 and 0 <= specificity <= 1):
            raise ValueError

        pos, neg = calculate_probabilities(prevalence, sensitivity, specificity)
        result_var.set(f"P(Disease|Positive): {pos:.4f}\nP(Disease|Negative): {neg:.4f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numbers between 0 and 1.")

root = tk.Tk()
root.title("Bayes' Theorem - Medical Test Calculator")
root.geometry("400x300")

tk.Label(root, text="Disease Prevalence (0-1):").pack()
entry_prevalence = tk.Entry(root)
entry_prevalence.pack()

tk.Label(root, text="Test Sensitivity (0-1):").pack()
entry_sensitivity = tk.Entry(root)
entry_sensitivity.pack()

tk.Label(root, text="Test Specificity (0-1):").pack()
entry_specificity = tk.Entry(root)
entry_specificity.pack()

tk.Button(root, text="Calculate", command=compute).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 12), justify="center").pack()

root.mainloop()
