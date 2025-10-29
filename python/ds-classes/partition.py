from adt import Partition

class Position:
  def __init__(self, element):
    self.element = element
    self.group = None

  def __str__(self):
    return f'{{ element: {self.element}, group: {self.group} }}'

class SequencePartition(Partition):
  def __init__(self):
    self.positions = {}
    self.groups = {}

  def num_clusters(self):
    return len(self.groups.keys())

  def make_group(self, x):
    new_position = Position(x)
    new_group = [x]
    new_position.group = x

    self.positions[x] = new_position
    self.groups[x] = new_group

    return x

  def union(self, p, q):
    left = self.groups[self.positions[p].group]
    right = self.groups[self.positions[q].group]

    # reassign the positions of the shorter group
    # then delete the shorter group
    if len(left) > len(right):
      for position in right:
        self.positions[position].group = left[0]

      self.groups[left[0]] = left + right
      del self.groups[right[0]]
    else:
      for position in left:
        self.positions[position].group = right[0]

      self.groups[right[0]] = right + left
      del self.groups[left[0]]

  def find(self, p):
    return self.groups[self.positions[p].group][0]

  def __str__(self):
    return f'positions: {", ".join([f'{self.positions[position]}' for position in self.positions])}\ngroups:\n{"\n".join([f'{group}: {", ".join([f'{position}' for position in self.groups[group]])}' for group in self.groups])}'

if __name__ == "__main__":
  test = SequencePartition()

  for i in range(10):
    test.make_group(i)

  print(test)

  for i in range(10):
    print(test.find(i))

  test.union(0, 1)
  test.union(2, 3)
  test.union(4, 5)
  test.union(6, 7)
  test.union(8, 9)

  print(test)

  test.union(1, 3)
  test.union(5, 7)

  print(test)

  test.union(3, 9)

  print(test)

  test.union(3, 7)

  print(test)