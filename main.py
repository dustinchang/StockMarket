import datetime, time

from decimal import Decimal

from googlefinance import getQuotes

import cPickle as pickle

import random

import sys
from sys import *

import re

import urllib

import Tkinter
from Tkinter import *

import locale

import json

import matplotlib.pyplot as plt
import matplotlib, sys
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from numpy import *


"""
Implementation of a stock market exchange where stocks are continually on the rise or dropping.
This program will assist on whether you should purchase or sell stocks.
"""

class Stock:
    """Details of a Stock and it's contents"""
    def __init__(self, symb, day, close, open_ = 0.0, high = 0.0, low = 0.0, volume = 0.0):
        """Stock Constructor"""
        self.StockID = symb
        self.StockDate = day
        self.StockOpen = open_
        self.StockDayRange = str(low) + ' - ' + str(high)
        self.StockVolume = volume
        self.StockClose = close
        self.StockPrice = price

    # Testing purposes
    def print_hist_stock(self):
        dt = self.StockDate.strftime('%Y-%m-%d T: %H:%M:%S')
        print 'ID: ' + self.StockID + '\nDate: ' + dt + '\nOpen: ' + str(self.StockOpen)
        print 'Day Range: ' + self.StockDayRange + '\nClose: ' + str(self.StockClose) + '\nVolume: ' + str(self.StockVolume)

    # Testing purposes
    def print_stock(self):
        dt = self.StockDate.strftime('%Y-%m-%d T: %H:%M:%S')
        print 'ID: ' + self.StockID + '\nDate: ' + dt
        print 'Last Trade Price: ' + str(self.StockPrice)

class Broker:
    """Details of the identification of a Broker"""
    def __init__(self):
        """Broker Constructor"""
        self.BrokerPhoneNumber = 0
        self.BrokerEmailAddress = ''
        self.BrokerAuthority = ''
        self.BrokerIndustry = ''
        self.BrokerLicenseIssue = 0
        self.ID = ''
        self.BrokerName = ''
        self.BrokerPassword = ''
        self.BrokerFirmID = ''
        self.BrokerPLReport = 0.0
        self.BrokerTotalBudget = 0.0
        self.BrokerTotalStocks = 0
        self.BrokerBudget = {} #{ String : String : Float } (ClientID : StockID : Budget $)
        self.BrokerProfit = 0.0
        self.BrokerCommission = 0.0
        self.BrokerLicenseType = ''
        self.BrokerShares = {} #{ String: Float } (StockID and Quantity)
        self.BrokerIndustry = ''
        self.Portfolio = [] # list of Investments
        self.InvestmentHistory = [] # list of Investments bought and sold. used for profit loss report
        self.InvestmentExpense = 0.0 # sum of all investments bought
        self.InvestmentRevenue = 0.0 # sum of all investments sold

    def calculate_profit_loss(self, investment): # investment: [inv_bought, inv_sold]
        self.InvestmentHistory.append(investment)
        self.InvestmentExpense += float(investment[0].PriceTraded)
        self.InvestmentRevenue += float(investment[1].PriceTraded)
        self.BrokerProfit = self.InvestmentRevenue - self.InvestmentExpense

        self.BrokerTotalBudget = (float(investment[1].PriceTraded) * investment[0].Volume) + float(self.BrokerTotalBudget)
        self.BrokerPLReport = (self.BrokerProfit / self.InvestmentRevenue) * 100

        print investment[0].PriceTraded
        print investment[1].PriceTraded
        print self.BrokerProfit
        print self.BrokerPLReport

class Firm:
    """Organizational details of a Firm"""
    def __init__(self):
        """Firm Constructor"""
        self.ID = ''
        self.FirmName = ''
        self.FirmBudget = 0.0
        self.FirmType = ''
        self.FirmTotalBrokers = 0
        self.FirmCode = ''
        self.FirmTotalBrokers = 0
        self.Portfolio = [] # list of Investments

class Client:
    """Personal details of an investing Client"""
    def __init__(self):
        """Client Constructor"""
        self.ID = ''
        self.ClientName = ''
        self.ClientPassword = ''
        self.ClientPhoneNumber = 0
        self.ClientEmailAddress = ''
        self.ClientPassword = ''
        self.ClientShares = {} # { String : Float : String } (StockID : Quantity : Can Exercise)
        self.ClientBudget = 0.0
        self.ClientFirmID = '' #Maybe int
        self.ClientBrokerID = '' #Maybe int
        self.ClientPLReport = 0.0
        self.ClientIndustry = ''
        self.ClientProfit = 0.0
        self.ClientPLReport = 0.0 # percentage
        self.Portfolio = [] # list of Investments
        self.InvestmentHistory = [] # list of Investments bought and sold. in case we want to use this later?
        self.InvestmentExpense = 0.0 # sum of all investments bought
        self.InvestmentRevenue = 0.0 # sum of all investments sold

    def calculate_profit_loss(self, investment):
        self.InvestmentHistory.append(investment)
        self.InvestmentExpense += float(investment[0].PriceTraded)
        self.InvestmentRevenue += float(investment[1].PriceTraded)
        self.ClientProfit = self.InvestmentRevenue - self.InvestmentExpense
        self.ClientBudget = (float(investment[1].PriceTraded) * investment[0].Volume) + float(self.ClientBudget)
        self.ClientPLReport = (self.ClientProfit / self.InvestmentRevenue) * 100

class Transaction:
    """Specifics of a trading Transaction"""
    def __init__(self, user, t_type, investment): 
        """Transaction Constructor"""
        self.TransactionID = ''
        self.TransactionStock = [] # if selling [inv_bought, inv_sold]
        self.TransactionTime = investment.TradeDate #{Integer:Integer} Maybe use datetime for this
        self.TransactionBuyer = '' #(ClientID BrokerID FirmID)
        self.TransactionSeller = '' #(ClientID BrokerID FirmID)
        #self.TransactionTrader = [] #(ClientID BrokerID FirmID)
        self.TransactionType = t_type #(Sell Buy Trade)
        self.TransactionPLReport = 0 #String : Float (only when it's a sell or trade)
        self.TransactionBSVolume = {} #String : Integer : Float (StockID : Volume : Price)
        self.TransactionTradeVolume = {} #{stock traded <> stock gained}
                                         #{String : Integer : Float <> String : Integer : Float }
                                         #StockID : Volume : Price <> StockID : Volume : Price
        self.TransactionExchange = ''
        self.check_transaction_type(user, t_type)

    # Function to assign ID values into Transaction{Buyer/Seller/Trader}
    # TransactionTrade will be a list of two user IDs
    def check_transaction_type(self, user, t_type):
        # Transaction type is 'buy'
        if t_type == "buy":
            self.TransactionBuyer = user.ID
            self.TransactionID = investment.StockID+userID+str(investment.TradeDate)
        # Transaction type is 'sell'
        elif t_type == "sell":
            self.TransactionSeller = user.ID
            self.TransactionID = investment.StockID+userID+str(investment.TradeDate)
        # Transaction type is 'trade'
        #else:
        #   self.TransactionTrader = [user[0].ID, user[1].ID]

    # Used only when t_type is 'sell'
    def calculate_profit_loss(self, inves):
        one = float(inves[1].PriceTraded)
        two = float(inves[0].PriceTraded)
        three = float(inves[1].PriceTraded)
        self.TransactionPLReport = ((one - two) / three) * 100

class Investment:
    """ """
    def __init__(self, stock, quantity):
        """ """
        self.StockID = stock.StockID
        self.TradeDate = stock.StockDate
        self.PriceTraded = stock.StockPrice
        self.Volume = quantity

    # testing purposes
    def print_invs(self):
        dt = self.TradeDate.strftime('%Y-%m-%d T: %H:%M:%S')
        print "ID: " + self.StockID + "\nTrade Date: " + dt + "\nPriceTraded: " + str(self.PriceTraded) + "\nVolume: " + str(self.Volume)

## Get historical data
#
#
def get_historical(symb, number_of_days):
    today = datetime.date.today()
    start = (today - datetime.timedelta(days=number_of_days)).strftime('%Y%m%d')
    today = int(time.mktime(datetime.datetime.strptime(start, '%Y%m%d').timetuple()))
    period = number_of_days
    url_string = "http://www.google.com/finance/getprices?q={0}&i={1}&p={2}d&ts={3}".format(symb, interval + 1, period, today)

    # First seven lines are parameter information for the url request. Not needed.
    ticks = urllib.urlopen(url_string).readlines()[7:]
    # Sample output line
    #   a1448980200,747.52,747.52,747.11,747.11,15534
    # Separate each line into values split by ','
    values = [tick.split(',') for tick in ticks]
    # values = [[a1448980200, 747.52, 747.52, 747.11, 747.11, 15534][...]]

    data = []
    for value in values:
        # epoch time = a1448980200
        dt = datetime.datetime.fromtimestamp(float(value[0][1:].strip())) # time in unix epoch format convert to datetime
        data.append(Stock(symb,
                          dt,
                          value[1].strip(), # close
                          value[4].strip(), # open; repeat cause python classes suck. will fix later
                          value[2].strip(), # high
                          value[3].strip(), # low
                          value[5].strip())) # volume
    return data


## Get current stock data
#  example:
#    quotes = getQuotes('AAPL')
#    return:
#    [{u'Index': u'NASDAQ',
#      u'LastTradeWithCurrency': u'129.09',
#      u'LastTradeDateTime': u'2015-03-02T16:04:29Z',
#      u'LastTradePrice': u'129.09',
#      u'Yield': u'1.46',
#      u'LastTradeTime': u'4:04PM EST',
#      u'LastTradeDateTimeLong': u'Mar 2, 4:04PM EST',
#      u'Dividend': u'0.47',
#      u'StockSymbol': u'AAPL',
#      u'ID': u'22144'}]
def get_current(symb):
    quote = getQuotes(symb)
    # Date
    dt = datetime.datetime.strptime(quote[0][u'LastTradeDateTime'], '%Y-%m-%dT%H:%M:%SZ')
    stock = Stock(str(quote[0][u'StockSymbol']), dt, float(quote[0][u'LastTradePrice']))
    return stock

## Get close prices
#
#
def close_prices(symb, number_of_days = 15):
    close_list = []
    stock_objs = get_historical(symb, number_of_days)
    for stk in stock_objs:
        close_list.append(stk.StockClose)
    return close_list

"""
## Used for testing purposes
#
#
def main():
    # create initial stocklist file with 7 day sample
    histo = get_historical('GOOG', 30)
    stock_list = {'GOOG':histo}
    pickle.dump(stock_list, open("stocklist.p", "wb"))


    symblist = {'GOOG' : 'Alphabet Inc.', 'AAPL' : 'Apple Inc.', 'NFLX' : 'Netflix, Inc.', 'AMZN' : 'Amazon.com, Inc.', 'TSLA' : 'Tesla Motors Inc'}
    ticker_list = {'Alphabet Inc.' : 'GOOG', 'Apple Inc.' : 'AAPL', 'Netflix, Inc.' : 'NFLX', 'Amazon.com, Inc.' : 'AMZN', 'Tesla Motors Inc' : 'TSLA'}

    # read from stock list file
    # stock_list = pickle.load(open('stocklist.p', 'rb'))

    #histo = get_historical('GOOG', 30)
    #for s in histo:
    #    s.print_hist_stock()

    #Get all the closing prices
    #close_prices_list = get_close_prices('GOOG')
    #print close_prices_list

    # get historical data on all stocks indicated in symbol list
    #quotelist = []
    #for key in symblist:
    #    quotelist.append(get_historical(key, 10))    # max 15 days

    #for symb in quotelist:
    #    for quote in symb:
    #        quote.print_hist_stock()

    #stock = get_current('GOOG')
    #stock.print_stock()

    # save state of stock list into file
    #pickle.dump(stock_list, open("stocklist.p", "wb"))
 
if __name__ == "__main__":
    main() """
