import sys

class index:
    IndexID = ''
    IndexName = ''
    IndexValue = 0.0
    IndexNetChange = 0.0
    IndexChange = 0.0
    IndexOpen  = 0.0
    IndexDayRange = ''
    IndexPreviousClose = 0.0
    Index52WKRange = ''
    Index1YRReturn = 0.0
    IndexYTDReturn = 0.0
    IndexTotalMembers = 0
    IndexMembersUp = 0
    IndexMembersDown = 0

class stock:
    StockID = ''
    StockName = ''
    StockOpen = 0.0
    StockNetChange = 0.0
    StockChange = 0.0
    StockDayRange = ''
    StockVolume = 0
    StockPreviousClose = 0.
    Stock52WKRange = ''
    Stock1YRReturn = 0.0
    StockYTDReturn = 0.0
    StockPERatio = 0.
    StockEarningsPS (per share) = 0.
    StockMarketCap = 0.0
    StockSharesOutdanding = 0.0
    StockPrice = 0.0
    StockDividend = 0.0
    StockSector = ''
    StockIndustry = ''
    StockSubIndustry = ''

class broker:
    BrokerID = ''
    BrokerName = ''
    BrokerFirmID = ''
    BrokerPLReport = 0.0
    BrokerTotalBudget = 0.0
    BrokerTotalStocks Integer
    BrokerBudget { String : String : Float } (ClientID : StockID : Budget $)
    BrokerCommission Float
    BrokerLicenseType String (Select from Options)
    BrokerShares { String: Float } (StockID and Quantity)

class firm:
    pass

class client:
    pass

class transaction:
    pass

class exchange:
    pass



def main():
    print 'test'

if __name__=="__main__":
    main()
