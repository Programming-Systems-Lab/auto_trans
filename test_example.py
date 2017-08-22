import sys
import os
import unittest
import test_example.example

class TestExample(unittest.TestCase):
  def test_add(self):
    self.assertEqual(test_example.example.add(3, 5), 8)

if __name__ == '__main__':
  unittest.main()
