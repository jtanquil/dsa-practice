from graph_adt import Vertex, Edge, Graph

class GraphAdjacencyList(Graph):
  def __init__(self, is_directed = False):
    self._edges = {}
    self.is_directed = is_directed

  def vertex_count(self):
    return len(self.vertices())

  def vertices(self):
    return self._edges.keys()

  def edge_count(self):
    return len(self.edges())

  def edges(self):
    _edges = []

    for vertex in self._edges:
      _edges += self._edges[vertex]

    return _edges

  def get_edge(self, u, v):
    edge = None

    for _edge in self._edges[u]:
      if _edge.v == v:
        edge = _edge
        return edge

  def degree(self, v, out = True):
    if not self.is_directed:
      return 2 * len(self.incident_edges(v))
    else:
      return len(self.incident_edges(v, out))

  def incident_edges(self, v, out = True):
    if not self.is_directed or (self.is_directed and out):
      return self._edges[v]
    elif self.is_directed and not out:
      incoming_edges = []

      for u in self._edges:
        for _edge in self._edges[u]:
          if _edge.v == v:
            incoming_edges.append(_edge)
            break

      return incoming_edges

  def insert_vertex(self, x = None):
    if x not in self._edges:
      self._edges[x] = []

  def insert_edge(self, u, v, x = None):
    for edge in self._edges[u]:
      if edge.v == v:
        edge.x = x
        
        if not self.is_directed:
          for edge in self._edges[v]:
            if edge.u == u:
              edge.x = x
              break
        
        return
        
    self._edges[u].append(Edge(u, v, x))
    
    if not self.is_directed:
      self._edges[v].append(Edge(v, u, x))

  def remove_vertex(self, v):
    del self._edges[v]

    for u in self._edges:
      for edge in self._edges[u]:
        if edge.v == v:
          del edge

  def remove_edge(self, e):
    u = e.u
    v = e.v

    for edge in self._edges[u]:
      if edge.v == v:
        del edge

    if not self.is_directed:
      for edge in self.edges[v]:
        if edge.u == u:
          del edge

  def __str__(self):
    return "\n".join([f'{u} : [{', '.join([f'{v}' for v in self._edges[u]])}]' for u in self._edges])

if __name__ == "__main__":
  graph = GraphAdjacencyList(is_directed = True)

  for i in range(10):
    graph.insert_vertex(i)
  
  for j in range(9):
    graph.insert_edge(j, j + 1)

  print(graph)

  for v in graph.vertices():
    print(f'{v}:', [f'{e}' for e in graph.incident_edges(v)], f'degree: {graph.degree(v)}')
