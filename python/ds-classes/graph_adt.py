from abc import ABCMeta, abstractmethod

class Vertex():
  def __init__(self, val):
    self.val = val

  def __str__(self):
    return f'{self.val}'

class Edge():
  def __init__(self, u, v, weight = None):
    self.u = u
    self.v = v
    self.weight = weight

  def endpoints(self):
    return (self.u, self.v)
  
  def opposite(self, vertex):
    if vertex == self.u:
      return self.v
    elif vertex == self.v:
      return self.u

  def __str__(self):
    return f'u: {self.u}, v: {self.v}, weight: {self.weight}'

class Graph(metaclass = ABCMeta):
  @abstractmethod
  def vertex_count(self):
    pass

  @abstractmethod
  def vertices(self):
    pass

  @abstractmethod
  def edge_count(self):
    pass

  @abstractmethod
  def edges(self):
    pass

  @abstractmethod
  def get_edge(self, u, v):
    pass

  @abstractmethod
  def degree(self, v, out = True):
    pass

  @abstractmethod
  def incident_edges(self, v, out = True):
    pass

  @abstractmethod
  def insert_vertex(self, x = None):
    pass

  @abstractmethod
  def insert_edge(self, u, v, x = None):
    pass
  
  @abstractmethod
  def remove_vertex(self, v):
    pass

  @abstractmethod
  def remove_edge(self, e):
    pass