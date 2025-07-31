# 📂 File Organizer and Directory Setup
This project provides Python scripts to automate the creation of a structured directory system and organize files based on metadata embedded in their filenames (e.g., city codes and dates).

## ⚙️ Requirements

- Python 3.x  
- No external libraries required

## 🛠️ Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
   

## 📂 Folder Structure
```
file-organizer/
├── scripts/
│   ├── create_dirs.py           # Creates year/month/region/city folders
│   ├── organize_files.py        # Parses filenames and copies files into folders
├── utils/
│   ├── config.py                # Region-to-city mapping
│   ├── find_path.py             # Logic to extract metadata from filenames
│   ├── logger.py                # Error logger using Python logging module
├── README.md                    # This file
├── .gitignore                   # Ignores compiled files, logs, etc.
```

## 🚀 How It Works
1. **Run** `create_dirs.py`
   - Creates the folder structure based on the current year.
   - Structure: `root/year/month/region/city/`
     
2. **Run** `organize_files.py`
   - Reads filenames like `jax030525.csv`
   - Extracts city (`jax`), month (`03` -> March), and year (`25` -> 2025)
   - Copies files to the appropriate folder (if it exists)
   - Logs any errors (e.g., invalid filenames, missing directories)

## 📌 To Do / Future Improvements

- Add `argparse` to make paths configurable via command line
- Use logging instead of print statements throughout
- Add unit tests and validation for filename formats
- Package as a CLI tool (setup.py + console_scripts)
- Accept custom region-to-city mappings via config file or JSON

## 👤 Author

Lens Ilestin    
Created: July 2025

Feel free to fork, clone, and contribute!

