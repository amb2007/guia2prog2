
import pyperclip, requests, webbrowser, sys,os
from bs4 import BeautifulSoup

paste = pyperclip.paste()

while True:
    folder = pyperclip.paste()
    if folder != paste :
        print(folder)
        break
if not os.path.exists('Imagenes'):
    os.makedirs('Imagenes')
os.chdir('Imagenes')

data = requests.get(folder)
soup = BeautifulSoup(data.text, 'html.parser')
p = soup.find('p', 'a', href= True)
print(p)
file = open('pdfs', 'wb')