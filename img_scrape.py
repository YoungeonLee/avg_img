import requests
from bs4 import BeautifulSoup
import os
import shutil
import time

######this method repeats the same images after x amount of images######
######for more data use the google_img_scrape######

def scrape(keyword = 'photography', num_imgs = 50, directory = "images", warn = True):
    """searches 'keyword' in google images and downloads
        'num_imgs(int)' images to 'directory'"""
    if warn:
        user = input(f"Warning!!! All files in the directory '{directory}' will be deleted \
if you still wish to proceed, type 'yes'")
        if user.lower() != 'yes':
            raise Exception

    # if the directory exists
    if os.path.isdir(directory):
        # delete all files in the 'directory'
        # by deleting the folder
        shutil.rmtree(directory)
        # take a quick break to prevent error
        time.sleep(0.2)
    # adding the folder
    os.mkdir(directory)
    
    # counter to name the image
    counter = 0
    # link to the google image search
    link = f'https://www.google.com/search?q={keyword}&tbm=isch'
    print(f"Getting images for {keyword}")
        
    for i in range(num_imgs//20+1):
        # get the page using request
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # find all images except google logo on the page
        imgs_html = soup.find_all('img')[1:]

        # save all images in images directory
        for html in imgs_html:
            url = html['src']
            img = requests.get(url, allow_redirects=True)     
            with open(f"{directory}/{counter}.jpg", 'wb') as f:
                f.write(img.content)
            counter += 1
            # return if number of images reached the goal
            if counter == num_imgs:
                return
        print(f"{counter} images downloaded")
        # next_link
        next_link = soup.find_all('a', {'class':'frGj1b'})[0]['href']
        link = f"https://www.google.com{next_link}"
    print("Finished downloading!")

