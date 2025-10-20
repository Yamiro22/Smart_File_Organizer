from dotenv import load_dotenv
load_dotenv()

import os
import shutil
import re
import logging
import json
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline

# Load the pre-trained model for text classification
nlp = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

def categorize_file_ai(file_path):
    """Read text and ask AI for category."""
    text = ""
    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages[:3]:
                text += page.extract_text() or ""
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()[:2000]

    # Use the pre-trained model for text classification
    result = nlp(text)
    category = result[0]['label']

    return category

def sort_files():
    # Sort files logic goes here
    source_dir = config.get("source_dir", "")
    output_dir = config.get("output_dir", "")

    if not source_dir or not output_dir:
        messagebox.showerror("Error", "Please select both source and output directories.")
        return

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            category = categorize_file_ai(file_path)

            category_dir = os.path.join(output_dir, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            shutil.move(file_path, os.path.join(category_dir, file))

    messagebox.showinfo("Success", "Files sorted successfully.")

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