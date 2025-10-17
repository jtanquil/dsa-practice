from graph_adjacencymap import GraphAdjacencyMap
from graph_traversal import dfs, connected_components

def vertex_has_cycle(graph, starting_vertex):
  def _vertex_has_cycle(graph, incoming_vertex, visited_vertices, ancestors):
    incident_vertices = graph.incident_edges(incoming_vertex)

    for outgoing_vertex in incident_vertices:
      if outgoing_vertex in ancestors:
        return True
    
      if outgoing_vertex not in visited_vertices:
        visited_vertices[outgoing_vertex] = graph.get_edge(incoming_vertex, outgoing_vertex)
        new_ancestors = ancestors.copy()
        new_ancestors[outgoing_vertex] = True
        return _vertex_has_cycle(graph, outgoing_vertex, visited_vertices, new_ancestors)

    return False

  return _vertex_has_cycle(graph, starting_vertex, {starting_vertex: None}, {starting_vertex: True})

def has_cycle(graph):
  components = connected_components(graph)

  for component in components:
    if vertex_has_cycle(graph, list(component["visited_vertices"].keys())[0]):
      return True

  return False

# find a vertex with no incoming edges
# put it at the front of the order
# remove the vertex and its incident edges
# keep track of removed vertices and edges
# repeat while there are still unvisited vertices
def topological_sort(graph):
  visited_vertices = []
  current_vertices = list(graph.vertices())

  while len(current_vertices) > 0:
    for vertex in current_vertices:
      if vertex not in visited_vertices:
        adjusted_degree = graph.degree(vertex, out = False)

        for _vertex in visited_vertices:
          if graph.get_edge(_vertex, vertex) is not None:
            adjusted_degree -= 1

        if adjusted_degree == 0:
          visited_vertices.append(vertex)
          current_vertices.remove(vertex)

  return visited_vertices

if __name__ == "__main__":
  no_cycle = GraphAdjacencyMap(is_directed = True)

  for i in range(5):
    no_cycle.insert_vertex(i)

  no_cycle.insert_edge(0, 1, 1)
  no_cycle.insert_edge(0, 2, 1)
  no_cycle.insert_edge(0, 3, 1)
  no_cycle.insert_edge(0, 4, 1)
  no_cycle.insert_edge(1, 2, 1)
  no_cycle.insert_edge(2, 3, 1)
  no_cycle.insert_edge(3, 4, 1)

  print(has_cycle(no_cycle))

  no_cycle.insert_edge(4, 3, 1)

  print(has_cycle(no_cycle))

  sort_test = GraphAdjacencyMap(is_directed = True)

  for letter in ["A", "B", "C", "D", "E", "F", "G", "H"]:
    sort_test.insert_vertex(letter)

  sort_test.insert_edge("A", "C", 1)
  sort_test.insert_edge("A", "D", 1)
  sort_test.insert_edge("B", "D", 1)
  sort_test.insert_edge("B", "F", 1)
  sort_test.insert_edge("C", "D", 1)
  sort_test.insert_edge("C", "E", 1)
  sort_test.insert_edge("C", "H", 1)
  sort_test.insert_edge("D", "F", 1)
  sort_test.insert_edge("E", "G", 1)
  sort_test.insert_edge("F", "G", 1)
  sort_test.insert_edge("F", "H", 1)
  sort_test.insert_edge("G", "H", 1)

  print(connected_components(sort_test))
  print(topological_sort(sort_test))