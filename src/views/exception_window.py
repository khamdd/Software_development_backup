import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import tkinter as tk

class ExceptionWindow:
    def __init__(self, message):
        self.root = tk.Tk()
        self.root.title("Error")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#607b8d")
        
        self.error_frame = tk.LabelFrame(self.root, text="Error", padx=20, pady=20, fg="red", bg="#607b8d")
        self.error_frame.pack(fill="both", expand="yes", padx=20, pady=20)
        self.error_frame.columnconfigure(0, weight=1)
        self.error_frame.columnconfigure(1, weight=1)
        
        warning_icon = tk.Label(self.error_frame, text="⚠️", bg="#607b8d", fg="yellow", justify="left", font=("Arial", 20))
        warning_icon.grid(row=0, column=0, sticky="w", pady=5, padx=5)
        
        error_label = tk.Label(self.error_frame, text=message, bg="#607b8d", fg="white", justify="left", font=("Arial 12 bold"), wraplength=300)
        error_label.grid(row=0, column=1, sticky="w", pady=5, padx=5)
        
        close_button = tk.Button(self.error_frame, text="Close", command=self.close)
        close_button.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        self.root.mainloop()
        
    def close(self):
        self.root.destroy()