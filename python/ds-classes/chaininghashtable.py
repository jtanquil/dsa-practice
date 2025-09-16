from adt import Set
from hashentry import HashEntry
from singlylinkedlist import SinglyLinkedList
from random import randint, seed

class HashTableChain(SinglyLinkedList):
  def get_by_key(self, key):
    current_node = self.head
    
    while current_node is not None:
      if current_node.val.key == key:
        return current_node

      current_node = current_node.next

    return None

  def set_by_key(self, key, val):
    current_node = self.head

    while current_node is not None:
      if current_node.val.key == key:
        current_node.val.val = val
        return False

      current_node = current_node.next

    self.insert_last(HashEntry(key, val))
    return True
  
  def del_by_key(self, key):
    current_node = self.head

    if current_node is not None and current_node.val.key == key:
      self.head = current_node.next

      if current_node == self.tail:
        self.tail = None

      return True
    else:
      prev_node, current_node = current_node, current_node.next

      while current_node is not None and current_node.val.key != key:
        prev_node, current_node = current_node, current_node.next

      if current_node is not None and current_node.val.key == key:
        prev_node.next = current_node.next

        if current_node.next is None:
          self.tail = prev_node

        return True
    
    return False

    def __str__(self):
      return '(' + super().__str__() + ')'

class ChainingHashTable(Set):
  DEFAULT_CAPACITY = 16

  def __init__(self, capacity = DEFAULT_CAPACITY):
    self._capacity = capacity
    self._a = [None] * self._capacity
    self._size = 0
    
  def __len__(self):
    return self._size

  def hash(self, key):
    return hash(key) % self.capacity

  def __iter__(self):
    for chain in self._a:
      if chain is not None:
        for ele in chain:
          yield ele
      else:
        yield None

  def __getitem__(self, key):
    chain = self._a[self.hash(key)]

    return None if chain is None else chain.get_by_key(key)

  def __setitem__(self, key, val):
    chain = self._a[self.hash(key)]
    element_added = False

    if chain is None:
      self._a[self.hash(key)] = HashTableChain()
      chain = self._a[self.hash(key)]

    element_added = chain.set_by_key(key, val)

    if element_added:
      self._size += 1

  def __delitem__(self, key):
    chain = self._a[self.hash(key)]

    if chain is not None:
      element_removed = chain.del_by_key(key)

    if element_removed:
      self._size -= 1

  def build(self, iter):
    self.capacity = len(iter)
    self._a = [None] * self.capacity
    self._size = 0

    for ele in iter:
      self[ele.key] = ele.val

  def __str__(self):
    return '[' + ", ".join(f'{ele}' for ele in self) + ']'

if __name__ == "__main__":
  seed(3413)

  hash_table = ChainingHashTable()
  test = []

  for j in range (10):
    test.append(HashEntry(f'test{j}', j))

  hash_table.build(test)

  print(hash_table)

  for j in range(11, 20):
    hash_table[f'test{j}'] = j

  print(hash_table)

  for j in range(0, 20, 2):
    print(f'checking test{j}')
    if hash_table[f'test{j}'] is not None:
      print(f'deleting test{j}')
      del hash_table[f'test{j}']

  print(hash_table)

  for k in range(20):
    print(f'test{k}: {hash_table[f'test{k}']}')