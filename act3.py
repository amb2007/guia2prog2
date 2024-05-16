import pyperclip, requests, webbrowser
from bs4 import BeautifulSoup

paste = pyperclip.paste()

while True:
    folder = pyperclip.paste()
    if folder != paste :
        print(folder)
        break
data = requests.get(folder)
soup = BeautifulSoup(data.text, 'html.parser')
nums = soup.find_all('div', {'class': "c-listing__pagination"})
nums2 = soup.find_all('a')
nums3 = soup.find_all('href')
print(nums3)
