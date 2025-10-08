from graph_adt import Vertex, Edge, Graph

class GraphAdjacencyMatrix(Graph):
  def __init__(self, is_directed = False):
    self.graph = []
    self.is_directed = is_directed

  def vertex_count(self):
    return len(self.graph)

  def vertices(self):
    return [i for i in range(len(self.graph))]

  def edge_count(self):
    return len(self.edges())

  def edges(self):
    _edges = []

    for u in range(len(self.graph)):
      for v in range(len(self.graph[u])):
        if u <= v and not self.is_directed:
          continue
        
        _edges.append(self.graph[u][v])

    return _edges    

  def get_edge(self, u, v):
    return self.graph[u][v]

  def degree(self, v, out = True):
    if not self.is_directed:
      return 2 * len(self.incident_edges(v))
    else:
      return len(self.incident_edges(v, out))

  def incident_edges(self, v, out = True):
    if not self.is_directed or out:
      return [edge for edge in self.graph[v] if edge is not None]
    elif self.is_directed and not out:
      return [row[v] for v in self.graph if row[v] is not None]

  def insert_vertex(self, x = None):
    for row in self.graph:
      row.append(None)

    self.graph.append([None for i in range(len(self.graph) + 1)])

  def insert_edge(self, u, v, x = None):
    if self.graph[u][v] is None:
      self.graph[u][v] = Edge(u, v, x)

      if not self.is_directed:
        self.graph[v][u] = Edge(v, u, x)
    else:
      self.graph[u][v].x = x

      if not self.is_directed:
        self.graph[v][u].x = x

  def remove_vertex(self, v):
    del self.graph[v]

    for row in self.graph:
      row.pop(v)

  def remove_edge(self, e):
    u, v = e.u, e.v

    if self.graph[u][v] == e:
      self.graph[u][v] = None

      if not self.is_directed:
        self.graph[v][u] = None

  def __str__(self):
    return "\n".join([" ".join([("0" if edge is None else "1") for edge in row]) for row in self.graph])

if __name__ == "__main__":
  graph = GraphAdjacencyMatrix(is_directed = True)

  for i in range(10):
    graph.insert_vertex(i)
  
  for j in range(9):
    graph.insert_edge(j, j + 1)

  print(graph)

  for v in graph.vertices():
    print(f'{v}:', [f'{e}' for e in graph.incident_edges(v)], f'degree: {graph.degree(v)}')
