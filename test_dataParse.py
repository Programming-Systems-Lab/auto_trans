from bs4 import BeautifulSoup
import urllib2
import os.path
import unittest

class TestDownloader(unittest.TestCase):
    def test_downloader_success(self):
        html = urllib2.urlopen("https://www.go-hero.net/jam/14/solutions/2/3/C%23")
        soup = BeautifulSoup(html, "html.parser")
        links = dict()

        problem_year = str(soup.find("title"))[
                       str(soup.find("title")).index('(2') + 1:str(soup.find("title")).index('(') + 5]
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
                filename = "%s-%s-%s-%s-%s.zip" % (
                problem_year, problem_round, problem_id, link.get('title')[21:], problem_language)
                links[filename] = href

        count = 1
        for i in links:
            print "Downloading: %s/%s" % (count, len(links))
            count += 1
            response = urllib2.urlopen(links[i])
            test = response.read()
            with open(os.path.join("/Users/Winston/Desktop/asdfasdf", i), "wb") as code:
                code.write(test)
        files = len(os.walk("/Users/Winston/Desktop/asdfasdf").next()[2]) - 1

        self.assertEqual(files, len(links))

def main():
    TestDownloader()

if __name__ == '__main__':
    unittest.main()
