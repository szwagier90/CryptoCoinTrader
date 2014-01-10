import unittest
import stockHistory

class TickerTest(unittest.TestCase):

    def test_htmlDownload(self):
        history = stockHistory.stockHistory()
        html = history.getHtml('http://www.cryptocoincharts.info/period-charts.php?period=5-days&resolution=hour&pair=ltc-usd&market=btc-e')
        self.assertIsInstance(html, str)


if __name__ == '__main__':
    unittest.main()