import unittest
from itemisedBill import readingCSV, creatingDictionaryList

class Mytest(unittest.TestCase):
  def test_readingCSV(self):
    data = readingCSV()
    self.assertEqual(data[0][0], '01/10/2015')
    self.assertEqual(data[0][1], 'MTN')
    self.assertEqual(data[0][2], '0832401145')
    self.assertEqual(data[0][3], '00h05m34s')

  def test_creatingDictionaryList(self):
    data = readingCSV()
    results = creatingDictionaryList(data)
    self.assertEqual(results[1]['Date'], '01/10/2015')
    self.assertEqual(results[1]['Provider'], 'MTN')
    self.assertEqual(results[1]['Number'], '0838758090')
    self.assertEqual(results[1]['Duration'], '00h01m34s')

if __name__ == '__main__':
  unittest.main()
