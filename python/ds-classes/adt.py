from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
  @abstractmethod
  def build(self, iter):
    """Builds a sequence from an iterable."""

  @abstractmethod
  def __len__(self):
    """Returns the length of the sequence."""
  
  @abstractmethod
  def __iter__(self):
    """Returns the stored items, one-by-one, in sequence order."""

  @abstractmethod
  def __getitem__(self, i):
    """Returns the element at index i of the sequence."""

  @abstractmethod
  def __setitem__(self, i, val):
    """Sets the item and index i to val."""

  @abstractmethod
  def insert_at(self, i, val):
    """Add val as the ith item."""

  @abstractmethod
  def delete_at(val, i):
    """Remove and return the ith item."""

  def insert_first(self, val):
    """Inserts val as the first item."""
    self.insert_at(0, val)

  def delete_first(self):
    """Remove and return the first item."""
    self.delete_at(0)

  def insert_last(self, val):
    """Inserts val as the last item."""
    self.insert_at(len(self), val)

  def delete_last(self):
    """Remove and return the last item."""
    self.delete_at(len(self) - 1)

class Set(metaclass = ABCMeta):
  @abstractmethod
  def build(self, iter):
    """Builds a set from an iterable."""

  @abstractmethod
  def __len__(self):
    """Returns the number of stored items."""

  @abstractmethod
  def __getitem__(self, key):
    """Returns the stored item with the given key."""

  @abstractmethod
  def __setitem__(self, key, val):
    """Add val to the set with the given key (overwrite self[key] if it exists)."""

  @abstractmethod
  def __delitem__(self, key):
    """Remove and return the stored item with the given key."""

  @abstractmethod
  def iter_ord(self):
    """Return the stored items one-by-one in key order."""

  @abstractmethod
  def find_min(self):
    """Return the stored item with smallest key."""

  @abstractmethod
  def find_max(self):
    """Return the stored item with largest key."""

  @abstractmethod
  def find_next(self, key):
    """Return the stored item with the smallest key larger than key."""

  @abstractmethod
  def find_prev(self, key):
    """Return the stored item with the largest key smaller than key."""