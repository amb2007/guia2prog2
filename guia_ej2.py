import pyperclip
paste = pyperclip.paste()
while True:
    valor = pyperclip.paste()
    if paste != valor:
        print(valor)
        break