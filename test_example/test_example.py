import sys
import unittest
import example

class TestExample(unittest.TestCase):
  def test_add(self):
    self.assertEqual(example.add(3, 5), 8)

if __name__ == '__main__':
  unittest.main()
