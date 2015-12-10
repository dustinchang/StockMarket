from main import get_historical
from main import Client
from main import Investment
from main import Stock

def change(curr_price, prev_price, avg_prices):
    avg_prices.append(round(float(curr_price)/float(prev_price), 2))

##Determine the patterns between highs and lows over
# the past 2 week business days
#
def stock_patterns(stk_hist):
    close_prices = []
    for stock in stk_hist:
         close_prices.append(stock.StockClose)
    print close_prices

    prev_curr = close_prices[0]
    curr = 0
    avg_prices = []
    for i, price  in enumerate(close_prices):
        curr = price
        if i % 9 == 0:
            change(curr, prev_curr, avg_prices)
            print "price:{} curr:{} prev:{}".format(price, curr, prev_curr)
            prev_curr = price
        else:
            pass
    print avg_prices
    print len(avg_prices)
    lower_bound = 0
    high_bound = 9
    pattern = []

    while high_bound < len(avg_prices):
        avg = sum(avg_prices[lower_bound:high_bound])/len(avg_prices[lower_bound:high_bound])
        print avg_prices[lower_bound:high_bound]
        print "len={}".format(len(avg_prices[lower_bound:high_bound]))
        print avg
        diff = avg-1.0
        pattern.append(avg-1.0)

        lower_bound = high_bound
        high_bound += 9
    avg =  sum(avg_prices[lower_bound:])/len(avg_prices[lower_bound:])
    pattern.append(avg-1.0)
    return pattern
    #print "low:{} high:{}".format(lower_bound, high_bound)
    #print "excess:\n{}".format(avg_prices[lower_bound:])
    #print "pattern\n{}".format(pattern)

##Evaluate the past 2 weeks of a stocks trading prices
# Determine the appropriate response for stock trader
#
def stock_estimate(portfolio, symb):
    stk_hist = get_historical(symb, 15)
    stock_patterns(stk_hist)
    #determine the stock_patterns
    print stk_hist
    print len(stk_hist)
    z = 1
    #for x in stk_hist:
    #    print "{}: {}".format(z, x.StockID)
    #    z+=1


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
