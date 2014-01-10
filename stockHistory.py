import urllib2
from bs4 import BeautifulSoup
import re
from datetime import datetime

class stockHistory(object):


    def __init__(self, url):
        self.TIME_REGEX = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2})h')
        self.url = url
        self.updateHistory()

    def updateHistory(self):
        self.history = []
        html = self.__getHtml()
        soup = BeautifulSoup(html)
        table = soup.tbody
        records = table.find_all('tr')
        for rec in records:
            fields = rec.find_all('td')

            history_tick = self.__parseFieldsToHistoryTick(fields)
            self.history.append(history_tick)

        return self.history

    def ticks(self):
        for tick in self.history:
            yield tick

    def __getHtml(self):
        html = urllib2.urlopen(self.url).read()
        return html

    def __parseFieldsToHistoryTick(self, fields):
        time_string = self.TIME_REGEX.search(fields[0].text)
        history_tick = {}

        history_tick['date'] = datetime(year=int(time_string.group('year')), month=int(time_string.group('month')), day=int(time_string.group('day')), hour=int(time_string.group('hour')))
        history_tick['low'] = self.__extractAndCheckCurrency(fields[1].text, 'USD')
        history_tick['high'] = self.__extractAndCheckCurrency(fields[2].text, 'USD')
        history_tick['open'] = self.__extractAndCheckCurrency(fields[3].text, 'USD')
        history_tick['close'] = self.__extractAndCheckCurrency(fields[4].text, 'USD')
        history_tick['volume'] = self.__extractAndCheckCurrency(fields[5].text, 'LTC')

        return history_tick

    def __extractAndCheckCurrency(self, string, currency):
        s = string.split(' ')
        if s[1] == currency:
            ret = s[0].replace(',', '')
            return float(ret)
        else:
            raise ValueError


#    def getNextTick(self):
#        if self.counter < len(self.ltc_history):
#            a = self.ltc_history[self.counter]
#            self.counter += 1
#            return a
#        else:
#            return None
#