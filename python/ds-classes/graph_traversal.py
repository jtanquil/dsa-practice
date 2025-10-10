from graph_adjacencymap import GraphAdjacencyMap

# for each vertex in incident edges:
#   visit each incident vertex and add it to vertices
#   call dfs on that
def dfs(graph, incoming_vertex):
  def _dfs(graph, incoming_vertex, visited_vertices):
    incident_edges = graph.incident_edges(incoming_vertex).keys()

    for outgoing_vertex in incident_edges:
      if outgoing_vertex not in visited_vertices:
        visited_vertices[outgoing_vertex] = [graph.get_edge(incoming_vertex, outgoing_vertex)] if incoming_vertex not in visited_vertices else visited_vertices[incoming_vertex] + [graph.get_edge(incoming_vertex, outgoing_vertex)]
        return _dfs(graph, outgoing_vertex, visited_vertices)
      else:
        continue
      
    return visited_vertices

  return _dfs(graph, incoming_vertex, {})

def get_weights(graph):
  path = {}

  for i in graph.vertices():
    paths = dfs(graph, i)
    weights = { j: sum(_edge.weight for _edge in paths[j]) for j in paths.keys() }
    path[i] = { i: weights }

  return path

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
    print(f'{i}: ' + "\n".join(f'{", ".join([f'{ele}' for ele in visited[edge]])}' for edge in visited))

  print(get_weights(graph))