from graph_adjacencymap import GraphAdjacencyMap
from graph_traversal import connected_components

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
    if vertex_has_cycle(graph, list(component.keys())[0]):
      return True

  return False

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