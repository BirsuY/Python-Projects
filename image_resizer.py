#by @BirsuY on github
from PIL import Image

def resize_img():
    img_name = input("Please enter the name of the image you want to resize (with its extension): ")
    img = Image.open('img_name')

    print(f"Current image size: {img.size}")

    l = int(input("Please enter the length that you want to adjust for the image: "))
    w = int(input("Please enter the width that you want to adjust for the image: "))

    resized_img = img.resize((w, l))
    
    img_new_name = input("Please enter the name for the resized image (with its extension): ")
    resized_img.save(img_new_name)
#by @BirsuY on github