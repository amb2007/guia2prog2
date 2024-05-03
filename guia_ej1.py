import pyperclip, requests, webbrowser


paste = pyperclip.paste()
while True:
    folder = pyperclip.paste()
    if paste != folder :
        print(folder)
    break
data = requests.get(folder)
file = open('ej1.txt', 'wb')
for chunk in data.iter_content(1000):
    file.write(chunk[:100])