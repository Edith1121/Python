



# 🔐 Secure Password Generator

A Python-based secure password generator that creates strong, random passwords using Python's `secrets` module. The program validates every generated password and automatically regenerates it if it contains weak patterns.

## Features

* Generates cryptographically secure passwords using the `secrets` module.
* Default password length of **16 characters**.
* Uses:

  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Numbers (`0-9`)
  * Special characters
* Automatically rejects passwords containing:

  * Four or more repeated characters (e.g. `AAAA`, `1111`, `$$$$`)
  * Sequential lowercase letters (e.g. `abcd`)
  * Sequential uppercase letters (e.g. `WXYZ`)
  * Sequential digits (e.g. `1234`)
  * Reverse sequences (e.g. `dcba`, `9876`)
* Keeps generating passwords until a valid one is produced.

## Requirements

* Python 3.8 or later

No external libraries are required.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

2. Open the project directory:

```bash
cd <repository-name>
```

3. Run the program:

```bash
python main.py
```

## Example Output

```text
Generated Password:
Q@8rLm!2Zx#7Pw$N
```

## Project Structure

```text
.
├── main.py
└── README.md
```

## Technologies Used

* Python
* `string`
* `secrets`

## Future Improvements

* Allow users to choose the password length.
* Guarantee at least one uppercase, lowercase, digit, and symbol.
* Option to include or exclude symbols.
* Password strength scoring.
* Check against common or leaked passwords.
* Export generated passwords to a file or clipboard.
* Graphical user interface (GUI).

## Why `secrets` Instead of `random`?

Python's `secrets` module is designed for generating cryptographically secure random values. Unlike the `random` module, it is suitable for passwords, authentication tokens, and other security-related applications.

## License

This project is released under the MIT License.
