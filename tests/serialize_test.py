#serialize object test

import pickle

class stock(object):
    name = ""
    price = 0

    def __int__(self, name = "unknown"):
        self.name = name

    def hello(self):
        return 'hello, %s' % self.name


#test
s = stock()
s.name = 'goog'
s.price = 100

s.hello()


strfile = 'test_serialize.txt'

with open(strfile, 'wb') as f:
    pickle.dump(s,f)

print("The pickle has landed")


with open(strfile, 'rb') as f:
    o = pickle.load(f)

    print(o)

    if isinstance(o,stock):
        print('name: ' + o.name + ' price: ' + str(o.price))
