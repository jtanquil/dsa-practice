from adt import PriorityQueue
from random import randint, seed
from math import floor

class Heap(PriorityQueue):
  def __init__(self):
    self._h = []

  def __len__(self):
    return len(self._h)
  
  def is_empty(self):
    return len(self._h) == 0

  def get_max(self, i):
    if not self.is_empty():
      return self._h[0]
    else:
      return None

  def build(self, iter):
    self._h = []

    for ele in iter:
      self.insert(ele)

  # append val to heap, then sift up:
  # check if it satisfies max heap property. if it does, done
  # otherwise, swap w/parent, sift up on parent index
  def insert(self, val):
    self._h.append(val)

    self.max_sift_up(len(self._h) - 1)

  def max_sift_up(self, index):
    if index > 0:
      parent = floor((index - 1) / 2)

      if self._h[index] >= self._h[parent]:
        self._h[index], self._h[parent] = self._h[parent], self._h[index]
        self.max_sift_up(parent)

  # reassign root w/value of the last element, then sift that element down
  def delete_max(self):
    self._h[0], self._h[len(self) - 1] = self._h[len(self._h) - 1], self._h[0]
    max_element = self._h.pop()
    self.max_sift_down(0)

    return max_element

  def max_sift_down(self, index):
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < len(self) and self._h[index] < self._h[left_child]:
      self._h[index], self._h[left_child] = self._h[left_child], self._h[index]
      self.max_sift_down(left_child)

    if right_child < len(self) and self._h[index] < self._h[right_child]:
      self._h[index], self._h[right_child] = self._h[right_child], self._h[index]
      self.max_sift_down(right_child)

  def find_max(self, val):
    return self._h[0]

  def __str__(self):
    return f'{self._h}'

# implement in-place heapsort: maintain a prefix array
# repeatedly insert the next element into the prefix w/append
# do this until prefix length = length of input array
# delete_max will swap the max element w/end of prefix, sift down the swapped element
# do this until prefix length = 0
class HeapSort():
  def __init__(self, iter):
    self._h = iter
    self.prefix_length = 0

  def __len__(self):
    return self.prefix_length

  def is_empty(self):
    return len(self) == 0
  
  def append(self):
    self.prefix_length += 1

    self.max_sift_up(self.prefix_length - 1)

  def max_sift_up(self, index):
    if index > 0:
      parent = floor((index - 1) / 2)

      if self._h[index] >= self._h[parent]:
        self._h[parent], self._h[index] = self._h[index], self._h[parent]
        self.max_sift_up(parent)

  def delete_max(self):
    self._h[0], self._h[len(self) - 1] = self._h[len(self) - 1], self._h[0]
    self.prefix_length -= 1

    self.max_sift_down(0)

  def max_sift_down(self, index):
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < len(self) and self._h[index] < self._h[left_child]:
      self._h[index], self._h[left_child] = self._h[left_child], self._h[index]
      self.max_sift_down(left_child)

    if right_child < len(self) and self._h[index] < self._h[right_child]:
      self._h[index], self._h[right_child] = self._h[right_child], self._h[index]
      self.max_sift_down(right_child)

  def sort(self):
    while self.prefix_length < len(self._h):
      self.append()

    while self.prefix_length > 0:
      self.delete_max()

if __name__ == "__main__":
  seed(3413)
  test = [randint(0, 20) for i in range(10)]
  test_heap = Heap()

  print(test)

  for ele in test:
    test_heap.insert(ele)

  print(test_heap)

  while len(test_heap) > 0:
    print(test_heap.delete_max())
    print(test_heap)

  test2 = [randint(-20, 20) for i in range(20)]
  print(test2)
  
  test_heapsort = HeapSort(test2) 
  test_heapsort.sort()

  print(test2)

