import argparse
import zipfile
import os

def zipper(directory, keep):
    if keep:
        for file in os.listdir(directory):
            if file.endswith(".zip"):
                zip_ref = zipfile.ZipFile("%s/%s" % (directory, file), 'r')
                zip_ref.extractall("%s/%s" % (directory, file[:len(file) - 4]))
                zip_ref.close()
    else:
        for file in os.listdir(directory):
            if file.endswith(".zip"):
                zip_ref = zipfile.ZipFile("%s/%s" % (directory, file), 'r')
                zip_ref.extractall("%s/%s" % (directory, file[:len(file) - 4]))
                zip_ref.close()
                os.remove("%s/%s" % (directory, file))


def main():
    parser = argparse.ArgumentParser(description = "Unzip some files")
    parser.add_argument('-i', "--directory", help = 'Input the directory of files to be unzipped')
    parser.add_argument('-z', "--keep", nargs = '?', help = 'Provide optional argument to keep unzipped files')
    args = parser.parse_args()
    zipper(args.directory, args.keep)

if __name__ == '__main__':
    main()