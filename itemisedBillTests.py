import unittest
from itemisedBill import readingCSV, creatingDictionaryList, specifiedCallsForProvider

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
    self.assertEqual(results[11]['Date'], '10/10/2015')
    self.assertEqual(results[11]['Provider'], 'Vodacom')
    self.assertEqual(results[11]['Number'], '0828907600')
    self.assertEqual(results[11]['Duration'], '00h00h56ss')

  def test_specifiedCallsForProvider(self):
    csv = readingCSV()
    data = creatingDictionaryList(csv)
    results = specifiedCallsForProvider(data, 'MTN')
    self.assertEqual(results[15]['Date'], '27/10/2015')
    self.assertEqual(results[15]['Provider'], 'MTN')
    self.assertEqual(results[15]['Number'], '0831239023')
    self.assertEqual(results[15]['Duration'], '00h03m04s')

if __name__ == '__main__':
  unittest.main()
