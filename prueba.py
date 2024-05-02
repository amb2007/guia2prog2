import webbrowser,requests
data = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
file = open('romeo.txt', 'wb')
for chunk in data.iter_content(1000):
    file.write(chunk[:100])
