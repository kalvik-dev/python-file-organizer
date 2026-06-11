# Python File Organizer

A simple Python automation script that organizes files into folders based on their file extensions.

## Features

- Automatically detects file types
- Creates folders if they do not exist
- Moves files into categorized directories
- Supports:
  - PDF files
  - DOCX files
  - Images (JPG, PNG)
  - Videos (MP4)
  - Text files
  - Songs (MP3)
- Ignores existing folders while scanning

## Technologies Used

- Python
- os module
- shutil module

## Project Structure

Before:

```
Notes/
├── notes.pdf
├── resume.docx
├── photo.jpg
├── movie.mp4
```

After:

```
Notes/
├── PDF/
│   └── notes.pdf
├── DOCX/
│   └── resume.docx
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
```

## How It Works

1. Reads all files from the target directory.
2. Identifies file extensions using `os.path.splitext()`.
3. Creates destination folders if needed.
4. Moves files using `shutil.move()`.
5. Skips existing directories.

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/python-file-organizer.git
```

Navigate to the project:

```bash
cd python-file-organizer
```

Run the script:

```bash
python file_organizer.py
```

## Future Improvements

- Support more file types
- Organize unknown files into an "Others" folder
- Command-line arguments
- GUI version using Tkinter
- Recursive folder scanning

## Author

Vivek Kaloori
