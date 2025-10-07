from graph_adt import Vertex, Edge, Graph

class GraphAdjacencyMap(Graph):
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

    for u in self._edges:
      _edges += [self.edges[u][v] for v in self._edges[u]]

    return _edges

  def get_edge(self, u, v):
    if u in self._edges and v in self._edges[u]:
      return self._edges[u][v]

  def degree(self, v, out = True):
    if not self.is_directed:
      return 2 * len(self.incident_edges(v))
    else:
      return len(self.incident_edges(v, out))

  def incident_edges(self, v, out = True):
    if not self.is_directed or (self.is_directed and out):
      return self._edges[v]
    elif self.is_directed and not out:
      incoming_edges = {}

      for u in self._edges:
        if v in self._edges[u]:
          incoming_edges[u] = self._edges[u][v]

      return incoming_edges

  def insert_vertex(self, x = None):
    if x not in self._edges:
      self._edges[x] = {}

  def insert_edge(self, u, v, x = None):
    if u in self._edges:
      if v in self._edges[u]:
        self._edges[u][v].weight = x

        if not self.is_directed:
          if u in self._edges[v]:
            self._edges[v][u].weight = x

        return self._edges[u][v]
      else:
        new_edge = Edge(u, v, x)
        self._edges[u][v] = new_edge

        if not self.is_directed:
          self._edges[v][u] = Edge(v, u, x)
        
        return new_edge

  def remove_vertex(self, v):
    del self._edges[v]

    for u in self._edges:
      if v in self._edges[u]:
        del self._edges[u][v]

  def remove_edge(self, e):
    if e.u in self._edges and e.v in self._edges[e.u]:
      del self._edges[e.u][e.v]

      if not self.is_directed:
        del self._edges[e.v][e.u]

  def __str__(self):
    return "\n".join([f'{u} : [{', '.join([f'{self._edges[u][v]}' for v in self._edges[u]])}]' for u in self._edges])

if __name__ == "__main__":
  graph = GraphAdjacencyMap(is_directed = False)

  for i in range(10):
    graph.insert_vertex(i)
  
  for j in range(9):
    graph.insert_edge(j, j + 1)

  print(graph)

  for v in graph.vertices():
    print(f'{v}:', [f'{e}' for e in graph.incident_edges(v)], f'degree: {graph.degree(v)}')
