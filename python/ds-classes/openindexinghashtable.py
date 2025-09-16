from adt import Set
from random import randint, seed
from hashentry import HashEntry

class OpenIndexingHashTable(Set):
  DEFAULT_CAPACITY = 16
  DELETED = HashEntry(None, "deleted")

  def __init__(self, capacity = DEFAULT_CAPACITY):
    self._capacity = capacity
    self._a = [None] * self._capacity
    self._size = 0
    self.deleted = self.DELETED
    """setting h1(x) = hash(x), h2(x) = random odd number"""
    self._h1 = hash
    num = randint(1, 255)

    while (num % 2 == 0):
      num = randint(1, 255)

    self._h2 = (lambda x: num)

  def __len__(self):
    return self._size
  
  def hash(self, key, iter = 1):
    return (self._h1(key) + iter * self._h2(key)) % self._capacity

  def __iter__(self):
    for ele in self._a:
      yield ele

  def __getitem__(self, key):
    iter = 1
    item = self._a[self.hash(key, iter)]

    while item is not None and item.key != key and iter < len(self):
      iter += 1
      item = self._a[self.hash(key, iter)]

    return item

  def __setitem__(self, key, val):
    iter = 1

    while self._a[self.hash(key, iter)] is not None and self._a[self.hash(key, iter)] != self.deleted and iter < len(self):
      iter += 1
    
    self._a[self.hash(key, iter)] = HashEntry(key, val)
    self._size += 1

  def __delitem__(self, key):
    iter = 1
    item = self._a[self.hash(key, iter)]

    while item is not None and item.key != key and iter < len(self):
      iter += 1
      item = self._a[self.hash(key, iter)]

    if (item.key == key):
      self._a[self.hash(key, iter)] = self.deleted
      self._size -= 1

  def build(self, iter):
    self._size = 0
    new_capacity_exp = 1

    while (2 ** new_capacity_exp < len(iter)):
      new_capacity_exp += 1

    self._a = [None] * (2 ** new_capacity_exp)

    for ele in iter:
      self[ele.key] = ele.val

  def __str__(self):
    return '[' + ", ".join(f'{ele}' for ele in self) + ']'

if __name__ == "__main__":
  seed(3413)
  hash_table = OpenIndexingHashTable()
  test = []

  for i in range(10):
    test.append(HashEntry(f'test{i}', i))

  for ele in test:
    print(ele)

  hash_table.build(test)

  print(hash_table)

  for i in range(10):
    print(hash_table[f'test{i}'])

  for j in range(0, 10, 2):
    print(f'checking test{j}')
    if hash_table[f'test{j}'] is not None:
      print(f'deleting test{j}')
      del hash_table[f'test{j}']

  print(hash_table)

  for k in range(10):
    print(f'test{k}: {hash_table[f'test{k}']}')