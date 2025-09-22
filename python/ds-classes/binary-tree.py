from abc import ABCMeta, abstractmethod
from random import randint, seed

from adt import Sequence, Set

class TreeNode():
  def __init__(self, val):
    self.val = val
    self.height = 0
    self.left = None
    self.right = None
    self.parent = None

  def __str__(self):
    return f'{self.val}'

  def skew(self):
    left_height = 0 if self.left is None else self.left.height
    right_height = 0 if self.right is None else self.right.height
    
    return right_height - left_height

  def is_imbalanced(self):
    return self.skew() < -1 or self.skew() > 1

class BSTNode(TreeNode):
  def __init__(self, val):
    super().__init__(val)

  def __leq__(self, node):
    return self.val <= node.val

  def __lt__(self, node):
    return self.val < node.val 

  def __geq__(self, node):
    return self.val >= node.val

  def __gt__(self, node):
    return self.val > node.val

  def __eq__(self, node):
    return self.val == node.val

  def __neq__(self, node):
    return self.val != node.val

  def insert(self, val):
    if self.val < val:
      if self.right is None:
        self.right = BSTNode(val)
        self.right.parent = self
        self.height = 1 if self.left is None else max(1, 1 + self.left.height)
      else:
        self.right.insert(val)
    else:
      if self.left is None:
        self.left = BSTNode(val)
        self.left.parent = self
        self.height = 1 if self.right is None else max(1, 1 + self.right.height)
      else:
        self.left.insert(val)

    if self.is_imbalanced():
      self.rebalance()

  def rebalance(self):
    pass

  def left_rotate(self):
    pass

  def right_rotate(self):
    pass

class BinarySearchTree(Set):
  def __init__(self):
    self.root = None
    self.node_count = 0

  def __len__(self):
    return self.node_count

  def insert(self, val):
    if self.root is None:
      self.root = BSTNode(val)
    else:
      self.root.insert(val)

    self.node_count += 1

  def build(self, iter):
    self.root = None
    self.node_count = 0

    for ele in iter:
      self.insert(ele)
  
  def __getitem__(self, key):
    pass

  def __setitem__(self, key):
    pass

  def __delitem__(self, key):
    pass

  def __str__(self):
    return ", ".join(self.bfs(lambda node: str(node)))

  def bfs(self, callback):
    nodes = []
    queue = [self.root] if self.root is not None else []

    while len(queue) > 0:
      current_node = queue[0]
    
      if current_node.left is not None:
        queue.append(current_node.left)

      if current_node.right is not None:
        queue.append(current_node.right)

      nodes.append(callback(current_node))
      queue.pop(0)

    return nodes
  
  def dfs(self, callback, order = "in-order"):
    def dfs_r(node, callback, result, order):
      if node is not None:
        if order == "pre-order":
          result.append(callback(node))

        if node.left is not None:
          dfs_r(node.left, callback, result, order)

        if order == "in-order":
          result.append(callback(node))

        if node.right is not None:
          dfs_r(node.right, callback, result, order)

        if order== "post-order":
          result.append(callback(node))

      return result

    return [] if self.root is None else dfs_r(self.root, callback, [], order)

if __name__ == "__main__":
  orders = ["pre-order", "in-order", "post-order"]
  seed(3413)
  test = [randint(0, 20) for i in range(10)]
  tree = BinarySearchTree()

  for i in test:
    tree.insert(i)

  print(f'list: {test}')
  print(f'tree (bfs): {tree}')

  for order in orders:
    print(f'{order} dfs: {tree.dfs(lambda node: str(node), order)}')

  build_test = [randint(0, 20) for i in range(10)]
  tree.build(build_test)

  print(f'list: {build_test}')
  print(f'tree (bfs): {tree}')

  for order in orders:
    print(f'{order} dfs: {tree.dfs(lambda node: str(node), order)}')