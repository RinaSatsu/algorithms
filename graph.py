#TO DO:
# encapsulation
# input validation
# functions to count degree, outgoing/ingoing edges etc. ---- maybe
class Graph:
  def __init__(self, vertices = set(), edges = set(), graph = {}, isDirected = False):
    self.vertices = vertices #set
    self.edges = edges #set of tuples {(A, B)}
    self.graph = graph #dictionary of vertex : set of adjacent edges {A: {B, C}}
    self.isDirected = isDirected

  @classmethod
  def from_vertices_edges(cls, vertices, edges, isDirected = False):
    newGraph = cls(vertices, edges, isDirected = isDirected)
    newGraph.generate_graph()
    return newGraph

  @classmethod
  def from_edges(cls, edges, isDirected = False):
    newGraph = cls(edges = edges, isDirected = isDirected)
    newGraph.vertices_from_edges()
    newGraph.generate_graph()
    return newGraph
  
  @classmethod
  def from_graph(cls, graph, isDirected = False):
    newGraph = cls(graph = graph, isDirected = isDirected)
    newGraph.vertices_from_graph()
    newGraph.edges_from_graph()
    return newGraph

  def find_adjacent_vertices(self, vertex):
    adjacentSet = set()
    if self.isDirected:
      for e in self.edges:
        if e[0] == vertex:
          adjacentSet.add(e[1])
    else:
      for e in self.edges:
        if vertex in e:
          adjacentSet.add(e[e.index(vertex) - 1])
    return adjacentSet

  def vertices_from_edges(self):
    self.vertices = set([v for e in self.edges for v in e])

  def vertices_from_graph(self):
    self.vertices = [key for key in self.graph.keys()]

  def edges_from_graph(self):
    if self.isDirected:
      self.edges = set([(key, v) for key, value in self.graph.items() for v in value])
    else:
      for key, value in self.graph.items():
        for v in value:
          self.edges.add((key, v))
          self.graph[v].remove(key)

  def generate_graph(self):
    for v in self.vertices:
      self.graph.update({v: self.find_adjacent_vertices(v)})

def main():
  vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'J'}
  edges = {('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'E'), ('C', 'F'), ('D', 'F'), ('E', 'F') }
  someGraph = Graph.from_edges(edges)
  print(someGraph.graph)
  someGraphDir = Graph.from_edges(edges, True)
  print(someGraphDir.graph)
  thirdGraph = Graph.from_vertices_edges(vertices, edges)
  print(thirdGraph.graph)

  graph = {'A': {'B', 'C'}, 'B': {'A'}, 'C': {'A'}}
  otherGraph = Graph.from_graph(graph)
  print(otherGraph.vertices)
  print(otherGraph.edges)

if __name__ == '__main__':
  main()