import unittest
import ticker

class TickerTest(unittest.TestCase):

    def setUp(self):
        self.t = ticker.ticker()

    def test_object(self):
        high = self.t.getHigh()
        self.assertIsInstance(high, float)
        low = self.t.getLow()
        self.assertIsInstance(low, float)
        avg = self.t.getAverage()
        self.assertIsInstance(avg, float)

    def test_average(self):
        high = self.t.getHigh()
        low = self.t.getLow()
        avg = self.t.getAverage()
        self.assertEqual(avg, (high+low)/2)


if __name__ == '__main__':
    unittest.main()