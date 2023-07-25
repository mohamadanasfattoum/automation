from PIL import Image
import os

file_size = int(input('Enter size: '))
output_folder = input('Enter output_folder Name: ')

os.chdir('images')

if not os.path.isdir(output_folder):  # python create folder if not exists
   os.mkdir(output_folder)

for filename in os.listdir('.'):    #python code loop in folder file
    #print(filename)
    if filename.endswith(('.jpg','.png','.jp')):   #python check file extension
        image= Image.open(filename)
        width , heigth = image.size    #python pillow get image width and height
        #print(width , heigth)
        if width > file_size and heigth > file_size:
            if width > heigth:
                heigth= int((file_size/width)*heigth)
                width= file_size

            else:
                width= int((file_size/heigth)*width)
                heigth= file_size
            image = image.resize((width,heigth))
            image = image.save(os.path.join(output_folder,filename.lower()))
            #image = image.resize((file_size,file_size))
            #image = image.save(output_folder,filename.lower())