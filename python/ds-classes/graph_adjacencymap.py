from graph_adt import Vertex, Edge, Graph

class GraphAdjacencyMap(Graph):
  def __init__(self, is_directed = False):
    self._outgoing = {}
    self._incoming = {} if is_directed else self._outgoing

  def is_directed(self):
    return self._outgoing != self._incoming

  def vertex_count(self):
    return len(self.vertices())

  def vertices(self):
    return self._outgoing.keys()

  def edge_count(self):
    return len(self.edges())

  def edges(self):
    _edges = set()

    for u in self._outgoing:
      _edges = _edges.union([self._outgoing[u][v] for v in self._outgoing[u]])

    return _edges

  def get_edge(self, u, v):
    if u in self._outgoing and v in self._outgoing[u]:
      return self._outgoing[u][v]

  def degree(self, v, out = True):
    _incident_edges = self.incident_edges(v, out)

    return len(_incident_edges) if self.is_directed else 2 * len(_incident_edges)

  def incident_edges(self, v, out = True):
    return self._outgoing[v] if out else self._incoming[v]

  def insert_vertex(self, x = None):
    if x not in self._outgoing:
      self._outgoing[x] = {}

    if self.is_directed():
      self._incoming[x] = {}

  def insert_edge(self, u, v, x = None):
    if u in self._outgoing and v in self._outgoing[u]:
      self._outgoing[u][v].weight = x
      return self._outgoing[u][v]
    else:
      edge = Edge(u, v, x)
      self._outgoing[u][v] = edge
      self._incoming[v][u] = edge
      return edge

  def remove_vertex(self, v):
    del self._outgoing[v]
    
    if self.is_directed():
      del self._incoming[v]

    for u in self._incoming:
      if v in self._incoming[u]:
        del self._incoming[u][v]

  def remove_edge(self, e):
    if self._outgoing[e.u][e.v] == e:
      del self._outgoing[e.u][e.v]
      del self._incoming[e.v][e.u]

  def __str__(self):
    if self.is_directed():
      return "\n".join([f'{u}:\noutgoing: [{'; '.join([f'{self._outgoing[u][v]}' for v in self._outgoing[u]])}] out-degree: {self.degree(u, True)}\nincoming: [{'; '.join([f'{self._incoming[u][v]}' for v in self._incoming[u]])}] in-degree: {self.degree(u, False)}' for u in self._outgoing])
    else:
      return "\n".join([f'{u}:\nedges: [{'; '.join([f'{self._outgoing[u][v]}' for v in self._outgoing[u]])}] degree: {self.degree(u, True)}' for u in self._outgoing])

if __name__ == "__main__":
  graph = GraphAdjacencyMap(is_directed = False)

  for i in range(10):
    graph.insert_vertex(i)

  print(f'graph:\n{graph}')
  
  for j in range(10):
    graph.insert_edge(j % 10, (j + 1) % 10, j)

  print(f'graph:\n{graph}\nvertex_count: {graph.vertex_count()}\nedge_count: {graph.edge_count()}')

  for j in range(5):
    edge = graph.get_edge(j % 10, (j + 1) % 10)
    print(f'deleting edge {j % 10} to {(j + 1) % 10}')
    graph.remove_edge(edge)
    print(f'graph:\n{graph}\nvertex_count: {graph.vertex_count()}\nedge_count: {graph.edge_count()}')

  graph.remove_vertex(0)
  print(f'graph:\n{graph}\nvertex_count: {graph.vertex_count()}\nedge_count: {graph.edge_count()}')

  graph.remove_vertex(9)
  print(f'graph:\n{graph}\nvertex_count: {graph.vertex_count()}\nedge_count: {graph.edge_count()}')
