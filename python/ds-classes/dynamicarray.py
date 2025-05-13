from random import randint, seed

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

  def __setitem__(self, i, val):
    if (i > len(self)):
      print("Out of bounds error")
    else:
      self._arr[i] = val

  def _resize(self, grow = True):
    print(f'resizing from {self.capacity()}, grow: {grow}')
    self._capacity = self._capacity * self.RESIZE_FACTOR if grow else self._capacity // self.RESIZE_FACTOR
    new_arr = [None] * self._capacity

    for j in range(len(self)):
      new_arr[j] = self[j]

    self._arr = new_arr

  def insert(self, i, val):
      """Splices val into the array at index i."""
      if (i > len(self)):
        print("Out of bounds error")
      else:
        if (len(self) == self.capacity()):
          self._resize()
        
        for j in range(len(self), i, -1):
          self[j] = self[j - 1]

        self[i] = val
        self._size += 1

  def push(self, item):
    self.insert(len(self), item)
  
  def prepend(self, item):
    self.insert(0, item)

  def delete(self, i):
    if (i < 0 or i > len(self)):
      print("Out of bounds error")
      return None
    else:
      if (len(self) <= self._capacity / 4):
        self._resize(grow = False)

      deleted = self[i]
      for j in range(i, len(self) - 1):
        self[j] = self[j + 1]

      self[len(self)] = None
      self._size -= 1

      return deleted

  def pop(self):
    return self.delete(0)

  def find(self, val):
    for j in range(len(self)):
      if self[j] == val:
        return j

    return -1

  def remove(self, val):
    j = 0

    while (j < len(self)):
      if self[j] == val:
        self.delete(j)
      else:
        j += 1

  def __str__(self):
    return "".join([f'arr[{j}]: {self[j]}\n' for j in range(len(self))]) if len(self) > 0 else "array is empty"

def size_capacity_test(arr):
  print(f'size: {len(arr)}, empty: {arr.is_empty()}, capacity: {arr.capacity()}')

def insert_test(arr):
  for j in range(100):
    arr.push(randint(0, 100))

def delete_test(arr):
  for k in range(80):
    print(f'popped: {arr.pop()}')

def remove_test(arr):
  fixed = randint(0, 100)
  for j in range(10):
    print(f'inserting {fixed}')
    arr.insert(randint(0, len(arr)), fixed)

  print(arr)

  arr.remove(fixed)

  print(arr)

if __name__ == "__main__":
  seed(3413)
  test = DynamicArray()

  size_capacity_test(test)
  print(test)

  insert_test(test)

  size_capacity_test(test)
  print(test)

  delete_test(test)

  size_capacity_test(test)
  print(test)

  remove_test(test)