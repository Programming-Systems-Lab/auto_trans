import os
import zipfile
import unittest

class TestZipper(unittest.TestCase):
    def test_zipper_successful(self):
        for file in os.listdir("./"):
            if file.endswith(".zip"):
                zip_ref = zipfile.ZipFile("%s/%s" % ("./", file), 'r')
                zip_ref.extractall("%s/%s" % ("./", file[:len(file) - 4]))
                zip_ref.close()
                os.remove("%s/%s" % ("./", file))
        count = 0
        for file in os.listdir("./"):
            if file.endswith(".zip"):
                count += 1
        self.assertEqual(count, 0)

def main():
    TestZipper()

if __name__ == '__main__':
    unittest.main()
