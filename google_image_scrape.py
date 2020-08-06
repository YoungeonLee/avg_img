from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import os
import shutil

def download(url, save_name):
    """download a image from url and save it to 'save_name'.jpg"""
    try:
        img = requests.get(url, allow_redirects=True)
        with open(f"{save_name}.jpg", 'wb') as f:
            f.write(img.content)
    except:
        print(f"Download failed for {save_name}")
        print(f"Failed URL: {url}")

def clean_up_directory():
    """clean up the 'directory'"""
    directory = 'avg_img_data'
    # if the directory exists
    if os.path.isdir(directory):
        # delete all files in the 'directory'
        # by deleting the folder
        shutil.rmtree(directory)
        # take a quick break to prevent error
        time.sleep(0.1)
    # adding the folder
    os.mkdir(directory)
    os.mkdir(os.path.join(directory, 'images'))


def download_images(driver, num_images, wait_time):
    directory = os.path.join('avg_img_data', 'images')
    """download the images from the browser"""
    # text that shows the end of the page
    end = driver.find_element_by_class_name('Yu2Dnd')
    # button to load more images
    show_more = driver.find_element_by_class_name('mye4qd')
    counter = 0
    i = 0
    # until all images are downloaded
    while True:
        # find all images
        imgs = driver.find_elements_by_class_name('rg_i')
        # loop until need to scroll
        while True:
            # pick a image
            try:
                img = imgs[i]
            # no more images to load -> return
            except IndexError:
                print("There are not enough images on the search")
                print(f"Only {counter} images are found")
                driver.quit()
                return
            # click the image
            try:
                ActionChains(driver).move_to_element(img).click(img).perform()
            except Exception as e:
                print(e)
                time.sleep(1)
                imgs = driver.find_elements_by_class_name('rg_i')
                img = imgs[i]
                try:
                    ActionChains(driver).move_to_element(img).click(img).perform()
                except Exception as e:
                    print(e)
                    print(f'{img} is not clickable for some reason')
                    break
                    
                
            # timer
            start_time = time.time()
            # loop until image is downloadable or timeout
            while True:
                # looks for enlarged image
                html = driver.find_elements_by_class_name('n3VNCb')
                # get the link for the image
                try:
                    if i == 0:
                        src = html[0].get_attribute('src')
                    else:
                        src = html[1].get_attribute('src')
                except Exception as e:
                    print(e)
                    print(html)
                    print(len(html))
                    break
                        
                # make sure the image is a link
                if 'http' == src[:4]:
                    #download image
                    download(src, f"{directory}/{counter}")
                    print(f"image saved as {counter}.jpg in {directory}")
                    counter += 1
                    if counter == num_images:
                        # end the scrape if enough images are gathered
                        driver.quit()
                        return
                    break
                # if it takes longer than the 'wait_time' for the image, move on to next
                taking = time.time() - start_time
                if taking > wait_time:
                    print(f"this image is not downloadable: {html[1].get_attribute('alt')}")
                    break
            i += 1
            # if all images are used -> scroll down
            if i == len(imgs):
                if show_more.is_displayed():
                    show_more.click()
                    time.sleep(1)
                #scroll
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                break



# chromedriver.exe needs to be in python's 'path'

def scrape(keyword = 'photography', num_images = 100, wait_time = 1):
    """scrapes 'n' images by searching 'keyword' on google images
        saves the images in 'directory'
        waits for 'wait_time' for images to load
        if the image does not load, move on to next"""


    # if the directory exists
    clean_up_directory()

    # turn on google chrome browser     
    driver = webdriver.Chrome()
    driver.implicitly_wait(wait_time)

    # search images
    driver.get(f"https://www.google.com/search?q={keyword}&tbm=isch")

    # list of images on the page

    print("Hunting for images...")
    download_images(driver, num_images, wait_time)
    
    
