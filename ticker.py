import urllib2
import json
import time

class ticker(object):

	def __init__(self):
		ticker_dictionary = self.__downloadTicker()
		self.__decodeTickerDictionary(ticker_dictionary)


	def __downloadTicker(self):
		raw_ticker = urllib2.urlopen('https://btc-e.com/api/2/ltc_usd/ticker').read()
		decoded_ticker = json.loads(raw_ticker)
		return decoded_ticker

	def __decodeTickerDictionary(self, ticker_dictionary):	
		self.sell = float(ticker_dictionary['ticker']['sell'])
		self.buy = float(ticker_dictionary['ticker']['buy'])
		self.last = float(ticker_dictionary['ticker']['last'])
		self.vol = float(ticker_dictionary['ticker']['vol'])
		self.vol_cur = float(ticker_dictionary['ticker']['vol_cur'])
		self.high = float(ticker_dictionary['ticker']['high'])
		self.low = float(ticker_dictionary['ticker']['low'])
		self.avg = float(ticker_dictionary['ticker']['avg'])
		self.server_time = time.gmtime(ticker_dictionary['ticker']['server_time'])
		self.updated = time.gmtime(ticker_dictionary['ticker']['updated'])

	def getHigh(self):
		return self.high

	def getLow(self):
		return self.low

	def getAverage(self):
		return self.avg

	def getLast(self):
		return self.last
		