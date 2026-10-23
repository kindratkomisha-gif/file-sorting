# File Organizer by Extension

A Python script that automatically scans a specified directory (including all nested subfolders), identifies files, groups them by their extensions, and neatly organizes them into corresponding newly created folders.

##  How It Works

1. **Scanning:** The script utilizes the `os.walk` method to perform a deep scan of the specified `base_pass` directory. It finds files even in the deepest subfolders.
2. **Analysis:** Using the `.rpartition(".")` string method, the script safely extracts each file's extension (everything after the last dot).
3. **Grouping:** Files are organized into lists inside the `grouped_file` dictionary, where the key is the extension itself and the value is the full path to the file.
4. **Moving:** New directories named after the extensions (e.g., `txt`, `png`, `pdf` folders) are created in the root folder (if they don't already exist), and the `shutil` module physically moves the files there.

## 🛠 Requirements

The script only requires **Python 3.x** installed. 
All used libraries (`os`, `shutil`) are built-in, so there is no need to install any additional packages via `pip`.

## 💻 Usage and Setup

⚠️ **IMPORTANT WARNING:** Before running the script, **make sure to create a backup copy (duplicate)** of all files and folders in the directory you plan to sort! The script physically moves files, so for the safety of your data, it is highly recommended to test it on a copy of your folder first.

1. Open the script file (e.g., `organizer.py`).
2. Specify the path to the folder you want to clean up in the `base_pass` variable. By default, it is set to:
   ```python
   base_pass = "C:\\Users\\balan\\Desktop\\oppgave"
   ```
   *Note: If you are using Windows, do not forget to double the backslashes (`\\`) to avoid path reading errors.*
3. Run the script via your terminal or Integrated Development Environment (IDE):
   ```bash
   python organizer.py
   ```

## 📋 Key Variables Explained

* `base_pass` — The root path to your target directory (the one to be sorted).
* `grouped_file` — A dictionary (`dict`) that temporarily stores data in RAM in the following format: `{ 'extension': ['list_of_full_file_paths'] }`.
* `full_file_path` — Combines the absolute path to a file by merging the current subfolder (`paths`) and the filename (`file`). This prevents the *"The system cannot find the file specified"* error.
* `os.path.basename(file)` — Strips away the long path, leaving only the clean filename with its extension to ensure it saves correctly in the new location.

## ⚠️ Important Note
If you have files with identical extensions but written in different cases (e.g., `photo.JPG` and `image.jpg`), the script will create two separate folders: `JPG` and `jpg`. If you want to merge them, you can simply add the `.lower()` method to the `prefix` variable in the code.
