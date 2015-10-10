import sys
from usr/local/Cellar/pyqt/4.11.4/lib/python3.5/site-packages/PyQt4/QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

# Set window size.
w.resize(500, 500)

# Set window title
w.setWindowTitle("QT Test 2")

# Show window
w.show(main)

sys.exit(a.exec_())

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
    StockEarningsPS = 0.0
    StockMarketCap = 0.0
    StockSharesOutdanding = 0.0
    StockPrice = 0.0
    StockDividend = 0.0
    StockSector = ''
    StockIndustry = ''
    StockSubIndustry = ''
'''
class broker:
    BrokerID String
    BrokerName String
    BrokerFirmID String
    BrokerPLReport
    BrokerTotalBudget Float $
    BrokerTotalStocks Integer
    BrokerBudget { String : String : Float } (ClientID : StockID : Budget $)
    BrokerCommission Float
    BrokerLicenseType String (Select from Options)
    BrokerShares { String: Float } (StockID and Quantity)
'''
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
