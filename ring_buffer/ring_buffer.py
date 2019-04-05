class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #new item, gets put in oldest datapoint's spot. ( index 0)
    self.storage.pop(0)
    self.storage.append(item)


  def get(self):
    return self.storage