class AdjacencyListGraph:
  def __init__(self, vertices = 3):
    self._list = { i: set() for i in range(vertices) }

  def add_edge(self, out_vertex, in_vertex):
    if (out_vertex not in self._list):
      print(f'error: edge {out_vertex} is not in the graph')
    elif (out_vertex == in_vertex):
      print('error: self-loops are not allowed')
    else:
      self._list[out_vertex].add(in_vertex)

  def get_shortest_path_tree(self, source_vertex):
    previous_level_set = set()
    previous_level_set.add(source_vertex)
    points_reached = set().union(previous_level_set)
    tree = { i: None for i in self._list }
    distances = { i: None for i in self._list }
    current_distance = 1
    current_level_set = set()

    while (len(previous_level_set) > 0):
      for vertex in previous_level_set:
        for neighbor in self._list[vertex] - points_reached:
          current_level_set.add(neighbor)
          if tree[neighbor] is None:
            tree[neighbor] = vertex
            distances[neighbor] = current_distance

      points_reached = points_reached.union(current_level_set)
      previous_level_set, current_level_set = current_level_set, set()
      current_distance += 1

    return { 'tree': tree, 'distances': distances }

  def __str__(self):
    adjacencies = []

    for vertex in self._list:
      adjacencies.append(f'{vertex}: {self._list[vertex] if len(self._list[vertex]) > 0 else 'None'}')

    return '\n'.join(adjacencies)

if __name__ == "__main__":
  test = AdjacencyListGraph(5)
  test.add_edge(0, 1)
  test.add_edge(0, 2)
  test.add_edge(1, 2)
  test.add_edge(1, 4)
  test.add_edge(2, 3)  
  test.add_edge(3, 1)
  test.add_edge(3, 4)
  test.add_edge(4, 3)

  print(test)

  for i in range(5):
    print(test.get_shortest_path_tree(i))