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

  def insert(self, val, tree):
    if self.val < val:
      if self.right is None:
        self.right = BSTNode(val)
        self.right.parent = self
      else:
        self.right.insert(val, tree)

      self.height = 1 + max(self.right.height, 0 if self.left is None else self.left.height)
    else:
      if self.left is None:
        self.left = BSTNode(val)
        self.left.parent = self
      else:
        self.left.insert(val, tree)

      self.height = 1 + max(self.left.height, 0 if self.right is None else self.right.height)

    if self.is_imbalanced():
      self.rebalance(tree)

  def update_height(self):
    left_height = 0 if self.left is None else self.left.height
    right_height = 0 if self.right is None else self.right.height
    max_subtree_height = max(left_height, right_height)

    self.height = 0 if max_subtree_height == 0 else max_subtree_height + 1

  def rebalance(self, tree):
    skew = self.skew()

    if skew == 2:
      right_child = self.right
      right_child_skew = right_child.skew()

      if right_child_skew >= 0:
        self.left_rotate(tree)
      elif right_child_skew < 0:
        right_child.right_rotate(tree)
        self.left_rotate(tree)
    elif skew == -2:
      left_child = self.left
      left_child_skew = left_child.skew()

      if left_child_skew <= 0:
        self.right_rotate(tree)
      elif left_child_skew > 0:
        left_child.left_rotate(tree)
        self.right_rotate(tree)

  def left_rotate(self, tree):
    parent, right, right_left = self.parent, self.right, self.right.left

    if parent is not None:
      right.parent = parent

      if self == parent.left:
        parent.left = right
      if self == parent.right:
        parent.right = right
    else: # if self has no parent, then it's the root
      tree.root = right
      right.parent = None

    right.left = self
    self.right = right_left
    self.parent = right
    self.update_height()
    right.update_height()

  def right_rotate(self, tree):
    parent, left, left_right = self.parent, self.left, self.left.right

    if parent is not None:
      left.parent = parent

      if self == parent.left:
        parent.left = left
      elif self == parent.right:
        parent.right = left
    else:
      tree.root = left
      left.parent = None
    
    left.right = self
    self.left = left_right
    self.parent = left
    self.update_height()
    left.update_height()

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
      self.root.insert(val, self)

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

  def debug_print(self):
    return self.bfs(lambda node: f'node: {node}, left: {node.left}, right: {node.right}, parent: {node.parent}, height: {node.height}, skew: {node.skew()}')

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
  print(f'list: {build_test}')
  tree.build(build_test)

  print(f'tree (bfs): {tree}')

  for order in orders:
    print(f'{order} dfs: {tree.dfs(lambda node: str(node), order)}')

  print("\n".join(tree.debug_print()))