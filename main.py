from PIL import Image
import os
import cv2


imcoming = [file for file in os.listdir('incoming') if file.endswith(('.png'))]


dpi=300


#2:3
sizes = ['4x6','6x9' , '8x12' ,'10x15' , '12x18' , '16x24' , '20x30' , '24x36']

#3:4
sizes2 = ['6x8',
'9x12',
'12x16',
'15x20',
'18x24',
'24x32']


#4:5
sizes3= [
'4x5',
'8x10',
'12x15',
'16x20',
'20x25',
'24x30']



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



img1 = 'incoming/design-lions_Watercolor.png'
# resize_image(img1, img1_out, 200, 400)

img_out = img1[:-4]
img_ext = img1.split('.')[-1]

def run_resize(type, sizes):
    for x in sizes:
       width, height = x.split('x')
       width = int(width)
       height = int(height)
       new_filename = f"{img_out}_{type}_{x}.{img_ext}"
       resize_cv(img1, new_filename, width*dpi, height*dpi)
       print('{} {} [{}] x {} [{}]'.format(new_filename, width, width*dpi, height, height*dpi))


run_resize('2by3', sizes)
run_resize('3by4', sizes)
run_resize('4by5', sizes)