import urllib2
import unittest

class BasicTest(unittest.TestCase):
    def test_downloader_success(self):
        url = urllib2.urlopen("https://www.google.com")
        print url
        self.assertEqual(1, 1)

def main():
    BasicTest()

if __name__ == '__main__':
    unittest.main()
