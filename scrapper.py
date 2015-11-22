from googlefinance import getQuotes

def scrape(ticker):
    realtime_qoute = getQuotes(ticker)
    print realtime_qoute[0][u'LastTradePrice']
    return realtime_qoute[0][u'LastTradePrice']

def main():
    s = scrape('googl')
    print s

if __name__ == "__main__":
    main()
