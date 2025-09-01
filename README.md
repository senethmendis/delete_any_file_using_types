# Delete Files by Extension (Python Script)
<div align="center">
  <br />
    <a href="https://github.com/senethmendis/delete_any_file_using_types/blob/main/dp.png" target="_blank">
      <img src="public/readme/hero.png" alt="Project Banner">
    </a>
  <br />
  <div/>




This Python script allows you to delete files with a specific file extension (e.g., `.AAE`, `.JPG`, `.PNG`) from a given directory.  
You can choose whether to delete files only in the specified directory or recursively in all its subdirectories.

---

## 🚀 Features
- Delete files by extension (case-insensitive).
- Option to include or exclude subfolders.
- Prints a list of deleted files and a summary count.
- Works on **Windows**, **Linux**, and **macOS**.

---

## 📂 Example Usage

### Run directly inside your script
```python
from delete import delete_files_by_extension

# Delete all .AAE files (non-recursive)
delete_files_by_extension(r"D:\Pictures\iPHONE UPACK\images\2025-08-02", ".AAE", recursive=False)

# Delete all .JPG files (recursive, includes subfolders)
delete_files_by_extension("C:/Users/mendi/Desktop/photos", ".JPG", recursive=True)
