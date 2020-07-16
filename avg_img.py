from os import listdir
from PIL import Image
import numpy as np

def avg_img(x=400, y=400, directory = 'images', output = 'avg.jpg'):
    """
    the function averages the pictures in the 'directory' and
    the output is saved as 'output' with pixels 'x' by 'y'
    """


    # black (blank) image data XxY(RGB) in numpy array format
    master_data = np.zeros((y,x,3), int)
    # counts the total number of images processed
    count = 0


    # go through all images in a directory
    for filename in listdir(directory):
        count += 1
        # load each image 
        img = Image.open(f'{directory}/{filename}')
        # resize image to fit the master_data
        img_resized = img.resize((x,y))
        # turns image to numpy array
        img_data = np.asarray(img_resized)
        # sums all images
        master_data += img_data


    # average the data
    master_data = master_data//count
    # turn numpy data into image
    master_image = Image.fromarray(master_data.astype("uint8"))

    # saves the image to the directory
    master_image.save(output)
