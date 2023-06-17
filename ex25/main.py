import random

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
        if self.Active is None: # Case when we are considering first n elements
            self.Partial.onGet(z)  
        else:
            if self.Partial.Seen == self.WindowSize: # Partial becomes active, new partial is created
                self.Active  = self.Partial
                self.Partial = Bucket()
            self.Partial.onGet(z)

    def readData(self):
        if self.Active is None: # Case when we are considering first n elements
            return self.Partial.readData()  
        else:
            (active_idx, active_val) = self.Active.readData()
            (_, partial_val)         = self.Partial.readData()
            
            is_expired = active_idx <= self.Partial.Seen
            if is_expired:
                return partial_val
            else:
                return active_val

class SlidingWindows:
    def __init__(self, window_size, sample_size):
        self.Windows    = [ SingleWindow(window_size) for _ in range(sample_size) ]

    def onGet(self, z):
        for window in self.Windows:
            window.onGet(z)

    def readData(self):
        return [ window.readData() for window in self.Windows ]