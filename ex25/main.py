import random
import matplotlib.pyplot as plt
import scipy.stats

class Bucket: # Vitter with one place
    def __init__(self):
        self.Idx  = None # Index inside the bucket
        self.Val  = None # Value at that index
        self.Seen = 0    # How many values have been seen by this bucket

    def onGet(self, z):
        self.Seen += 1
        if random.random() <= (1 / self.Seen):
            self.Idx = self.Seen
            self.Val = z

    def readData(self):
        return self.Idx, self.Val

class SingleWindow:
    def __init__(self, window_size):
        self.Partial    = Bucket() 
        self.Active     = None 
        self.WindowSize = window_size

    def onGet(self, z):
        self.Partial.onGet(z)  
        if self.Partial.Seen == self.WindowSize: # Partial becomes active, new partial is created
            self.Active  = self.Partial
            self.Partial = Bucket()
            
    def readData(self):
        if self.Active is None: # Case when we are considering first n elements
            (_, partial_val) = self.Partial.readData()
            return partial_val
        else:
            (active_idx, active_val) = self.Active.readData()
            (_, partial_val)         = self.Partial.readData()
            
            if active_idx <= self.Partial.Seen:
                return partial_val
            else:
                return active_val
            
    def readIdx(self):
        if self.Active is None: # Case when we are considering first n elements
            (partial_idx, _) = self.Partial.readData()
            return partial_idx - 1
        else:
            (active_idx, _) = self.Active.readData()
            return (self.WindowSize + active_idx - 1 - self.Partial.Seen) % self.WindowSize

def histogram_test():
    window_size = 5
    num_of_tests = 1000
    stream_len = 1000

    sample = [] 
    for _ in range(num_of_tests):
        window = SingleWindow(window_size)
        for i in range(stream_len):
            window.onGet(i)
            sample.append(window.readData())

    plt.hist(sample, density=True, bins=stream_len)
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('SW distr (window size = 5, stream length = 1000)))')
    plt.savefig('data/histogram.png', dpi=300)

def chi_square_test():
    window_size  = 5
    stream_len   = 10000 
    frequencies  = [0] * 5

    window = SingleWindow(window_size)
    for i in range(stream_len):
        window.onGet(i)
        frequencies[window.readIdx()] += 1

    (chisq, p) = scipy.stats.chisquare(frequencies)
    print(f"Chi-square statistic: {chisq}, p-value: {p}")

if __name__ == '__main__':
    histogram_test()
    chi_square_test()