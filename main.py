import sys
import random
from decimal import Decimal
import threading

class Index:
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        self.FirmID = ''
        self.FirmName = ''
        self.FirmBudget = 0.0
        self.FirmType = ''
        self.FirmTotalBrokers = 0

class Client:
    def __init__(self):
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

class Exhange:
    def __init__(self):
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
    def __init__(self):
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

def current_stock_status(stk, f):
    #threading.Timer(2.0, current_stock_status, [stk]).start()
    print '~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~'
    fluctuate(stk, f)
    stat = random.randint(0, 100)
    print 'Current Stock Status:'+str(stat)
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
        rise(stk, f)
    elif stat % 3 == 0:
        print 'divisible by 3'
        drop(stk, f)
    elif stat % 5 == 0:
        print 'divisible by 5'
    else:
        print 'prime'

def rise(stk, f):
    percent_rise = round(random.uniform(0.01, 0.1),2)
    print 'percent_rise:'+str(percent_rise)
    print 'stk.StockPrice='+str(stk.StockPrice)
    stk.StockPrice += round(stk.StockPrice*percent_rise,2)
    print 'Stock Price Increased to:'+str(stk.StockPrice)
    f.write('Stock Price Increased to:'+str(stk.StockPrice)+'\n')

def drop(stk, f):
    percent_drop = round(random.uniform(0.01, 0.1),2)
    print 'percent_drop:'+str(percent_drop)
    print 'stk.StockPrice='+str(stk.StockPrice)
    stk.StockPrice -= round(stk.StockPrice*percent_drop,2)
    print 'Stock Price Decreased to:'+str(stk.StockPrice)
    f.write('Stock Price Decreased to:'+str(stk.StockPrice)+'\n')

def fluctuate(stk, f):
    threading.Timer(2.0, current_stock_status, [stk, f]).start()

def main():
    client1 = Stock()
    open('client1.txt', 'a').close()    #If not there creates it for the StockPrice tracking
    f = open('client1.txt', 'a')
    client1.StockPrice = 100.22
    f.write('client1\nStarting Stock Price:'+str(client1.StockPrice)+'\n')
    fluctuate(client1, f)


if __name__ == "__main__":
    main()
