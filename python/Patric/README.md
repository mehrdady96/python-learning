# Patrik


Patrik is a simple Python image steganography project.


It allows the user to hide a text message inside an image and
decode the hidden message later.


## Features


- Hide text messages inside images
- Decode hidden messages from encoded images
- Save the encoded image as a PNG file
- Simple command-line interface


## Requirements


- Python 3
- Pillow


Install Pillow with:


```bash
pip install -r requirements.txt
```
Project Structure
patrik/
│
├── main.py
├── app.py
├── coder.py
├── requirements.txt
├── .gitignore
└── README.md

### main.py

The entry point of the application.

### app.py

Handles user interaction and controls the flow of the program.

### coder.py

Contains the main image encoding and decoding logic.

### requirements.txt

Contains the Python packages required by the project.

## How to Run

Run the following command:
```
python main.py
```
Then follow the instructions shown in the terminal.

## How It Works

The program converts each character of the message into its Unicode
value using ord() and stores the encoded information in specific
pixels of the image.

During decoding, the program reads those pixels and converts the
stored values back into characters using chr().

# Note

This is an educational project created to practice Python,
Pillow, functions, modules, and Git/GitHub.
