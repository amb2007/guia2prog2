import requests
from bs4 import BeautifulSoup
import os
request = requests.get("https://dribbble.com/tags/image-gallery")
request.raise_for_status()
if request.status_code == 200:
    soup = BeautifulSoup(request.text, 'html.parser')
    
    if not os.path.exists('Imagenes'):
        os.makedirs('Imagenes')
    os.chdir('Imagenes')
    imageList = filter(lambda x: (x.get('src') != None) and ("https" in x.get('src')), soup.find_all('img', limit=None))
    
    for img in imageList:

        imgSrc = img.get('src').split("?")[0]

        print(imgSrc)
        res = requests.get(imgSrc.split("?")[0])
        res.raise_for_status()
        
        imageFile = open(os.path.join(imgSrc.split("/")[-1]), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        del res