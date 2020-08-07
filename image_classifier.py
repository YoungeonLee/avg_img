from sklearn.cluster import AffinityPropagation
from sklearn import preprocessing
import numpy as np
from PIL import Image
import os
from shutil import copy2, rmtree
from avg_img import avg_img
import time

def collect_data(x=100, y=100, directory = 'avg_img_data'):
    directory = os.path.join('avg_img_data', 'images')
    print("collecting data")
    # master data
    X = []
    names = []
    # go through all images in a directory
    for filename in os.listdir(directory):
        # load each image
        try:
            img = Image.open(f'{directory}/{filename}').convert("RGB")
        except Exception as e:
            print(e)
            print(f"Unable to open {filename}")
            continue

        # resize image to match size
        img_resized = img.resize((x,y))
        # turns image to numpy array
        img_data = np.asarray(img_resized)
        # turn the data into 1d
        img_master = []
        for i in range(len(img_data)):
            for j in range(len(img_data[i])):
                for k in range(len(img_data[i][j])):
                    img_master.append(img_data[i][j][k])
        # put it in in the master data
        X.append(img_master)
        names.append(filename)
    return (X, names)

def classify_data(X):
    print("classifying data")
    # preprocess data
    X = np.array(X)
    global X_scaled
    X_scaled = preprocessing.scale(X)
    global clustering
    clustering = AffinityPropagation().fit(X_scaled)
    return clustering.labels_

def classify_to_directories(classified, directory = 'avg_img_data'):
    print("copying files to directories")
    class_directory = os.path.join(directory, 'classified')
    if os.path.isdir(class_directory):
            # delete all files in the 'directory'
            # by deleting the folder
            rmtree(class_directory)
            # take a quick break to prevent error
            time.sleep(0.1)
    os.mkdir(class_directory)
    for key in classified:
        #make directory for the key
        # if the directory exists
        key_directory = os.path.join(class_directory, str(key))
        # adding the folder
        os.mkdir(key_directory)
        # copy files to new directory
        for img in classified[key]:
            copy2(f'{os.path.join(directory, "images", img)}', f"{key_directory}")
            print(f"copied {img} to {key_directory}")
        avg_img(1080,1080, key_directory, key_directory)
        
        
    
def classify_images(x = 64, y=64, directory= 'avg_img_data'):
    # read in data
    global data
    global names
    (data, names) = collect_data(x,y,directory)
    # classify data
    labels = classify_data(data)
    global classified
    classified = {}
    for i in range(len(labels)):
        label = labels[i]
        if label in classified:
            classified[label].append(names[i])
        else:
            classified[label] = [names[i]]

    
    classify_to_directories(classified, directory)
            
    print("finished")






    
