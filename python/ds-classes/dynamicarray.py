from adt import Sequence, Set

class DynamicArray():
  DEFAULT_CAPACITY = 16
  RESIZE_FACTOR = 2
  SHRINK_THRESHOLD = 1/4

  def __init__(self, capacity = DEFAULT_CAPACITY):
    self._capacity = capacity
    self._size = 0
    self._a = [None] * self._capacity

  def build(self, iter):
    self._capacity = len(iter) * self.RESIZE_FACTOR
    self._size = len(iter)
    self._a = [None] * self._capacity

    for i in range(len(iter)):
      self[i] = iter[i]
      print(self[i], iter[i])

  def __len__(self):
    return self._size

  def is_empty(self):
    return len(self) == 0

  def capacity(self):
    return self._capacity

  def __getitem__(self, i):
    if i in range(len(self)):
      return self._a[i]
    elif i in range(-len(self), 0):
      return self._a[len(self) + i]
    else:
      print("error: index out of range")

  def __setitem__(self, i, val):
    if i in range(len(self)):
      self._a[i] = val
    elif i in range(-len(self), 0):
      self._a[len(self) + i] = val
    else:
      print("error: assignment index out of range")

  def __iter__(self):
    for i in range(len(self)):
      yield self[i]

  def __str__(self):
    return f'[{", ".join([f'{i}' for i in self])}]'
    
  def _resize(self, grow = True):
    self._capacity = self._capacity * self.RESIZE_FACTOR if grow else self._capacity // self.RESIZE_FACTOR
    new_arr = [None] * self._capacity

    for i in range(len(self)):
      new_arr[i] = self[i]

    self._a = new_arr

if __name__ == "__main__":
  test = DynamicArray()
  test.build([1, 2, 3])
  
  test[0] = 3
  test[1] = 5
  test[-1] = 7

  print(test[-1], test)

  for i in range(len(test)):
    print(i, test[i])

  for i in range(-len(test), 0):
    print(i, test[i])

  print(test.capacity())

  test._resize()

  print(test.capacity())

  test._resize(grow = False)

  print(test.capacity())