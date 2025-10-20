# 📘 **README.md**

```markdown
# 🧠 Smart File Organizer

**Developer:** Mohammed Yamin  
**IDE:** VS Code | **AI Assistant:** Tabnine  
**Language:** Python 3.11+

An intelligent automation tool that scans folders and **automatically sorts files** by **type**, **date**, or **name pattern** — saving time and keeping your workspace clean.  
Built in VS Code with Tabnine AI assistance for optimized and readable code.

---

## 🚀 Features

✅ Automatically detects and moves files by:

- **File Type** → images, videos, documents, audio, etc.
- **Creation Date** → groups files by day.
- **Name Pattern** → detects words like “invoice”, “report”, “project”.

✅ Supports **custom configuration** via `config.json`  
✅ Creates **detailed log files** for each run  
✅ Lightweight — runs on any machine with Python 3  
✅ Designed and formatted professionally with Tabnine + VS Code

---

## 🗂️ Folder Structure
```

Smart_File_Organizer/

│

├── main.py

├── config.json

├── requirements.txt

├── README.md

│

├── data/ # Unsorted files

├── output/ # Sorted files

└── logs/ # Run logs

````

---

## ⚙️ Installation Guide

1️⃣ **Clone the repository**
```bash
git clone https://github.com/Yamiro22/Smart_File_Organizer.git
cd Smart_File_Organizer
````

2️⃣ **Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # macOS/Linux
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Prepare your folders**

```
/data     → place unsorted files here
/output   → will be auto-created for sorted files
/logs     → will store log reports
```

5️⃣ **Run the tool**

```bash
python main.py
```

---

## ⚙️ Configuration (`config.json`)

```json
{
  "source_dir": "data",
  "output_dir": "output",
  "log_dir": "logs",
  "sort_by_date": true,

  "file_types": {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"]
  },

  "name_patterns": {
    "invoice": "Invoices",
    "report": "Reports",
    "project": "Projects",
    "contract": "Contracts",
    "resume": "Resumes"
  },

  "logging_level": "INFO"
}
```

💡 Edit this file to change file categories or turn off date-based sorting.

---

## 🧰 Technologies Used

| Tool                                 | Purpose                 |
| ------------------------------------ | ----------------------- |
| **Python 3.11+**                     | Core language           |
| **VS Code**                          | Development IDE         |
| **Tabnine**                          | AI code assistant       |
| **os, shutil, re, pathlib, logging** | File handling & logging |
| **pandas / openpyxl (optional)**     | Advanced Excel handling |
| **PySimpleGUI (optional)**           | GUI interface           |

---

## 🧾 Example Log Output

```
2025-10-20 13:22:18 | INFO | Found 34 files in /data
2025-10-20 13:22:19 | INFO | Moved 10 image files → /output/Images/2025-10-20/
2025-10-20 13:22:19 | INFO | Moved 8 documents → /output/Documents/2025-10-20/
2025-10-20 13:22:20 | INFO | Sorting completed successfully ✅
```

---

## 📸 Screenshots / Demo

> **Before:** Folder with mixed files
>
> **After:** Auto-organized folders by type and date

_(Insert your own screenshots from VS Code terminal and Explorer here)_

---

## 🧩 Future Enhancements

- 🪄 Add real-time file monitoring
- 📦 Integrate GUI for drag-and-drop folders
- 🌐 Add web dashboard using Flask
- 📤 Include cloud sync support (Google Drive API)

---

## 💬 Author

**Mohammed Yamin**

📍 Amman, Jordan

💼 [Developer Portfolio](https://cw9r7kv2pd.wixstudio.com/developer-portfolio)

💻 [GitHub Profile](https://github.com/Yamiro22)

✉️ [moyamingo1234@gmail.com](mailto:moyamingo1234@gmail.com)

---

## 🏁 License

This project is licensed under the MIT License — feel free to use and improve it.

---

## 🌟 Support

If you like this project, please ⭐ star it on GitHub and add it to your portfolio
