from bs4 import BeautifulSoup
import urllib2
import argparse
import os.path

def downloader(url, path):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    links = dict()

    problem_year = str(soup.find("title"))[str(soup.find("title")).index('(2') + 1:str(soup.find("title")).index('(') + 5]
    problem_round = ""
    problem_language = ""
    problem_id = ""
    count = 0

    for link in soup.find_all('a'):
        href = link.get('href')
        if link.parent.get('id') == 'navbar-current':
            problem_round = link.string
            count += 1
        if href[:10] == "languages/":
            problem_language = href[10:]
            count += 1
        if href[:9] == "problems/":
            problem_id = href[len(href) - 1:]
            count += 1
        if count == 3:
            break

    for link in soup.find_all('a'):
        href = link.get('href')
        if href[:7] == "http://" and link.get('title')[:20] == "Download solution by":
            filename = "%s-%s-%s-%s-%s.zip" % (problem_year, problem_round, problem_id, link.get('title')[21:], problem_language)
            links[filename] = href

    count = 1
    for i in links:
        print "Downloading: %s/%s" % (count, len(links))
        count += 1
        response = urllib2.urlopen(links[i])
        test = response.read()
        with open(os.path.join(path, i), "wb") as code:
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
