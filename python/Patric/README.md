# Patrik 🖼️

A small Python experiment in image steganography: hide a short text message inside an image, then read it back from the encoded image.

## Features

- Hide a text message inside an image
- Save the result as a PNG file with a name and folder you choose
- Decode a hidden message from an encoded image
- Simple command-line interface

## Requirements

- Python 3
- [Pillow](https://pypi.org/project/pillow/)

```bash
pip install Pillow
```

## How to run

```bash
python main.py
```

The program asks for four things, in this order:

1. The location of the image to hide the message in
2. The text to hide
3. A name for the encoded image
4. The folder to save it in

The encoded image is saved as `<folder>/<name>.png`, and the program then decodes it and prints the hidden message.

## How it works

**Encoding** (`encoder` in `coder.py`): each character of the message is converted to its Unicode number with `ord()`. For the character at position `i`, the program colors one pixel pure red `(255, 0, 0)` at:

- row `800 + i`
- column `ord(character) + 300`

**Decoding** (`decoder` in `coder.py`): the program scans the image from row 800 downward, and every pure red pixel it finds becomes the character `chr(column - 300)`.

The result is saved as PNG because PNG is lossless. A format like JPEG would change the pixel colors and destroy the message.

## Image requirements

- The image must be an RGB image at least `ord(character) + 301` pixels wide for the highest character in the message. Lowercase English letters need about 423 pixels; other characters can need more.
- The image must be at least `800 + (message length)` pixels tall.
- If the image is too small, encoding fails with an `IndexError`.
- Pure red pixels that already exist in the image below row 800 would be read as part of the message.

## Project structure

```
Patric/
├── main.py     # entry point, starts the app
├── app.py      # user interaction: prompts and printed messages
├── coder.py    # encoding and decoding logic
└── README.md
```

## Note

This is an educational project, and it is not secure: anyone who knows how the message is stored can read it. It was created to practice Python, Pillow, functions, modules, and Git/GitHub.
