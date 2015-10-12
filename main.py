import sys
import random

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

def main():
    print random.randint(0, 9)
    test_stock = Stock()
    print vars(test_stock) #same as print test_stock.__dict__
    #print test_stock.__dict__.keys()
    #print test_stock.__dict__.values()
    print test_stock.StockPrice
    test_stock.StockPrice = 100.22
    print test_stock.StockPrice


if __name__ == "__main__":
    main()
