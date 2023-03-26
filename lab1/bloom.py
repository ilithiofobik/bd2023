import mmh3
import numpy as np
import bitarray
from plots import bloom_plot

class BloomFilter:
    array = bitarray.bitarray(0)

    def __init__(self, n):
        self.array = bitarray.bitarray(n)

    def onAdd(self, x):
        for i in range(1, 9):
            self.array[mmh3.hash(x, i * i) % len(self.array)] = 1
    
    def onCheck(self, x):
        for i in range(1, 9):
            if self.array[mmh3.hash(x, i * i) % len(self.array)] == 0:
                return False
        return True

def bloom_exp(poem):
    n = len(poem)
    x = np.arange(n)
    y = np.zeros(n, int)
    filter = BloomFilter(n)

    for i in range(n):
        word = poem[i]
        filter.onAdd(word)
        if not filter.onCheck(word):
            raise Exception("Bloom filter failed to add word " + word)
        for j in range(n):
            if filter.onCheck(poem[j]):
                y[i] += 1
    bloom_plot(x, y)