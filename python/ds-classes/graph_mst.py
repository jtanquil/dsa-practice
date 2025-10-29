from heap import HeapNode, MutableMinHeap
from graph_adjacencymap import GraphAdjacencyMap
from partition import SequencePartition

def prim_jarnik(graph):
  edges = {}
  vertices = set()
  vertex_heap = MutableMinHeap()
  
  for _vertex in graph.vertices():
    _vertex_node = HeapNode(_vertex, float('inf') if len(vertex_heap) > 0 else 0)
    vertex_heap.insert(_vertex_node)
    
    edges[_vertex] = { 'node': _vertex_node, 'edge' : None }

  while len(vertex_heap) > 0:
    incoming_vertex = vertex_heap.delete_min().key
    vertices.add(incoming_vertex)
    
    for outgoing_vertex in graph.incident_edges(incoming_vertex):
      edge = graph.get_edge(incoming_vertex, outgoing_vertex)
      is_already_in_tree = outgoing_vertex in vertices # don't add if the incoming/outgoing pair is already represented

      if edges[outgoing_vertex]["node"].val > edge.weight and not is_already_in_tree:
        vertex_heap.update(outgoing_vertex, edge.weight)
        edges[outgoing_vertex]["edge"] = edge

  return [ edges[vertex]["edge"] for vertex in edges if edges[vertex]["edge"] is not None ]

def kruskal(graph):
  clusters = SequencePartition()
  edges = []
  edge_heap = MutableMinHeap()

  for vertex in graph.vertices():
    clusters.make_group(vertex)

  for edge in graph.edges():
    edge_heap.insert(HeapNode(edge, edge.weight))

  while len(edge_heap) > 0:
    edge = edge_heap.delete_min().key

    if clusters.find(edge.u) != clusters.find(edge.v):
      edges.append(edge)
      clusters.union(clusters.find(edge.u), clusters.find(edge.v))

    if clusters.num_clusters() == 1:
      break

  return edges

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

  prim_jarnik_result = prim_jarnik(test)

  for edge in prim_jarnik_result:
    print(f'edge: {edge}')

  kruskal_result = kruskal(test)

  print("---")

  for edge in kruskal_result:
    print(f'edge: {edge}')