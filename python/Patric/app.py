
"""
this module prints decoded text into a more readable way
"""
import os
from coder import encoder, revealer



def welcome():
    """
    welcomes user and shows instructions
    """
    print("Welcome to the image decoder programme ")
    print("Where you can encode your message in images")
    print("And NO ONE can read it")
    print("Except the person you want to")
    print("images are not meant to be written over")
    print("Soooo....")
    print("make it short :)")



def found_it(save_path):
    """
    to show encoded message to user 
    """
    print("")
    print("image is decoded")
    print("this message was find in image: ")
    print(f"'{revealer(save_path)}'")


def path_location():
    """
    gets image and save path from user
    user can choose name for encoded image
    """
    img_location = input("Enter your image location: ")
    text = input("Enter your text wish to hide: ")
    file_name = input("choose a name for encoded image: ")
    save_location = input("Enter your save location: ")
    save_location = os.path.join(save_location, file_name + ".png")

    return img_location, text, save_location


def run():
    """
    runs the programm
    """
    welcome()

    message, img_path, save_path = path_location()

    encoder(img_path, save_path, message)

    found_it(save_path)
