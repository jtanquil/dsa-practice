from random import randint, seed

class ListNode():
  def __init__(self, key = None):
    self._key = key
    self.next = None
    self.prev = None

  def __str__(self):
    return f'{self._key}'

  def __eq__(self, other):
    return self._key == other._key

  def __lt__(self, other):
    return self._key < other._key

  def __gt__(self, other):
    return self._key > other._key

class LinkedList():
  def __init__(self, nodes = None):
    self._size = 0
    self._sentinel = ListNode()

    if (nodes is not None):
      for node in nodes:
        self.push_tail(node)

  def __len__(self):
    return self._size

  def __str__(self):
    if (len(self) == 0):
      return "list is empty"
    else:
      keys = []
      current_node = self._sentinel.next

      while (current_node != self._sentinel):
        keys.append(f'{current_node}')
        current_node = current_node.next
      
      return ", ".join(keys)

  def __getitem__(self, val):
    if (val >= len(self)):
      print("error: list is empty")
      return None
    else:
      current_node = self._sentinel.next

      for i in range(val):
        current_node = current_node.next

      return current_node

  def push_head(self, val):
    new_node = ListNode(val) if not isinstance(val, ListNode) else val
    new_node.prev = self._sentinel
    current_head = self._sentinel.next
    self._sentinel.next = new_node

    if (current_head is None):
      self._sentinel.prev = new_node
      new_node.next = self._sentinel
    else:
      current_head.prev = new_node
      new_node.next = current_head

    self._size += 1

  def push_tail(self, val):
    new_node = ListNode(val) if not isinstance(val, ListNode) else val
    new_node.next = self._sentinel
    current_tail = self._sentinel.prev
    self._sentinel.prev = new_node

    if (current_tail is None):
      self._sentinel.next = new_node
      new_node.prev = self._sentinel
    else:
      current_tail.next = new_node
      new_node.prev = current_tail

    self._size += 1

if __name__ == "__main__":
  test = LinkedList()

  for i in range(10):
    test.push_head(i)
    test.push_tail(-i)

  print(test)
  print(ListNode(3) != ListNode(4))
  print(test[3])

  test2 = LinkedList([ListNode(1), ListNode(2), ListNode(3)])
  print(test2)