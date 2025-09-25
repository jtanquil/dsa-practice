class HashEntry():
  def __init__(self, key, val):
    self.key = key
    self.val = val

  def __str__(self):
    return f'{{ key: {self.key}, val: {self.val} }}'