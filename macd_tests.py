import unittest
import macd

class MACDTest(unittest.TestCase):

    def setUp(self):
        self.numbers = [2.0, 4.0, 10.0, 16.0, 20.0, 12.0]
        
    def test_ExponentialMovingAverage_listLength(self):
        EMA = macd.exponentialMovingAverage(self.numbers, 4)
        self.assertEqual(len(self.numbers), len(EMA))
        
    def test_ExponentialMovingAverage(self):
        EMA = macd.exponentialMovingAverage(self.numbers, 4)
        self.assertEqual(EMA[0], None)
        self.assertEqual(EMA[1], None)
        self.assertEqual(EMA[2], None)
        self.assertAlmostEqual(EMA[3], 8)
        self.assertAlmostEqual(EMA[4], 12.8)
        self.assertAlmostEqual(EMA[5], 12.48)

#    def test_macd(self):
#        numbers = [2.0, 6.0, 10.0, 11.0, 13.0, 10.0]
#        macd_numbers = macd.calulateMacd(numbers, 5, 4, 2)

if __name__ == '__main__':
    unittest.main()

#
#def ema(s, n):
#    """
#    returns an n period exponential moving average for
#    the time series s
#
#    s is a list ordered from oldest (index 0) to most
#    recent (index -1)
#    n is an integer
#
#    returns a numeric array of the exponential
#    moving average
#    """
#    s = array(s)
#    ema = []
#    j = 1
#
#    #get n sma first and calculate the next n period ema
#    sma = sum(s[:n]) / n
#    multiplier = 2 / float(1 + n)
#    ema.append(sma)
#
#    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
#    ema.append(( (s[n] - sma) * multiplier) + sma)
#
#    #now calculate the rest of the values
#    for i in s[n+1:]:
#        tmp = ( (i - ema[j]) * multiplier) + ema[j]
#        j = j + 1
#        ema.append(tmp)
#
#    return ema