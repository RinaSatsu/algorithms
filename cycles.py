#Cycle-detection algorithms
from graph import Graph
from collections import deque
import copy

def cycle_iter(parent, current, visited, graph):
  visited.add(current)
  vertex_stack = deque()
  for v in graph.graph[current]:
    if v == parent:
      continue
    elif v in visited:
      return True
    else:
      vertex_stack.append(v)
  has_cycle = False
  while not has_cycle and len(vertex_stack) > 0: # check all children until we find cycle (has_cycle = true) or until we run out of children
    next = vertex_stack.pop()
    has_cycle = cycle_iter(current, next, visited, graph)
  return has_cycle

def has_cycle_dfs(graph):
  vertices = copy.deepcopy(graph.vertices)
  visited = set()
  has_cycle = False
  while not has_cycle and len(vertices) > 0: # run until we find cycle or until we checked all nodes
    start = vertices.pop()
    visited.add(start)
    has_cycle = cycle_iter(None, start, visited, graph)
    vertices -= visited # remove all nodes we already checked
  return has_cycle



def main():
  vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'}
  edges = {('A', 'B'), ('C', 'D'), ('C', 'E'), ('A', 'F'), ('A', 'G'), ('D', 'E')}
  someGraph = Graph.from_vertices_edges(vertices, edges)
  print(someGraph.graph)

  print(has_cycle_dfs(someGraph))
  

if __name__ == '__main__':
  main()