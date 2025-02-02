# Password Generator

This project is a simple password generator written in Python, using the tkInter and pyperclip modules. It allows users to generate random passwords with specified lengths and character sets.

## Features

- Generate passwords of a specified length
- Include or exclude uppercase letters, lowercase letters, digits, and special characters
- Copy the generated password to the clipboard

## Requirements

- Python 3.x
- `pyperclip` library (for clipboard functionality)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/pwiez/personalprojects.git
    ```
2. Navigate to the project directory:
    ```sh
    cd passwordgenerator
    ```
3. Install the required dependencies:
    ```sh
    # Ensure you are in a virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
    # Install dependencies
    pip install pyperclip==1.9.0
    ```
4. Ensure `tkinter` is installed:
- **Linux**:
    ```sh
    sudo apt-get install python3-tk
    ```
- **macOS and Windows**:
    Tkinter is included with the standard Python installation. If you encounter issues, you may need to install Python from [python.org](https://www.python.org/downloads/).

## Usage

From the project folder, run the `passwordgenerator.py` file using the terminal (or cmd on Windows) to start the password generator:
```sh
python3 passwordgenerator.py
