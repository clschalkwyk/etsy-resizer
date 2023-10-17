from PIL import Image
import os
import cv2


imcoming = [file for file in os.listdir('incoming') if file.endswith(('.png'))]


dpi=300


sizes = ['4x6','6x9' , '8x12' ,'10x15' , '12x18' , '16x24' , '20x30' , '24x36']


def resize_image(input_path, output_path, target_width, target_height):
   with Image.open(input_path) as img:
       # Get the current image dimensions
       width, height = img.size
       print(f"Current Dimensions: Width = {width}, Height = {height}")


       ratio = width/height
       img_resized = img.resize((target_width, target_height))
       img_resized.save(output_path)
       print(f"Image saved to {ratio} with dimensions: Width = {width}, Height = {height}")


def resize_cv(input_path, output_path, target_width, target_height):
    image = cv2.imread(input_path)
    image_resized = cv2.resize(image, (target_width, target_height))
    cv2.imwrite(output_path, image_resized)



img1 = 'incoming/design-harbor-style-1-fs8.png'
img1_out = 'incoming/design-harbor-style-1_{}.png'
# resize_image(img1, img1_out, 200, 400)


for x in sizes:
   width, height = x.split('x')
   width = int(width)
   height = int(height)
   ou = img1_out.format(x)


   resize_cv(img1, ou, width*dpi, height*dpi)
   print('{} {} [{}] x {} [{}]'.format(ou, width, width*dpi, height, height*dpi))