from main import get_historical
from main import Client
from main import Investment
from main import Stock

def stock_estimate(portfolio, symb):
    stk_hist = get_historical(symb, 15)
    print stk_hist
    print stk_hist[0].StockID
    print len(stk_hist)
    z = 1
    for x in stk_hist:
        print "{}: {}".format(z, x.StockID)
        z+=1

    #for stock in portfolio:
    #    if portfolio.StockID == symb:
    #        pass
    #        #Code about if this client has the ticker
    #    else:
    #info over the past few weeks for ticker, default 15(max)


#Main for testing
def main():
    client1 = Client()
    client1.Portfolio.append(Investment(Stock('GOOG', 'Dec 8', 762)))
    print client1.Portfolio[0]
    print client1.Portfolio[0].StockID
    print client1.Portfolio[0].TradeDate
    print client1.Portfolio[0].StockVolume
    print client1.Portfolio[0].PriceTraded
    
    stock_estimate(client1.Portfolio, 'GOOG')

if __name__ == "__main__":
    main()