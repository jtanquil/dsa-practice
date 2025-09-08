from random import randint, seed

from adt import Sequence, Set

class DynamicArray(Sequence):
  DEFAULT_CAPACITY = 16
  RESIZE_FACTOR = 2
  SHRINK_SIZE = 1/4

if __name__ == "__main__":
  test = DynamicArray()

  for i in range(32):
    test[i] = i

  for j in range(24):
    print(j)
    test.delete_at(j)