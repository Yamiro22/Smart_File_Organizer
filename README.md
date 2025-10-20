# 🧠 Smart File Organizer

![AI Powered](https://img.shields.io/badge/AI-Powered-lightblue?logo=openai&logoColor=white) ![Build](https://img.shields.io/badge/Build-PyInstaller-lightgrey?logo=gear&logoColor=white)

A **smart desktop automation tool** that automatically sorts, classifies, and organizes files using AI.

Built with **VS Code** , **Tabnine** , and **PySimpleGUI** , it features **real-time monitoring** , **AI categorization** , and a modern **GUI** .

---

## 🚀 Getting Started

### 🧩 Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- (Optional) [OpenAI API Key](https://platform.openai.com/account/api-keys) — for AI categorization

---

### ⚙️ Installation

```bash
git clone https://github.com/Yamiro22/Smart_File_Organizer.git
cd Smart_File_Organizer
pip install -r requirements.txt
```

If you plan to use **AI features** :

```bash
pip install openai langchain transformers torch
```

If you plan to use **real-time folder monitoring** :

```bash
pip install watchdog
```

---

## ▶️ Running the App

### 1️⃣ **Graphical Interface**

```bash
python main_gui.py
```

Choose your source/output folders, enable AI mode, and click **“Sort Files”** .

---

### 2️⃣ **Real-Time Mode**

Run this to auto-organize files as soon as they appear:

```bash
python main_watch.py
```

✅ The tool will run in the background and instantly sort new files.

---

### 3️⃣ **Run Tests**

```bash
python -m unittest discover
```

---

## 🧠 Key Features

| Feature                    | Description                            | Libraries               |
| -------------------------- | -------------------------------------- | ----------------------- |
| 🔹**Automatic Sorting**    | Organizes files by type, date, or name | `os`,`shutil`           |
| 🔹**GUI Interface**        | User-friendly desktop app              | `PySimpleGUI`           |
| 🔹**Real-Time Monitoring** | Detects new files instantly            | `watchdog`              |
| 🔹**AI Categorization**    | Analyzes content & filenames           | `OpenAI`,`Transformers` |
| 🔹**Logging System**       | Tracks all operations                  | `logging`               |
| 🔹**.exe Packaging**       | Runs standalone on Windows             | `PyInstaller`           |

---

## ⚙️ Configuration (`config.json`)

```json
{
  "source_dir": "data",
  "output_dir": "output",
  "log_dir": "logs",
  "sort_by_date": true,
  "file_types": {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov"],
    "Audio": [".mp3", ".wav"]
  },
  "name_patterns": {
    "invoice": "Invoices",
    "report": "Reports",
    "contract": "Contracts"
  }
}
```

---

## 🧰 Built With

- [Python](https://www.python.org/) — Core Language
- [PySimpleGUI](https://pysimplegui.readthedocs.io/) — GUI Framework
- [OpenAI API](https://platform.openai.com/) — AI Categorization
- [Transformers](https://huggingface.co/docs/transformers/index) — Local Model Integration
- [Watchdog](https://pythonhosted.org/watchdog/) — File Monitoring
- [VS Code + Tabnine](https://code.visualstudio.com/) — Development Tools

---

## 🧪 Testing

```bash
python -m unittest test_main_gui.py
```

All test cases validate directory creation, file movement, and logging behavior.

---

## 📦 Packaging into .exe

```bash
pyinstaller --noconsole --onefile main_gui.py --icon=logo.ico --add-data "config.json;."
```

The executable will be created in:

```
/dist/SmartFileOrganizer.exe
```

---

## 🧭 Project Roadmap

| Stage | Goal                        | Tools / Libraries               | Status  |
| ----- | --------------------------- | ------------------------------- | ------- |
| **1** | Core Logic & Config         | Python, JSON                    | ✅ Done |
| **2** | GUI Interface               | PySimpleGUI                     | ✅ Done |
| **3** | Real-Time Watch Feature     | Watchdog                        | ✅ Done |
| **4** | Package to `.exe`           | PyInstaller                     | ✅ Done |
| **5** | GitHub & Portfolio Showcase | GitHub, Wix Studio              | ✅ Done |
| **6** | AI-Powered Upgrade          | OpenAI, LangChain, Transformers | ✅ Done |

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE.txt](https://chatgpt.com/c/LICENSE.txt) file for details.

---

## 👤 Author

**Mohammed Yamin**

📍 Amman, Jordan

💼 [Developer Portfolio](https://cw9r7kv2pd.wixstudio.com/developer-portfolio)

💻 [GitHub Profile](https://github.com/Yamiro22)

✉️ [moyamingo1234@gmail.com](mailto:moyamingo1234@gmail.com)

---

## 🌟 Acknowledgments

- Developed entirely using **VS Code + Tabnine AI**
- AI-Powered by **OpenAI** and **Hugging Face Transformers**
- Inspired by the need for smart digital organization tools
