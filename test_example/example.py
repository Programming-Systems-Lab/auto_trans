import sys

def add(v1, v2):
  return v1 + v2

def main():
  if len(sys.argv) != 3:
    print 'Invalid input argument: ' + str(len(sys.argv))
    print '# inputs should be 3'
    sys.exit(-1)

  v1 = int(sys.argv[1])
  v2 = int(sys.argv[2])
  result = add(v1, v2)
  print 'Result: ' + str(result)

if __name__ == '__main__':
  main()
