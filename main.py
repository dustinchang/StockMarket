import sys
import random
from decimal import Decimal
import threading
import stock_pb2

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
    def __init__(self):
        """Stock Constructor"""
        self.StockID = ''
        self.StockName = ''
        self.StockOpen = 0.0
        self.StockNetChange = 0.0
        self.StockChange = 0.0
        self.StockDayRange = ''
        self.StockVolume = 0
        self.StockPreviousClose = 0.0
        self.Stock52WKRange = ''
        self.Stock1YRReturn = 0.0
        self.StockYTDReturn = 0.0
        self.StockPERatio = 0.0
        self.StockEarningsPS = 0.0
        self.StockMarketCap = 0.0
        self.StockSharesOutdanding = 0.0
        self.StockPrice = 0.0
        self.StockDividend = 0.0
        self.StockSector = ''
        self.StockIndustry = ''
        self.StockSubIndustry = ''

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
   percent_rise = round(random.uniform(0.01, 0.1), 2)
   print 'percent_rise: ' + str(percent_rise)
   print 'Stock Price: ' + str(stk.StockPrice)
   stk.StockPrice += round(stk.StockPrice * percent_rise, 2)
   print 'Stock Price Increased to: ' + str(stk.StockPrice)
###def rise(stk, stock_list):
###    percent_rise = round(random.uniform(0.01, 0.1), 2)
###    print 'percent_rise: ' + str(percent_rise)
###    print 'Stock Price: ' + str(stk.StockPrice)
###    stk.StockPrice += round(stk.StockPrice * percent_rise, 2)
###    stk_temp = stk.StockPrice
###    del stock_list.stock[-1]
###    stock_list.stock.add().StockPrice = stk_temp
###    print 'Stock Price Increased to: ' + str(stk.StockPrice)
###    return stk


##Takes a stock and a stock_list as parameters and
# implements a drop in the stock
#
def drop(stk):
   percent_drop = round(random.uniform(0.01, 0.1), 2)
   print 'percent_drop: ' + str(percent_drop)
   print 'Stock Price: ' + str(stk.StockPrice)
   stk.StockPrice -= round(stk.StockPrice * percent_drop, 2)
   print 'Stock Price Decreased to:' + str(stk.StockPrice)
###def drop(stk, stock_list):
###    percent_drop = round(random.uniform(0.01, 0.1), 2)
###    print 'percent_drop: ' + str(percent_drop)
###    print 'Stock Price: ' + str(stk.StockPrice)
###    stk.StockPrice -= round(stk.StockPrice * percent_drop, 2)
###    stk_temp = stk.StockPrice
###    del stock_list.stock[-1]
###    stock_list.stock.add().StockPrice = stk_temp
###    print 'Stock Price Decreased to:' + str(stk.StockPrice)
###    return stk
    #f.write('Stock Price Decreased to:'+str(stk.StockPrice)+'\n')

##To calculate the frequency that the stock should fluctuate
# and determine the status of what the stock should do at each fluctuation stage
#
def fluctuate(stk, stock_list):
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

##Execution start of program, adding to protocol buffers
#
#
def main():
    s = Stock()
    rise(s)
    print s.StockPrice


    stock_list = stock_pb2.StockList()

    # Read existing address book
    try:
        f = open('client1.bin', 'rb')
        stock_list.ParseFromString(f.read())
        f.close()
    except IOError:
        print 'Could not open file: client1.bin'

    while True:
        choice = raw_input('What would you like to do?\n\tAdd a stock (1)\n\tView stocks (2)\n\tExit (3)\nInput: ')
        if choice == '1':
            # Create a stock
            print 'Adding stock...'
            stk = stock_list.stock.add()
            stk.StockID = raw_input('Stock ID: ')
            stk.StockName = raw_input('Stock name: ')
            stk.StockPrice = float(raw_input('Stock price: '))

            f = open('client1.bin', "wb")
            f.write(stock_list.SerializeToString())
            f.close()
        elif choice == '2':
            for stock in stock_list.stock:
                print 'Stock ID: ', stock.StockID
                print 'Stock Name: ', stock.StockName
                print 'Stock Price: ', str(stock.StockPrice)
        else:
            break

    # later functionality
    # Simulate fluctuations for stock
    # for x in range(10):
    #    fluctuate(client1, stock_list)

    f = open('client1.bin', 'wb')
    f.write(stock_list.SerializeToString())

if __name__ == "__main__":
    main()
