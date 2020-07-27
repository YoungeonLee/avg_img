from os import listdir
from PIL import Image
import numpy as np

def avg_img(x=400, y=400, directory = 'images', output = 'avg', limit = float("inf")):
    """
    the function averages the pictures in the 'directory' and
    the output is saved as 'output'.jpg with pixels 'x' by 'y'
    """
    # black (blank) image data XxY(RGB) in numpy array format
    master_data = np.zeros((y,x,3), int)
    # counts the total number of images processed
    count = 0

    print("Working on averaging the images...")
    # go through all images in a directory
    for filename in listdir(directory):
        count += 1
        # load each image
        try:
            img = Image.open(f'{directory}/{filename}').convert("RGB")
        except Exception as e:
            print(e)
            print(f"Unable to open {filename}")
            continue
        # resize image to fit the master_data
        img_resized = img.resize((x,y))
        # turns image to numpy array
        img_data = np.asarray(img_resized)
        # sums all images
        master_data += img_data
        if count == limit:
            break


    # average the data
    master_data = master_data//count
    # turn numpy data into image
    master_image = Image.fromarray(master_data.astype("uint8"))

    # saves the image to the directory
    master_image.save(f"{output}.jpg")
    print(f"Finished! image saved to '{output}.jpg'")



def avg_img_with_different_amounts(x=400, y=400, directory = 'images', output = 'avg'):
    amounts = []
    length = len(listdir(directory))
    while length != 0:
        amounts.insert(0, length)
        length //= 2
    for amount in amounts:
        avg_img(x, y, directory, output = f"{output}{amount}", limit = amount)
    
    
    
