File Organizer Scripts

This repository contains two Python scripts designed for organizing and managing files based on their extensions. These scripts help automate file management tasks such as sorting files into categorized folders and moving files to a target directory.

Scripts Overview

1. organize.py

Purpose

This script organizes files in a specified source folder by grouping them into subfolders based on their extensions. Each file type (extension) will have its own folder.

How It Works

The user specifies a source folder and a list of file extensions.

The script creates subfolders for each extension inside the source folder (if they don't already exist).

Files matching the specified extensions are moved into the respective subfolders.


Usage

1. Run the script.


2. Provide the path to the source folder.


3. Enter the file extensions to organize (comma-separated, e.g., .txt,.jpg).


4. The script will create categorized subfolders and organize the files.



Example

If you specify extensions .txt and .jpg:

Files like document.txt will move to TXT_Files/.

Files like image.jpg will move to JPG_Files/.



---

2. move.py

Purpose

This script moves files from a source folder to a target folder based on their extensions. It ensures that only specified file types are transferred.

How It Works

The user specifies a source folder, a target folder, and a list of file extensions.

The script moves files with matching extensions from the source folder to the target folder.


Usage

1. Run the script.


2. Provide the path to the source folder.


3. Provide the path to the target folder.


4. Enter the file extensions to move (comma-separated, e.g., .txt,.png).


5. The script will transfer the files.



Example

If you specify extensions .png and .docx:

Files like image.png will move to the target folder.

Files like report.docx will also move to the target folder.



---

Prerequisites

Ensure you have Python installed on your system (Python 3.x recommended). These scripts rely on the following standard library modules:

os

shutil


No additional packages are required.


---

Running the Scripts

1. Download the scripts.


2. Open a terminal or command prompt.


3. Navigate to the folder containing the scripts.


4. Execute the scripts using Python:

python organize.py

or

python move.py




---

Notes

Ensure that the source folder contains files before running the scripts.

For safety, avoid specifying system-critical directories as the source or target folders.

Use the scripts responsibly to avoid unintentional data loss.
