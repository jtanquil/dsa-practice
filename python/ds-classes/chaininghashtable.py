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

      current_node = current_node.next
  
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

class ChainingHashTable(Set):
  DEFAULT_CAPACITY = 16

  def __init__(self, capacity, DEFAULT_CAPACITY):
    self._capacity = capacity
    self._a = [None] * self._capacity
    self._size = 0
    
  def __len__(self):
    return self._size

  def hash(self, key):
    return hash(key) % self.capacity

  def __iter__(self):
    pass

  def __getitem__(self, key):
    pass

  def __setitem__(self, key, val):
    pass

  def __delitem__(self, key):
    pass

  def build(self, iter):
    pass

  def __str__(self):
    pass

if __name__ == "__main__":
  seed(3413)
  hash_table_chain = HashTableChain()

  for i in range(5):
    hash_table_chain.insert_first(HashEntry(f'test{i}', i))

  print(hash_table_chain)

  for i in range(5):
    print(hash_table_chain.get_by_key(f'test{i}'))
    hash_table_chain.set_by_key(f'test{i}', i + 1)
    
  print(hash_table_chain)

  for i in range(0, 5, 2):
    print(f'deleting test{i}')
    hash_table_chain.del_by_key(f'test{i}')
    print(hash_table_chain)

  print(hash_table_chain)