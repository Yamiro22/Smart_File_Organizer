import os
import shutil
import re
import logging
import json
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# ... rest of your code ...

def sort_files():
    # Sort files logic goes here
    pass

def select_source_dir():
    source_dir = filedialog.askdirectory(initialdir=config.get("source_dir", "."), title="Select Source Directory")
    if source_dir:
        config["source_dir"] = source_dir
        save_config()

def select_output_dir():
    output_dir = filedialog.askdirectory(initialdir=config.get("output_dir", "."), title="Select Output Directory")
    if output_dir:
        config["output_dir"] = output_dir
        save_config()

def save_config():
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def create_gui():
    root = tk.Tk()
    root.title("Smart File Organizer")

    # Source directory label and button
    source_label = tk.Label(root, text="Source Directory:")
    source_label.pack(pady=10)

    source_dir_var = tk.StringVar()
    source_dir_var.set(config.get("source_dir", ""))

    source_entry = tk.Entry(root, textvariable=source_dir_var, width=50)
    source_entry.pack()

    source_button = tk.Button(root, text="Select Source Directory", command=select_source_dir)
    source_button.pack(pady=5)

    # Output directory label and button
    output_label = tk.Label(root, text="Output Directory:")
    output_label.pack(pady=10)

    output_dir_var = tk.StringVar()
    output_dir_var.set(config.get("output_dir", ""))

    output_entry = tk.Entry(root, textvariable=output_dir_var, width=50)
    output_entry.pack()

    output_button = tk.Button(root, text="Select Output Directory", command=select_output_dir)
    output_button.pack(pady=5)

    # Sort files button
    sort_button = tk.Button(root, text="Sort Files", command=sort_files)
    sort_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()