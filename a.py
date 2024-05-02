from bs4 import BeautifulSoup
import requests
import webbrowser
url = 'https://www.cartoonstock.com/directory/n/nerd.asp'
request = requests.get(url)
def DescargrImgs(url):
    sopa = BeautifulSoup('response.txt', 'html.parser')
    img_tags = sopa.find_all('img')
    if not os.path.exist('imagenes'):
        os.makedirs('imagenes')
    for img in img_tags :
        img_url = img['src']
        img_response = request.get(img_url)
        
        if img_response.status_code == 200:
            img_filename= os.path.oin('imgs', os.path.basename(img_url))
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f'imagen descargada {img_filename}')
        else:
            print(f'error al descargar la img {img_url}')