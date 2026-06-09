from collections import deque

class RollingMean:
    def __init__(self,window):
        self.window = window
        self.values = deque(maxlen=window)

    def update(self,value):
        self.values.append(value)

        if len(self.values) < self.window:
            return None
        
        return sum(self.values) / self.window
    
