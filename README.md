# Tidy-Folder

A Python script to automatically organise files in a folder into categories such as **Documents**, **Images**, **Videos**, **Code**, and **Others**.

---

## Features

- Automatically moves files into folders based on file type
- Safely handles filename conflicts by renaming duplicates
- Undo to revert previous move
- Creates missing folders automatically
- Allows more filetypes and folder categories to be added

---

## File Categories

The default categories are defined in `file_categories.py`:

```python
FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp",
        ".svg", ".tiff", ".heic", ".ico"
    ],
    "Documents": [
        ".pdf", ".txt", ".doc", ".docx", ".rtf", ".odt",
```
etc.

You can easily add or remove file types to fit your needs.

---

## Getting Started

### Requirements

- Python 3.8 or higher

### Installation

1. **Clone the repository** (recommended):

```bash
git clone https://github.com/daniel-turczy/tidy-folder.git
cd tidy-folder
```

Or **Download ZIP** from GitHub and extract it.

---

## Run the script

```bash
python tidy_folder.py
```

Follow the prompts to enter the folder you want to organise.

---

## Usage Example

```text
Enter the path to the folder you want to organise (q to quit):
> C:\Users\Daniel\Downloads\Test

Folder organised successfully!
Type 'u' to undo this move or press ENTER to continue:
>
```

After running, your folder might look like:

```text
TestFolder/
│
├── Documents/
│   └── report.pdf
├── Images/
│   └── photo.jpg
├── Code/
│   └── script.py
└── Others/
    └── random.dat
```

## Undo Moves

If you make a mistake or want to revert changes, the script can undo the last move using the built-in undo feature. Simply type `u` when prompted.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Notes

- Only files in the specified folder are organised; subfolders are ignored.  
- Files with unknown extensions are moved to the **Others** folder.  
- Works on Windows, macOS, and Linux (Python 3.8+).
