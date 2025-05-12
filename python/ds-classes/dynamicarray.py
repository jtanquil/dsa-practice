from adt import Sequence, Set

class DynamicArray():
  DEFAULT_CAPACITY = 16
  RESIZE_FACTOR = 2

  def __init__(self, capacity = DEFAULT_CAPACITY):
    self._capacity = capacity
    self._size = 0
    self._arr = [None] * self._capacity

  def __len__(self):
    return self._size

  def is_empty(self):
    return len(self) == 0

  def capacity(self):
    return self._capacity

  def __getitem__(self, i):
    if (i >= len(self)):
      print("Out of bounds error")
      return None
    else:
      return self._arr[i]

  def resize(self, grow = True):
    self._capacity = self._capacity * RESIZE_FACTOR if grow else self._capacity / RESIZE_FACTOR
    new_arr = [None] * self._capacity

    for ele in self._arr:
      new_arr.push(ele)

    self._arr = new_arr

  def __setitem__(self, i, val):
    if (i > len(self)):
      print("Out of bounds error")
    else:
      if (len(self) == self._capacity):
        self.resize()

      self._arr[i] = val
      

      

if __name__ == "__main__":
  test = DynamicArray()

  print(f'size: {len(test)}, empty: {test.is_empty()}, capacity: {test.capacity()}')