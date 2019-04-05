class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #new item, gets put in oldest datapoint's spot. ( index 0)
    pass

  def get(self):
    pass