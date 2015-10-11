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
    StockPreviousClose = 0.0
    Stock52WKRange = ''
    Stock1YRReturn = 0.0
    StockYTDReturn = 0.0
    StockPERatio = 0.0
    StockEarningsPS = 0.0
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
    BrokerTotalStocks = 0
    BrokerBudget = {} #{ String : String : Float } (ClientID : StockID : Budget $)
    BrokerCommission = 0.0
    BrokerLicenseType = ''
    BrokerShares = {} #{ String: Float } (StockID and Quantity)

class firm:
    FirmID = ''
    FirmName = ''
    FirmBudget = 0.0
    FirmType = ''
    FirmTotalBrokers = 0

class client:
    ClientID = ''
    ClientName = ''
    ClientPhoneNumber = 0
    ClientEmailAddress = ''
    ClientBudget = 0.0
    ClientShares = {} #{ String : Float : String } (StockID : Quantity : Can Exercise)
    ClientFirmID = '' #Maybe int
    ClientBrokerID = '' #Maybe int
    ClientPLReport = 0.0
    ClientIndsutry = []

class exhange:
    ExchangeID = ''
    ExchangeName = ''
    ExchangeHQ = ''
    ExchangeEconomy = ''
    ExchangeTimeZone = ''
    ExchangeVolume = 0
    ExchangeNetChange = 0.0
    ExchangeChange = 0.0
    ExchangeOpen = 0.0
    ExchangeDayRange = ''
    ExchangePreviousClose = 0.0
    Exchange52WKRange = ''
    Exchange1YRReturn = 0.0
    ExchangeYTDReturn = 0.0

class transaction:
    TransactionID = ''
    TransactionTime = {} #{Integer:Integer} Maybe use datetime for this
    TransactionBuyer = '' #(ClientID BrokerID FirmID)
    TransactionSeller = '' #(ClientID BrokerID FirmID)
    TransactionTrader = '' #(ClientID BrokerID FirmID)
    TransactionType = '' #(Sell Buy Trade)
    TransactionPLReport = {} #String : Float (only when it's a sell or trade)
    TransactionBSVolume = {} #String : Integer : Float (StockID : Volume : Price)
    TransactionTradeVolume = {} #{stock traded <> stock gained}
                              #{String : Integer : Float <> String : Integer : Float }
                              #StockID : Volume : Price <> StockID : Volume : Price
    TransactionExchange = ''

def main():
    print 'test run'

if __name__ == "__main__":
    main()
