import yfinance as yf
import matplotlib.pyplot as plt
import random

class R_Algorithm:
    def __init__(self, sample_size):
        self.A = [None] * sample_size
        self.E = [None] * sample_size
        self.n = 0
        self.k = sample_size

    def onGet(self, z):
        if self.n < self.k:
            self.A[self.n] = self.n
            self.E[self.n] = z
        else:
            if random.random() < (self.k/self.n):
                i = random.randrange(self.k)
                self.A[i] = self.n
                self.E[i] = z
        self.n += 1

    def getData(self):
        return self.A, self.E


BTC_Ticker = yf.Ticker("BTC-USD")
BTC_Data = BTC_Ticker.history(period="5y")

R = R_Algorithm(40)

for open_val in BTC_Data['Open']:
    R.onGet(open_val)

A, E = R.getData()

sorted_idx = sorted(A, key=lambda k: BTC_Data.index[k])
dates  = [BTC_Data.index[i] for i in sorted_idx]
sample = [BTC_Data['Open'][date] for date in dates]

plt.plot(BTC_Data.index, BTC_Data['Open'], color='blue', label='Exact', linewidth=1)
plt.plot(dates, sample, color='red', label='Sample', linewidth=2)
plt.legend()
plt.xlabel('Date')
plt.ylabel('BTC Opening Price [USD]')
plt.savefig('data/compare.png', dpi=300)
plt.close()