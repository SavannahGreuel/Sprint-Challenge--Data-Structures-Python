class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0 #current index to overwrite
    self.storage = [None]*capacity 

  def append(self, item):
    #new item, gets put in oldest datapoint's spot. ( index 0)
    self.storage[self.current] = item 
    if self.current < self.capacity - 1:
      self.current+=1
    else:
      self.current = 0


  def get(self):
    return [item for item in self.storage if item is not None]