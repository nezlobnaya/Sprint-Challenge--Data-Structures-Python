class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.index = 0
        

    def append(self, item):
        if len(self.ring) < self.capacity:
            self.ring.append(item)
        else:
            self.ring[self.index] = item
            self.index += 1
            if self.index + 1 > self.capacity:
                self.index = 0


    def get(self):
        return [i for i in self.ring if i is not None]