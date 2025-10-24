from heap import HeapNode, MutableMinHeap
from graph_adjacencymap import GraphAdjacencyMap

def dijkstra(graph, vertex):
  dist = {}
  vertex_heap = MutableMinHeap()

  for _vertex in graph.vertices():
    _vertex_node = HeapNode(_vertex, float('inf') if _vertex != vertex else 0)
    dist[_vertex] = { 'node': _vertex_node, 'last_edge': None }
    vertex_heap.insert(_vertex_node)

  while len(vertex_heap) > 0:
    print(vertex_heap)
    incoming_vertex = vertex_heap.delete_min().key

    for outgoing_vertex in graph.incident_edges(incoming_vertex):
      if dist[outgoing_vertex]["node"].val > dist[incoming_vertex]["node"].val + graph.get_edge(incoming_vertex, outgoing_vertex).weight:
        vertex_heap.update(outgoing_vertex, dist[incoming_vertex]["node"].val + graph.get_edge(incoming_vertex, outgoing_vertex).weight)
        dist[outgoing_vertex]["last_edge"] = graph.get_edge(incoming_vertex, outgoing_vertex)

  return dist

if __name__ == "__main__":
  test = GraphAdjacencyMap()

  test.insert_vertex("SFO")
  test.insert_vertex("LAX")
  test.insert_vertex("DFW")
  test.insert_vertex("MIA")
  test.insert_vertex("BWI")
  test.insert_vertex("JFK")
  test.insert_vertex("ORD")
  test.insert_vertex("PVD")
  test.insert_vertex("BOS")

  test.insert_edge("SFO", "LAX", 337)
  test.insert_edge("SFO", "DFW", 1464)
  test.insert_edge("SFO", "BOS", 2704)
  test.insert_edge("SFO", "ORD", 1846)
  test.insert_edge("LAX", "DFW", 1235)
  test.insert_edge("LAX", "MIA", 2342)
  test.insert_edge("DFW", "ORD", 802)
  test.insert_edge("DFW", "MIA", 1121)
  test.insert_edge("DFW", "JFK", 1391)
  test.insert_edge("ORD", "BOS", 867)
  test.insert_edge("ORD", "PVD", 849)
  test.insert_edge("ORD", "JFK", 740)
  test.insert_edge("ORD", "BWI", 621)
  test.insert_edge("BOS", "MIA", 1258)
  test.insert_edge("BOS", "JFK", 187)
  test.insert_edge("PVD", "JFK", 144)
  test.insert_edge("JFK", "BWI", 184)
  test.insert_edge("JFK", "MIA", 1090)
  test.insert_edge("BWI", "MIA", 946)

  dijkstra_result = dijkstra(test, "BWI")

  for vertex in dijkstra_result:
    print(f'BWI to {vertex}, dist: {dijkstra_result[vertex]["node"].val}, last_edge: {dijkstra_result[vertex]["last_edge"]}')
