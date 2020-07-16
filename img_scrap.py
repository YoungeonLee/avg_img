import requests
from bs4 import BeautifulSoup

# link to the google image search
keyword = 'photography'
link = f'https://www.google.com/search?q={keyword}&tbm=isch'

# get the page using request
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

# find all images except google logo on the page
imgs_html = soup.find_all('img')[1:]

# counter to name the image
counter = 0

# save all images in images directory
for html in imgs_html:
    url = html['src']
    img = requests.get(url, allow_redirects=True)     
    with open(f"images/{counter}.jpg", 'wb') as f:
        f.write(img.content)
    counter += 1
    
