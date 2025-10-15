from graph_adjacencymap import GraphAdjacencyMap

# for each vertex in incident edges:
#   visit each incident vertex and add it to vertices
#   call dfs on that
def dfs(graph, incoming_vertex):
  def _dfs(graph, incoming_vertex, visited_vertices):
    incident_vertices = graph.incident_edges(incoming_vertex)

    for outgoing_vertex in incident_vertices:
      if outgoing_vertex not in visited_vertices:
        visited_vertices[outgoing_vertex] = graph.get_edge(incoming_vertex, outgoing_vertex)
        _dfs(graph, outgoing_vertex, visited_vertices)
    
    return visited_vertices

  return _dfs(graph, incoming_vertex, {incoming_vertex: None})

def connected_components(graph):
  components = []

  for vertex in graph.vertices():
    if len(list(filter(lambda x: vertex in x, components))) == 0:
      components.append(dfs(graph, vertex))

  return components

if __name__ == "__main__":
  graph = GraphAdjacencyMap(is_directed = True)

  for i in range(5):
    graph.insert_vertex(i)

  graph.insert_edge(0, 1, 1)
  graph.insert_edge(0, 2, 1)
  graph.insert_edge(1, 2, 1)
  graph.insert_edge(1, 4, 1)
  graph.insert_edge(2, 3, 1)
  graph.insert_edge(3, 1, 1)
  graph.insert_edge(3, 4, 1)
  graph.insert_edge(4, 3, 1)

  print(graph)
  
  for i in range(5):
    visited = dfs(graph, i)
    print(f'dfs on {i}:')
    print({i: f'{visited[i]}' for i in visited})

  two_components = GraphAdjacencyMap()

  for i in range(6):
    two_components.insert_vertex(i)

  two_components.insert_edge(0, 1, 1)
  two_components.insert_edge(1, 2, 1)
  two_components.insert_edge(2, 0, 1)
  two_components.insert_edge(3, 4, 1)
  two_components.insert_edge(4, 5, 1)
  two_components.insert_edge(5, 3, 1)

  print(connected_components(two_components))