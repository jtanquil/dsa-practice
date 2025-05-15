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
  def __init__(self):
    self._size = 0
    self._sentinel = ListNode()

  def __len__(self):
    return self._size

  def __getitem__(self, val):
    if (len(self) == 0):
      print("error: list is empty")
      return None
    else:
      if (isinstance(val, slice)):
        start, stop, step = val.indices(len(self))

        return [
          self[i] for i in range(start, stop, step)
        ]
      else:
        reduced = val % len(self)
        current_node = self._sentinel.next

        for i in range(reduced):
          current_node = current_node.next

        return current_node

  def __str__(self):
    if (len(self) == 0):
      return "list is empty"
    else:
      keys = []

      for i in range(len(self)):
        keys.append(f'{self[i]}')
      
      return ", ".join(keys)

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

  # merges two sorted lists of listnodes:
  # each iteration, pops the smallest listnode
  # attaches it to the previous listnode
  # at the end, set the first element as the head and the last element as the tail
  def _merge(self, left, right):
    merged = []

    while (len(left) > 0 and len(right) > 0):
      if(left[0] < right[0]):
        merged.append(left.pop(0))
      else:
        merged.append(right.pop(0))

      if (len(merged) > 1):
        merged[-1].prev, merged[-2].next = merged[-2], merged[-1]

    if (len(left) > 0):
      while (len(left) > 0):
        merged.append(left.pop(0))

        if (len(merged) > 1):
          merged[-1].prev, merged[-2].next = merged[-2], merged[-1]
    elif (len(right) > 0):
      while (len(right) > 0):
        merged.append(right.pop(0))

        if (len(merged) > 1):
          merged[-1].prev, merged[-2].next = merged[-2], merged[-1]

    return merged

  def _merge_sort_recursive(self, arr):
    if (len(arr) <= 1):
      return arr
    else:
      mid = len(arr) // 2
      return self._merge(self._merge_sort_recursive(arr[:mid]), self._merge_sort_recursive(arr[mid:]))

  # mergesorts the nodes in the list
  # then updates the sentinel after the last merge
  def merge_sort(self):
    if (len(self) == 0):
      print("error: list is empty")
    else:
      sorted = self._merge_sort_recursive(self[:])
      self._sentinel.next = sorted[0]
      self._sentinel.prev = sorted[-1]

if __name__ == "__main__":
  test = LinkedList()

  for i in range(1):
    test.push_head(randint(0, 10))

  print(test)
  print(ListNode(3) != ListNode(4))
  print(test[3])

  test.merge_sort()
  print(f'sorted: {test}')
  print(test._sentinel.next, test._sentinel.prev)