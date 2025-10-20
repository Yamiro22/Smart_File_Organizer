import os
import shutil
import re
import logging
import json
from datetime import datetime
from pathlib import Path

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# ---- CONFIGURATION ----
SOURCE_DIR = config.get("source_dir", "data")          # Folder containing unsorted files
OUTPUT_DIR = config.get("output_dir", "output")        # Folder where sorted files will be saved
LOG_DIR = config.get("log_dir", "logs")               # Folder for run logs
SORT_BY_DATE = config.get("sort_by_date", True)        # Set to True to group by creation date
NAME_PATTERNS = config.get("name_patterns", {            # Optional: Regex keywords → sub-folders
    "invoice": "Invoices",
    "report": "Reports",
    "project": "Projects"
})

# File categories by extension
FILE_TYPES = config.get("file_types", {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"]
})

# ---- SETUP ----
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

log_filename = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_path = os.path.join(LOG_DIR, log_filename)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def get_category(file_name: str) -> str:
    """Return category folder based on extension or regex match."""
    ext = os.path.splitext(file_name)[1].lower()

    # Match by file extension
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category

    # Match by regex pattern
    for pattern, folder in NAME_PATTERNS.items():
        if re.search(pattern, file_name, re.IGNORECASE):
            return folder

    return "Others"

def sort_files():
    """Sort files from SOURCE_DIR into OUTPUT_DIR."""
    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    logging.info(f"Found {len(files)} files in /{SOURCE_DIR}")

    for file in files:
        src_path = os.path.join(SOURCE_DIR, file)
        category = get_category(file)
        date_folder = ""

        if SORT_BY_DATE:
            ctime = datetime.fromtimestamp(os.path.getctime(src_path))
            date_folder = ctime.strftime("%Y-%m-%d")

        dest_dir = Path(OUTPUT_DIR) / category / date_folder
        os.makedirs(dest_dir, exist_ok=True)

        try:
            shutil.move(src_path, dest_dir)
            logging.info(f"Moved {file} → {dest_dir}")
        except Exception as e:
            logging.error(f"Failed to move {file}: {e}")

    logging.info("Sorting completed successfully ✅")

if __name__ == "__main__":
    print("🚀 Smart File Organizer running…")
    sort_files()
    print(f"✅ Sorting complete! Log saved at: {log_path}")
