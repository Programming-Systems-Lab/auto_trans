from bs4 import BeautifulSoup
import urllib2

html = urllib2.urlopen("https://www.go-hero.net/jam/14/solutions/3/1/Java") #Change the URL
soup = BeautifulSoup(html, "html.parser")
links = []
for link in soup.find_all('a'):
    if link.get('href')[:7] == "http://":
        links.append(link.get('href'))

for i in range(len(links)):
    print "Downloading: %s/%s" % (i + 1, len(links))
    temp = str(links[i])
    response = urllib2.urlopen(temp)
    test = response.read()
    with open("code%s.zip"% (i), "wb") as code:
        code.write(test)

print "Done"



