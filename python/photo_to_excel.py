import openpyxl
from PIL import Image

img = "C:\\Users\\farha\\Desktop\\patrik.jpg"

def find_rgb(image):
    """
    moves in image in a 10x10 squares
    """
    photo = Image.open(image)
    width = image.width
    height = image.height
    start = 0
    finish = 0
    r = 0
    g = 0
    b = 0
    for y in range(height):
        for x in range(11):
            rgb_photo = photo.convert("RGB")
            red , green , blue = rgb_photo.getpixel((x,y))
            r += red
            g += green
            b += blue

    r = round(r/100 )
    g = round(g/100 )
    b = round(b/100 )
    return  r , g , b



print(x , y)
print(find_rgb(img))
