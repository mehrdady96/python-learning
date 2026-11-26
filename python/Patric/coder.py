"""
this module encodes your text in your given image
"""

from PIL  import Image


def extrct_ord(user):
    """
    this function only makes message into ord
    used in encoder function
    return is not used directly
    """
    words = []
    for x in user:
        words.append(ord(x))
    return words



def encoder(img_path , save_path, message):
    """
    burns the message into image
    """
    img = Image.open(img_path)
    y = 800
    for x in extrct_ord(message):
        img.putpixel((x+300 , y),(255, 0, 0))
        y += 1

    img.save(save_path)
    return img



def decoder(save_path):
    """
    decodes hidden message in image
    """
    hidden_message = []
    img = Image.open(save_path)
    x, y = img.size
    start = 800
    for j in range(start,y):
        for i in range(0,x):
            pixel  = img.getpixel((i,j))
            start += 1
            if pixel == (255, 0, 0):
                hidden_message.append(chr(i-300))
                if chr(i) == ".":
                    break

    return hidden_message



def revealer(save_path):
    """
    makes the encoded message readable
    """
    encoded = decoder(save_path)
    true_message = "".join(encoded)

    return true_message
