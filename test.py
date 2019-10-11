from urllib.request import urlopen
html = []
with urlopen("https://docs.python.org/3/howto/urllib2.html") as response:
    for line in response:
        line_words = line.decode('utf-8')
        html.append(line_words)
for line in html:
    print(line)




