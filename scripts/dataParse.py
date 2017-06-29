from bs4 import BeautifulSoup
import urllib2
import argparse
import os.path

def downloader(url, path):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    links = []

    #The way to identify if a href is downloadable is not rigorous
    #Need to analyze the title attribute
    #link.get('title').startswith('Download solution by')
    for link in soup.find_all('a'):
        if link.get('href')[:7] == "http://":
            links.append(link.get('href'))
    
    #The current naming is not meaningful
    #Use year-round-problem-id-username-language to form the file name
    #This can be done by analyzing the url and the title attribute
    #Instead of using list to contain all links, use a dict
    #links = dict(); links[key] = link
    #key will be the file name and the value is the link
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



