class CacheNode():
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

  def __str__(self):
    return f'[ key: {self.key}, val: {self.val}, prev: {None if self.prev is None else self.prev.key}, next: {None if self.next is None else self.next.key}]'

class LRUCache():
  def __init__(self, capacity = 3):
    self.cache = {}
    self.capacity = capacity
    self.size = 0
    self.lru = None
    self.mru = None

  def get(self, key):
    if key not in self.cache:
      return -1
    else:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val

  def put(self, key, val):
    if key not in self.cache:
      node = CacheNode(key, val)
      
      if self.size == self.capacity:
        lru = self.lru
        self.remove(lru)
        del self.cache[lru.key]
        self.size -= 1
      
      self.insert(node)
      self.cache[key] = node
      self.size += 1
    else:
      self.remove(self.cache[key])
      self.insert(self.cache[key])

      self.cache[key].val = val

  def remove(self, node):
    if self.lru == node or self.mru == node:
      if self.lru == node:
        new_head = self.lru.next
        node.next = None

        if new_head is not None:
          new_head.prev = None
        
        self.lru = new_head
      elif self.mru == node:
        new_tail = self.mru.prev
        node.prev = None

        if new_tail is not None:
          new_tail.next = None
        
        self.mru = new_tail
    elif self.lru != node and self.mru != node:
      node.prev.next, node.next.prev = node.next, node.prev
      node.prev, node.next = None

  def insert(self, node):
    if self.lru is None:
      self.lru, self.mru = node, node
    else:
      old_tail = self.mru
      old_tail.next = node
      node.prev = old_tail
      self.mru = node

  def __str__(self):
    return f'{{ {[f'{self.cache[key]}' for key in self.cache]} }}'

if __name__ == "__main__":
  cache = LRUCache()

  for i in range(10):
    cache.put(i, i * 10)
    print(cache, cache.lru, cache.mru)