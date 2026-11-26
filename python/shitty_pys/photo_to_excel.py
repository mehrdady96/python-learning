'''
finds average RGB in a 10x10 pixcel and fills a cell in excel
'''
import openpyxl
from PIL import Image

img = input(" Enter your file location : ")
def find_rgb(image):
    '''
    finds every 10x10 pixcel in a photo
    '''
    photo = Image.open(image).convert("RGB")
    array = []
    x_start = 0
    y_start = 0
    sqaure_size = 10
    width = (photo.width) - sqaure_size + 1
    height = (photo.height) - sqaure_size + 1
    for y_start in range(0 , 10 , sqaure_size):
        for x_start in range(0 , 10 , sqaure_size):
            r = 0
            g = 0
            b = 0
            sqaure = []
            for y in range(y_start , y_start + sqaure_size):
                row = []
                for x in range(x_start , x_start + sqaure_size):
                    red, green, blue = photo.getpixel((x, y))
                    clr = (red, green, blue)
                    row.append(clr)
                sqaure.append(row)
            array.append(sqaure)
    return array

def burn_rgb(img):
    '''
    takes the average RGB and fills a cell in excel for 10 pixcels
    '''
    
for matrix in find_rgb(img):
    for row in matrix:
        print(row)
    print()
