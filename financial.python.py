import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

class FinancialSimulator:
    def __init__(self, root):
        self.transaction = []
        self.root = root
        self.root.title("Financial Simulator")
        
        
        # Set thwe theme color
        self.bg_color = "#f0f0f0" 
        self.button_color = "#4CAF50"
        self.text_color="#333"
        self.root.configure(bg=self.bg_color)
        #Setup UI
        self.create_widgets()

    def create_widgets(self):
        #Title label
        self.title_label = tk.Label(self.root, text="Financial Simulator", font=("Helvetica", 18, "bold"), bg=self.bg_color, fg=self.text_color)
        self.title_label.pack(pady=20)
        # Frame for Inputs
        self.input_frame = tk.Frame(self.root, bg=self.bg_color)
        self.input_frame.pack(pady=10, padx=20, fill=tk.x)
        # Amount Entry 
        self.amount_label = tk.Label(self.input_frame, text="Amount:", bg=self.bg_color, fg=self.text_color)
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.amount_entry = tk.Entry(self.input_frame,width=30)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)
        # Description Entry
        self.description_label = tk.Label(self.input_frame, text="Description:", bg=self.bg_color, fg=self.text_color)
        self.description_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.description_entry = tk.Entry(self.input_frame,width=30)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)
        # Buttons
        self.add_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction, bg=self.button_color, fg="white")
        self.add_button.pack(pady=5, padx=20, fill=tk.x)
        self.balance_button = tk.button(self.root, text="View Balance",command=self.view_balance, bg=self.button_color, fg="white")
        self.balance_button.pack(pady=5, padx=20, fill=tk.x)
        self.report_button = tk.button(self.root, text="Generate Report",command=self.view_balance, bg=self.button_color, fg="white")
        self.report_button.pack(pady=5, padx=20, fill=tk.x)
        # Scrolled Text widget for displaying reports
        