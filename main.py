import datetime, time
from decimal import Decimal
from googlefinance import getQuotes
import cPickle as pickle
import random
import sys
import urllib

"""
Implementation of a stock market exchange where stocks are continually on the rise or dropping.
This program will assist on whether you should purchase or sell stocks.
"""

class Index:
    """Investment information about an Index, which is a portion of a stock market"""
    def __init__(self):
        """Index Constructor"""
        self.IndexID = ''
        self.IndexName = ''
        self.IndexValue = 0.0
        self.IndexNetChange = 0.0
        self.IndexChange = 0.0
        self.IndexOpen  = 0.0
        self.IndexDayRange = ''
        self.IndexPreviousClose = 0.0
        self.Index52WKRange = ''
        self.Index1YRReturn = 0.0
        self.IndexYTDReturn = 0.0
        self.IndexTotalMembers = 0
        self.IndexMembersUp = 0
        self.IndexMembersDown = 0

class Stock:
    """Details of a Stock and it's contents"""
    def __init__(self, symb, day, price, open_ = 0.0, high = 0.0, low = 0.0, close = 0.0, volume = 0.0):
        """Stock Constructor"""
        self.StockID = symb
        #self.StockName = ''
        self.StockDate = day
        self.StockOpen = open_
        #self.StockNetChange = 0.0
        #self.StockChange = 0.0
        self.StockDayRange = str(low) + ' - ' + str(high)
        self.StockVolume = volume
        self.StockClose = close
        #self.StockPreviousClose = 0.0
        #self.Stock52WKRange = ''
        #self.Stock1YRReturn = 0.0
        #self.StockYTDReturn = 0.0
        #self.StockPERatio = 0.0
        #self.StockEarningsPS = 0.0
        #self.StockMarketCap = 0.0
        #self.StockSharesOutdanding = 0.0
        self.StockPrice = price
        #self.StockDividend = 0.0
        #self.StockSector = ''
        #self.StockIndustry = ''
        #self.StockSubIndustry = ''

    def print_hist_stock(self):
        dt = self.StockDate.strftime('%Y-%m-%d T: %H:%M:%S')
        print 'ID: ' + self.StockID + '\nDate: ' + dt + '\nOpen: ' + str(self.StockOpen)
        print 'Day Range: ' + self.StockDayRange + '\nClose: ' + str(self.StockClose) + '\nVolume: ' + str(self.StockVolume)

    def print_stock(self):
        dt = self.StockDate.strftime('%Y-%m-%d T: %H:%M:%S')
        print 'ID: ' + self.StockID + '\nDate: ' + dt
        print 'Last Trade Price: ' + self.StockPrice

class Broker:
    """Details of the identification of a Broker"""
    def __init__(self):
        """Broker Constructor"""
        self.BrokerID = ''
        self.BrokerName = ''
        self.BrokerFirmID = ''
        self.BrokerPLReport = 0.0
        self.BrokerTotalBudget = 0.0
        self.BrokerTotalStocks = 0
        self.BrokerBudget = {} #{ String : String : Float } (ClientID : StockID : Budget $)
        self.BrokerCommission = 0.0
        self.BrokerLicenseType = ''
        self.BrokerShares = {} #{ String: Float } (StockID and Quantity)

class Firm:
    """Organizational details of a Firm"""
    def __init__(self):
        """Firm Constructor"""
        self.FirmID = ''
        self.FirmName = ''
        self.FirmBudget = 0.0
        self.FirmType = ''
        self.FirmTotalBrokers = 0

class Client:
    """Personal details of an investing Client"""
    def __init__(self):
        """Client Constructor"""
        self.ClientID = ''
        self.ClientName = ''
        self.ClientPhoneNumber = 0
        self.ClientEmailAddress = ''
        self.ClientBudget = 0.0
        self.ClientShares = {} #{ String : Float : String } (StockID : Quantity : Can Exercise)
        self.ClientFirmID = '' #Maybe int
        self.ClientBrokerID = '' #Maybe int
        self.ClientPLReport = 0.0
        self.ClientIndsutry = []

class Exchange:
    """Contains the details of wanted market exchanges"""
    def __init__(self):
        """Exchange Constructor"""
        self.ExchangeID = ''
        self.ExchangeName = ''
        self.ExchangeHQ = ''
        self.ExchangeEconomy = ''
        self.ExchangeTimeZone = ''
        self.ExchangeVolume = 0
        self.ExchangeNetChange = 0.0
        self.ExchangeChange = 0.0
        self.ExchangeOpen = 0.0
        self.ExchangeDayRange = ''
        self.ExchangePreviousClose = 0.0
        self.Exchange52WKRange = ''
        self.Exchange1YRReturn = 0.0
        self.ExchangeYTDReturn = 0.0

class Transaction:
    """Specifics of a trading Transaction"""
    def __init__(self):
        """Transaction Constructor"""
        self.TransactionID = ''
        self.TransactionTime = {} #{Integer:Integer} Maybe use datetime for this
        self.TransactionBuyer = '' #(ClientID BrokerID FirmID)
        self.TransactionSeller = '' #(ClientID BrokerID FirmID)
        self.TransactionTrader = '' #(ClientID BrokerID FirmID)
        self.TransactionType = '' #(Sell Buy Trade)
        self.TransactionPLReport = {} #String : Float (only when it's a sell or trade)
        self.TransactionBSVolume = {} #String : Integer : Float (StockID : Volume : Price)
        self.TransactionTradeVolume = {} #{stock traded <> stock gained}
                                         #{String : Integer : Float <> String : Integer : Float }
                                         #StockID : Volume : Price <> StockID : Volume : Price
        self.TransactionExchange = ''

##Takes a stock and a stock_list as parameters and
# implements a rise in the stock
#
def rise(stk):
	# if the stock rise buy otherwise not buy or sell
	currentPrice = stk.StockPrice
	lastPrice = 
   percent_rise = round(random.uniform(0.01, 0.1), 2)
   print 'percent_rise: ' + str(percent_rise)
   print 'Stock Price: ' + str(stk.StockPrice)
   stk.StockPrice += round(stk.StockPrice * percent_rise, 2)
   print 'Stock Price Increased to: ' + str(stk.StockPrice)


##Takes a stock and a stock_list as parameters and
# implements a drop in the stock
#
def drop(stk):
   percent_drop = round(random.uniform(0.01, 0.1), 2)
   print 'percent_drop: ' + str(percent_drop)
   print 'Stock Price: ' + str(stk.StockPrice)
   stk.StockPrice -= round(stk.StockPrice * percent_drop, 2)
   print 'Stock Price Decreased to:' + str(stk.StockPrice)

##To calculate the frequency that the stock should fluctuate
# and determine the status of what the stock should do at each fluctuation stage
#
def fluctuate(stk):
    print '~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~'
    stat = random.randint(0, 100)
    print 'Current Stock Status: ' + str(stat)
    if stat < 10:
        print 'Stock should be sold or buy more'
    elif stat % 2 == 0 and stat % 3 == 0 and stat % 5 == 0:
        print 'divisible by 2 and 3 and 5'
    elif stat % 2 == 0 and stat % 3 == 0:
        print 'divisible by 2 and 3'
    elif stat % 2 == 0 and stat % 5 == 0:
        print 'divisible by 2 and 5'
    elif stat % 3 == 0 and stat % 5 == 0:
        print 'divisible by 3 and 5'
    elif stat % 2 == 0:
        print 'divisible by 2'
        rise(stk)
    elif stat % 3 == 0:
        print 'divisible by 3'
        drop(stk)
    elif stat % 5 == 0:
        print 'divisible by 5'
    else:
        print 'prime'

"""
## Get historical stock data
#  - retrieves one quote a day
#  Use for last 30 days?
def get_historical(symb, number_of_days):
    today = datetime.date.today()
    start = (today - datetime.timedelta(days=number_of_days))
    # Outputs historical data into csv format (only output available)
    url_string = "http://www.google.com/finance/historical?q={0}".format(symb)
    url_string += "&startdate={0}&enddate={1}&output=csv".format(
        start.strftime('%b %d, %Y'),today.strftime('%b %d, %Y'))
    csv = urllib.urlopen(url_string).readlines()
    # Put header information at end; dont need it
    csv.reverse()

    # Put stocks into a list called 'histo'
    histo = []
    for day in xrange(0, len(csv) - 1): # -1 because last element is header
      ds,open_,high,low,close,volume = csv[day].rstrip().split(',')
      open_,high,low,close = [float(x) for x in [open_,high,low,close]]
      dt = datetime.datetime.strptime(ds, '%d-%b-%y')
      histo.append(Stock(symb, dt, open_, open_, high, low, close, volume))

    return histo
"""

def get_historical(symb, number_of_days):
    today = datetime.date.today()
    start = (today - datetime.timedelta(days=number_of_days)).strftime('%Y%m%d')
    today = int(time.mktime(datetime.datetime.strptime(start, '%Y%m%d').timetuple()))
    period = number_of_days
    interval = 61
    url_string = "http://www.google.com/finance/getprices?q={0}&i={1}&p={2}d&ts={3}".format(symb, interval, period, today)

    ticks = urllib.urlopen(url_string).readlines()[7:]
    values = [tick.split(',') for tick in ticks]

    data = []
    for value in values:
        dt = datetime.datetime.fromtimestamp(float(value[0][1:].strip())) # time in unix epoch format convert to datetime
        data.append(Stock(symb,
                          dt,
                          value[4].strip(),
                          value[4].strip(), # open; repeat cause python classes suck
                          value[2].strip(), # high
                          value[3].strip(), # low
                          value[1].strip(), # close
                          value[5].strip())) # volume
    return data


## Get current stock data
#  example:
#    quotes = getQuotes('AAPL')
#    return:
#    [{u'Index': u'NASDAQ',
#      u'LastTradeWithCurrency': u'129.09',
#      u'LastTradeDateTime': u'2015-03-02T16:04:29Z',
#      u'LastTradePrice': u'129.09',
#      u'Yield': u'1.46',
#      u'LastTradeTime': u'4:04PM EST',
#      u'LastTradeDateTimeLong': u'Mar 2, 4:04PM EST',
#      u'Dividend': u'0.47',
#      u'StockSymbol': u'AAPL',
#      u'ID': u'22144'}]
#
#   multiple quotes use getQuotes(['AAPL', 'GOOG'])
def get_current(symb):
    quote = getQuotes(symb)
    # Date
    dt = datetime.datetime.strptime(quote[0][u'LastTradeDateTime'], '%Y-%m-%dT%H:%M:%SZ')
    stock = Stock(quote[0][u'StockSymbol'], dt, quote[0][u'LastTradePrice'])
    return stock

##
#
#
def transaction(user, stock):
    pass


def close_prices(symblist):
    stock_objs = []
    close_list = []
    stk_tracker = 0
    for ticker in symblist:
        stock_objs.append(get_historical(ticker, 1))
    for stk_list in stock_objs:
        close_list.append([stk_list[0].StockID])
        for stk in stk_list:
            close_list[stk_tracker].append(stk.StockClose)
        stk_tracker += 1
    close_list[0].append('hellow')
    #print close_list
    return close_list

##Execution start of program, adding to protocol buffers
#
#
def main():
    """
    # create initial stocklist file with 7 day sample
    histo = get_historical('GOOG', 30)
    stock_list = {'GOOG':histo}
    pickle.dump(stock_list, open("stocklist.p", "wb"))
    """

    symblist = {'GOOG' : 'Alphabet Inc.', 'AAPL' : 'Apple Inc.', 'NFLX' : 'Netflix, Inc.', 'AMZN' : 'Amazon.com, Inc.', 'TSLA' : 'Tesla Motors Inc'}
    ticker_list = {'Alphabet Inc.' : 'GOOG', 'Apple Inc.' : 'AAPL', 'Netflix, Inc.' : 'NFLX', 'Amazon.com, Inc.' : 'AMZN', 'Tesla Motors Inc' : 'TSLA'}

    # read from stock list file
    # stock_list = pickle.load(open('stocklist.p', 'rb'))

    #histo = get_historical('GOOG', 30)
    #for s in histo:
    #    s.print_hist_stock()

    #Get all the closing prices
    close_prices_list = close_prices(symblist)
    #print close_prices_list

    # get historical data on all stocks indicated in symbol list
    quotelist = []
    for key in symblist:
        quotelist.append(get_historical(key, 1))

    #Prints out the historical data that was grabbed from above for loop
    #day = get_historical('GOOG', 5)
    ###for symb in quotelist:
    ###    for quote in symb:
    ###        quote.print_hist_stock()

    #stock = get_current('GOOG')
    #stock.print_stock()

    # save state of stock list into file
    #pickle.dump(stock_list, open("stocklist.p", "wb"))

if __name__ == "__main__":
    main()
