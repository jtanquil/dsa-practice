from adt import Queue

class CircularBuffer(Queue):
  DEFAULT_CAPACITY = 10

  def __init__(self, capacity = DEFAULT_CAPACITY):
    self.capacity = capacity
    self._a = [None] * self.capacity
    self.read_index = 0
    self.write_index = 0
    self._size = 0

  def __len__(self):
    return self._size

  def enqueue(self, val):
    self._a[self.write_index] = val

    if self.read_index == self.write_index:
      self.read_index = (self.read_index + 1) % self.capacity

    self.write_index = (self.write_index + 1) % self.capacity
  
  def dequeue(self):
    dequeued = self._a[self.read_index]
    self._a[self.read_index] = None
    self.read_index = (self.read_index + 1) % self.capacity

    return dequeued

  def __str__(self):
    return f'{self._a}'

if __name__ == "__main__":
  test_queue = CircularBuffer()

  for i in range(15):
    test_queue.enqueue(i)
    print(test_queue)

  for j in range(7):
    print(test_queue.dequeue())
    print(test_queue)