from adt import Sequence, Set

class DynamicArray():
  DEFAULT_CAPACITY = 16
  RESIZE_FACTOR = 2
  SHRINK_THRESHOLD = 1/4

  def __init__(self, capacity = DEFAULT_CAPACITY):
    self._capacity = capacity
    self._size = 0
    self._a = [None] * self._capacity

  def __len__(self):
    return self._size

  def is_empty(self):
    return len(self) == 0

  def capacity(self):
    return self._capacity

  def __getitem__(self, i):
    if abs(i) in range(len(self)) or i == -len(self):
      return self._a[i]
    else:
      print("error: index out of range")

  def __setitem__(self, i, val):
    if abs(i) in range(len(self)) or i == -len(self):
      self._a[i] = val
    else:
      print("error: assignment index out of range")

  def __iter__(self):
    for i in range(len(self)):
      yield self[i]
    
  def _resize(self, grow = True):
    pass

  def __str__(self):
    return f'[{", ".join([f'{i}' for i in self])}]'

if __name__ == "__main__":
  test = DynamicArray()
  test._a = [1, 2, 3]
  test._size = 3

  test[0] = 3
  test[1] = 5
  test[-1] = 7

  print(test[0], test)