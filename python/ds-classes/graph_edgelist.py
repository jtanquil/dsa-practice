from graph_adt import Vertex, Edge, Graph

class GraphEdgeList(Graph):
  def __init__(self, is_directed = False):
    self._vertices = []
    self._edges = []
    self.is_directed = is_directed

  def vertex_count(self):
    return len(self._vertices)

  def vertices(self):
    return self._vertices

  def edge_count(self):
    return len(self._edges)

  def edges(self):
    return self._edges

  def get_edge(self, u, v):
    for edge in self._edges:
      if edge.u == u and edge.v == v:
        return edge
    
    return -1

  def degree(self, v, out = True):
    return len(self.incident_edges(v, out))

  def incident_edges(self, v, out = True):
    if not self.is_directed:
      return [edge for edge in self._edges if (edge.u == v or edge.v == v)]
    elif self.is_directed and out:
      return [edge for edge in self._edges if edge.u == v]
    elif self.is_directed and not out:
      return [edge for edge in self._edges if edge.v == v]

  def insert_vertex(self, x = None):
    new_vertex = Vertex(x)
    self._vertices.append(new_vertex)
    return new_vertex

  def insert_edge(self, u, v, x = None):
    new_edge = Edge(u, v, x)
    self._edges.append(new_edge)
    return new_edge

  def remove_vertex(self, v):
    for edge in self._edges:
      if edge.u == v or edge.v == v:
        del edge

    self._vertices.remove(v)

  def remove_edge(self, e):
    for edge in self._edges:
      if edge == e:
        del edge

  def __str__(self):
    return f'vertices: [{[f'{v}' for v in self._vertices]}]\nedges: [{[f'{e}' for e in self._edges]}]\nis_directed: {self.is_directed}'

if __name__ == "__main__":
  graph = GraphEdgeList()

  for i in range(10):
    graph.insert_vertex(i)
  
  for j in range(9):
    graph.insert_edge(graph.vertices()[j], graph.vertices()[j + 1])

  print(graph)

  for v in graph.vertices():
    print(f'{v}:', [f'{e}' for e in graph.incident_edges(v)], f'degree: {graph.degree(v)}')
