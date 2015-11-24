import unittest
from itemisedBill import readingCSV

class Mytest(unittest.TestCase):
  def test_readingCSV(self):
    readcsv = readingCSV()
    self.assertEqual(readcsv[1][0], '01/10/2015')
    self.assertEqual(readcsv[1][1], 'MTN')
    self.assertEqual(readcsv[1][2], '0832401145')
    self.assertEqual(readcsv[1][3], '00h05m34s')

if __name__ == '__main__':
  unittest.main()
