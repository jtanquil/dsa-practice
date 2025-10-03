from ABC import ABCMeta, abstractmethod

class Vertex():
  def __init__(self, val):
    self.val = val

  def __str__(self):
    return f'{self.val}'

class Edge():
  def __init__(self, ingoing, outgoing, weight = None):
    self.ingoing = ingoing
    self.outgoing = outgoing
    self.weight = weight

  def endpoints(self):
    return (self.ingoing, self.outgoing)
  
  def opposite(self, vertex):
    if vertex == self.ingoing:
      return self.outgoing
    elif vertex == self.outgoing:
      return self.ingoing

class Graph(metaclass = ABCMeta):
  @abstractmethod
  def vertex_count(self):

  @abstractmethod
  def vertices(self):

  @abstractmethod
  def edge_count(self):

  @abstractmethod
  def edges(self):

  @abstractmethod
  def get_edge(self, u, v):

  @abstractmethod
  def degree(self, v, out = True):

  @abstractmethod
  def incident_edges(self, v, out = True):

  @abstractmethod
  def insert_vertex(self, x = None):

  @abstractmethod
  def insert_edge(self, u, v, x = None):
  
  @abstractmethod
  def remove_vertex(self, v):

  @abstractmethod
  def remove_edge(self, e):