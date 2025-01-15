# Breadth-first search
from graph import Graph
from collections import deque

def bfs_traverse(start, graph):
  if start not in graph.vertices:
    print("Error: start node is not in graph")
    return
  visited = set()
  vertex_queue = deque()
  vertex_queue.append(start)
  while len(vertex_queue) != 0:
    current_vertex = vertex_queue.popleft()
    print(current_vertex, end = " ")
    visited.add(current_vertex)
    adjacent = graph.find_adjacent_vertices(current_vertex)
    for v in adjacent:
      if v not in visited and v not in vertex_queue:
        vertex_queue.append(v)
  if not (visited == graph.vertices):
    print(f"\nIsolated vertices: {graph.vertices - visited}")

def main():
  vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'J'}
  edges = {('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'E'), ('C', 'F'), ('D', 'F'), ('E', 'F') }
  someGraph = Graph.from_vertices_edges(vertices, edges, True)
  print(someGraph.graph)

  startNode = 'A'
  bfs_traverse(startNode, someGraph)

if __name__ == '__main__':
  main()