from adt import Sequence, Set

class SinglyLinkedListNode():
  def __init__(self, val):
    self.val = val
    self.next = None

  def traverse(self, i):
    # return the element i spaces from the current node or the tail, whichever comes first
    current_node = self
    for j in range(i):
      if current_node.next is None:
        return current_node
      else:
        current_node = current_node.next

    return current_node

  def __str__(self):
    return f'{self.val}'

class SinglyLinkedList(Sequence):
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def __len__(self):
    return self._size

  def is_empty(self):
    return len(self) == 0

  def __iter__(self):
    current_node = self.head
    while current_node is not None:
      yield current_node
      current_node = current_node.next

  def __getitem__(self, i):
    if i == len(self) - 1 or i == -1:
      return self.tail
    elif i in range(len(self) - 1):
      return self.head.traverse(i)
    elif -i in range(2, len(self) + 1):
      return self.head.traverse(len(self) + i)
    else:
      print("error: index is out of bounds")
    
  def __setitem__(self, i, val):
    if i == len(self) - 1 or i == -1:
      self.tail.val = val
    elif i in range(len(self) - 1):
      self.head.traverse(i).val = val
    elif -i in range(2, len(self) + 1):
      self.head.traverse(len(self) + i).val = val
    else: 
      print("error: assignment index is out of bounds")

  def insert_at(self, i, val):
    if i not in range(len(self) + 1):
      print("error: insertion index is out of bounds")
      return
    
    new_node = SinglyLinkedListNode(val)

    if i == 0:
      self.head, new_node.next = new_node, self.head

      if len(self) == 0:
        self.tail = new_node
    elif i == len(self):
      self.tail.next, self.tail = new_node, new_node
    else:
      prev_node = self.head.traverse(i - 1)
      old_node = prev_node.next
      prev_node.next, new_node.next = new_node, old_node

    self._size += 1

  def delete_at(self, i):
    if i not in range(len(self)):
      print("error: deletion index out of range")
      return

    old_head = self.head

    if i == 0:
      self.head = old_head.next

      if self._size == 1:
        self.tail = None
      
      self._size -= 1
    else:
      prev_node = old_head.traverse(i - 1)
      old_node = prev_node.next

      # if old_node is the tail, prev_node becomes the new tail
      if old_node.next is None:
        self.tail = prev_node
      
      prev_node.next = old_node.next
      self._size -= 1

  def build(self, iter):
    self.head = None
    self.tail = None
    self._size = 0

    for ele in range(len(iter) - 1, -1, -1):
      self.insert_first(iter[ele])
  
  def __str__(self):
    return ", ".join([f'{node}' for node in self])

if __name__ == "__main__":
  test_node = SinglyLinkedListNode(3)
  test_node.next = SinglyLinkedListNode(4)
  test_node.next.next = SinglyLinkedListNode(5)

  for j in range(4):
    print(test_node.traverse(j))

  test_list = SinglyLinkedList()
  test_list.insert_first(1)
  test_list.insert_first(2)
  test_list.insert_first(3)
  test_list.insert_last(4)
  test_list.insert_last(5)

  print(test_list)

  test_list.insert_at(3, 6)
  test_list.insert_at(1, 7)

  print(test_list)

  test_list[1] = 2
  test_list[-1] = 4
  test_list[5] = 7
  test_list[-4] = 12

  print(test_list)

  test_list.build([1, 2, 3, 4, 5, 6, 7, 8])
  
  print(test_list, test_list.head, test_list.tail)

  test_list.delete_first()
  test_list.delete_last()
  
  print(test_list)

  test_list.delete_at(5)
  print(test_list)
  test_list.delete_at(2)
  print(test_list)
  test_list.delete_at(3)
  print(test_list)
  test_list.delete_at(1)
  print(test_list)
  test_list.delete_at(1)
  print(test_list)
  test_list.delete_last()
  print(test_list, test_list.head, test_list.tail)