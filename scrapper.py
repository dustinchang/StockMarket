#Requires and runs on googlefinance
from googlefinance import getQuotes

#Call to get the real time quote for any given stock ticker
def scrape(ticker):
    realtime_qoute = getQuotes(ticker)
    print realtime_qoute[0][u'LastTradePrice']
    return realtime_qoute[0][u'LastTradePrice']

#Main for testing
def main():
    s = scrape('googl')
    print s

if __name__ == "__main__":
    main()
