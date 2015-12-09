from main import get_historical
from main import Client
from main import Investment
from main import Stock

##Determine the patterns between highs and lows over
# the past 2 week business days
#
def stock_patterns(stk_hist):
    pass

##Evaluate the past 2 weeks of a stocks trading prices
# Determine the appropriate response for stock trader
#
def stock_estimate(portfolio, symb):
    stk_hist = get_historical(symb, 15)
    #determine the stock_patterns
    print stk_hist
    print stk_hist[0].StockID
    print len(stk_hist)
    z = 1
    for x in stk_hist:
        print "{}: {}".format(z, x.StockID)
        z+=1


    for stock in portfolio:
        if stock.StockID == symb:
            print 'yes'
            #Code about if this client has the ticker
        else:
            print 'no'


#Main for testing
def main():
    client1 = Client()
    client1.Portfolio.append(Investment(Stock('GOOG', 'Dec 8', 762)))
    client1.Portfolio.append(Investment(Stock('AAPL', 'Dec 8', 117)))
    print client1.Portfolio[0]
    print client1.Portfolio[0].StockID
    print client1.Portfolio[0].TradeDate
    print client1.Portfolio[0].StockVolume
    print client1.Portfolio[0].PriceTraded

    stock_estimate(client1.Portfolio, 'GOOGL')

if __name__ == "__main__":
    main()
