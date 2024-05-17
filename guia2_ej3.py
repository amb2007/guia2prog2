import pyperclip, requests, webbrowser, sys
from bs4 import BeautifulSoup

paste = pyperclip.paste()

while True:
    folder = pyperclip.paste()
    if folder != paste :
        print(folder)
        break
data = requests.get(folder)
soup = BeautifulSoup(data.text, 'html.parser')
nums = soup.find_all( 'a',  href=True)
res = []
for tag in nums:
    res.append(tag.get("href"))
print(res)

#for tag in tags:
    #print('____________________________________________________________________')
    #print(tag.gets("href"))

    #href = tag.get("href")
    #print(href)
