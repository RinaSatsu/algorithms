# Depth-first search
from graph import Graph
from collections import deque

def dfs(start, graph):
  if start not in graph.vertices:
    print("Error: start node is not in graph")
    return
  visited = set()
  vertex_stack = deque()
  vertex_stack.append(start)
  while len(vertex_stack) != 0:
    current_vertex = vertex_stack.pop()
    print(current_vertex, end = " ")
    visited.add(current_vertex)
    adjacent = graph.find_adjacent_vertices(current_vertex)
    for v in adjacent:
      if v not in visited and v not in vertex_stack:
        vertex_stack.append(v)
  if not (visited == graph.vertices):
    print(f"\nUreachable vertices: {graph.vertices - visited}")
  

def main():
  vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'J'}
  edges = {('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'E'), ('C', 'F'), ('D', 'F'), ('E', 'F') }
  someGraph = Graph.from_vertices_edges(vertices, edges)
  print(someGraph.graph)

  startNode = 'A'
  dfs(startNode, someGraph)

if __name__ == '__main__':
  main()