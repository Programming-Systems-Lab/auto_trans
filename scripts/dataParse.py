from bs4 import BeautifulSoup
import urllib2
import argparse
import os.path

def downloader(url, path):
    html = urllib2.urlopen(url)
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
        with open(os.path.join(path, "code%s.zip" % (i + 1)), "wb") as code:
            code.write(test)

    print "Done"

def main():
    parser = argparse.ArgumentParser(description = "Download some files.")
    parser.add_argument('-i', "--url", help = 'Input the URL to download links from')
    parser.add_argument('-o', "--path", help = 'Input the directory to store the files')
    args = parser.parse_args()
    downloader(args.url, args.path)

if __name__ == '__main__':
    main()



