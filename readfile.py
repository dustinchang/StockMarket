import stock_pb2
import sys

def ListStocks(stock_list):
	for stock in stock_list.stock:
		print "StockPrice: ", stock.StockPrice

stock_list = stock_pb2.StockList()

f = open(sys.argv[1], "rb")
stock_list.ParseFromString(f.read())
f.close()

ListStocks(stock_list)