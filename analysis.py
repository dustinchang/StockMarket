from stock_backend import get_historical
from stock_backend import Client
from stock_backend import Investment
from stock_backend import Stock

def change(curr_price, prev_price, avg_prices):
    avg_prices.append(round(float(curr_price)/float(prev_price), 2))

##Determine the patterns between highs and lows over
# the past 2 week business days
#
def stock_patterns(stk_hist):
    close_prices = []
    for stock in stk_hist:
         close_prices.append(stock.StockClose)

    prev_curr = close_prices[0]
    curr = 0
    avg_prices = []
    for i, price  in enumerate(close_prices):
        curr = price
        if i % 9 == 0:
            change(curr, prev_curr, avg_prices)
            #print "price:{} curr:{} prev:{}".format(price, curr, prev_curr)
            prev_curr = price
        else:
            pass
    lower_bound = 0
    high_bound = 9
    pattern = []

    while high_bound < len(avg_prices):
        avg = sum(avg_prices[lower_bound:high_bound])/len(avg_prices[lower_bound:high_bound])
        #print avg_prices[lower_bound:high_bound]
        #print "len={}".format(len(avg_prices[lower_bound:high_bound]))
        #print avg
        diff = avg-1.0
        pattern.append(avg-1.0)

        lower_bound = high_bound
        high_bound += 9
    avg =  sum(avg_prices[lower_bound:])/len(avg_prices[lower_bound:])
    pattern.append(avg-1.0)
    #print "low:{} high:{}".format(lower_bound, high_bound)
    #print "excess:\n{}".format(avg_prices[lower_bound:])
    #print "len_patter:{}\npattern\n{}".format(len(pattern),pattern)
    return pattern

##Determines the choice to advice the trader on what to do with the stock
# whether they own the stock or are currently just tracking the stock
#
def choices(estimates, portfolio, symb):
    #estimates = []
    for stock in portfolio:
        if stock.StockID == symb:
            if all(est > 0 for est in estimates):
                return 'Sell, as stocks may be reaching peak'
            elif all(est < 0 for est in estimates):
                return 'Buy, as stocks are at a low point'
            elif all(est > 0 for est in estimates[2:]) and all(est < 0 for est in estimates[:2]):
                return 'Hold, stocks may continue to rise'
            elif estimates[-1] > 0 and all(est <= 0 for est in estimates[:-1]):
                return 'Buy, stocks rising from a low'
            elif estimates[-1] < 0 and all(est >= 0 for est in estimates[:-1]):
                return 'Sell, stocks dropping from a high'
            else:
                return 'Hold, stable fluctuation'
        else:
            pass #Shouldn't need
    #If reaches out of for loop, then the stock is not owned by trader
    if all(est > 0 for est in estimates):
        return "Don't buy, as stocks are at high"
    elif all(est < 0 for est in estimates):
        return 'Buy, as stocks are at a low point'
    elif all(est > 0 for est in estimates[2:]) and all(est < 0 for est in estimates[:2]):
        return 'Buy, stocks may continue to rise'
    elif all(est > 0 for est in estimates[2:]) and all(est <= 0 for est in estimates[:2]):
        return 'Wait, may just be a temporary rise'
    elif estimates[-1] > 0 and all(est <= 0 for est in estimates[:-1]):
        return 'Buy, stocks rising from a low'
    elif estimates[-1] < 0 and all(est >= 0 for est in estimates[:-1]):
        return 'Watch closely for any sudden drops'
    else:
        return 'Wait, stable fluctuation'

##Evaluate the past 2 weeks of a stocks trading prices
# Determine the appropriate response for stock trader
#
def stock_estimate(portfolio, symb):
    stk_hist = get_historical(symb, 15)
    stk_pattern = stock_patterns(stk_hist)
    estimates = []
    for avg in stk_pattern:
        if avg >= .003:
            estimates.append(2)
        elif avg >= .002:
            estimates.append(1)
        elif avg < .002 and avg >= -.002:
            estimates.append(0)
        elif avg < -.002:
            estimates.append(-1)
        elif avg < -.003:
            estimates.append(-2)

    #if all(x < 0 for x in estimates[3:]):
    #    print 'all negs'
    #else:
    #    print 'wrong'
    return choices(estimates, portfolio, symb)
'''
#Main for testing
def main():
    client1 = Client()
    client1.Portfolio.append(Investment(Stock('GOOG', 'Dec 8', 762)))
    client1.Portfolio.append(Investment(Stock('AAPL', 'Dec 8', 117)))

    test = stock_estimate(client1.Portfolio, 'GOOG')
    print test

if __name__ == "__main__":
    main()
'''
