# Python Projects

A collection of Python projects I've built while learning Python through hands-on practice.

I focus on learning by building projects rather than only following tutorials. Each project introduces new Python concepts and gradually increases in complexity.

---

## 📂 Projects

### 1. 🔐 Password Strength Checker

A Python program that analyzes a password and evaluates its strength based on multiple characteristics.

#### Features
- Checks password length
- Checks uppercase characters
- Checks lowercase characters
- Checks numbers
- Checks special characters
- Detects repeated characters
- Detects sequential characters
- Calculates a password strength score
- Converts the score into a rating out of 10

#### Concepts learned
- Strings
- Loops
- Functions
- `string` module
- String methods
- Conditional statements
- Sets
- Basic scoring algorithms

---

### 2. 🔑 Password Generator

A Python program that generates random and secure passwords using a combination of letters, numbers, and special characters.

#### Features
- Generates random passwords
- Uses uppercase letters
- Uses lowercase letters
- Uses numbers
- Uses special characters
- Allows control over password length
- Uses Python's `secrets` module for secure random generation

#### Concepts learned
- `secrets`
- `string`
- Random generation
- Strings
- Lists
- Loops
- Functions
- User input

---

### 3. 🔒 Password Hashing Program

A Python program for generating cryptographic hashes from input data using Python's `hashlib` module.

#### Features
- Accepts user input
- Generates cryptographic hashes
- Supports different hashing algorithms
- Uses hexadecimal digest output

#### Concepts learned
- `hashlib`
- Hash functions
- `.update()`
- `.hexdigest()`
- String encoding
- Python modules

---

### 4. 📁 File Organizer

A Python program that automatically organizes files into folders based on their file extensions.

#### Features
- Detects file extensions
- Separates files into categories
- Automatically creates folders when required
- Moves files using `shutil`
- Handles images
- Handles videos
- Handles documents
- Handles music
- Handles archives
- Handles source code
- Places unknown file types into an `Other` folder
- Ignores directories and only processes files

#### Supported categories

| Category | Examples |
|---|---|
| Images | JPG, PNG, GIF, WEBP, SVG, BMP |
| Videos | MP4, MKV, AVI, MOV, WEBM |
| Documents | PDF, DOCX, TXT, XLSX, PPTX |
| Music | MP3, WAV, FLAC, AAC, OGG |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JS, HTML, CSS, JAVA, C, CPP |
| Other | Unknown file types |

#### Concepts learned
- `os`
- `shutil`
- `os.listdir()`
- `os.path.join()`
- `os.path.basename()`
- `os.path.splitext()`
- File paths
- Directory creation
- File movement
- Sets
- File extension handling

---

### 5. ✅ CLI To-Do List

A command-line task management application that stores tasks permanently using JSON.

#### Features
- View tasks
- Add tasks
- Delete tasks
- Modify task names
- Mark tasks as completed/incomplete
- Persistent task storage
- Automatically saves changes to JSON
- Handles missing JSON files
- Handles invalid JSON
- Validates user input
- Handles invalid menu selections
- Prevents empty task names

#### Example

```text
------TO-DO LIST-------

What do you want to do ?

1. View Tasks
2. Add Tasks
3. Delete Task
4. Modify
5. EXIT

Please enter the number of your selection:
