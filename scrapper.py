from googlefinance import getQuotes
import json
y = getQuotes('Googl')
x = json.dumps(getQuotes('Googl'), indent=2)
print type(x)
print x
print type(y)
print y
print y[0]
print len(y)
print y[0][u'LastTradePrice']


def scrape(ticker):
    realtime_qoute = getQuotes(ticker)
    print realtime_qoute[0][u'LastTradePrice']

def main():
    scrape('googl')

if __name__ == "__main__":
    main()
