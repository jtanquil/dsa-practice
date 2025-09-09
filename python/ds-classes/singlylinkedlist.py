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
    pass

  def __setitem__(self, i, val):
    pass

  def insert_at(self, i, val):
    pass

  def delete_at(self, i):
    pass

  def build(self, iter):
    pass

if __name__ == "__main__":
  test_node = SinglyLinkedListNode(3)
  test_node.next = SinglyLinkedListNode(4)
  test_node.next.next = SinglyLinkedListNode(5)

  for j in range(4):
    print(test_node.traverse(j))

  test_list = SinglyLinkedList()