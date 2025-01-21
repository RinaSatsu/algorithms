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

def cycle_dir_iter(current, visited, cur_path, graph):
  visited.add(current)
  cur_path.append(current)
  vertex_stack = deque()
  for v in graph.graph[current]:
    if v in visited and v in cur_path:
      return True
    else:
      vertex_stack.append(v)
  has_cycle = False
  while not has_cycle and len(vertex_stack) > 0: # check all children until we find cycle (has_cycle = true) or until we run out of children
    next = vertex_stack.pop()
    has_cycle = cycle_dir_iter(next, visited, cur_path, graph)
  cur_path.remove(current)
  return has_cycle

def has_cycle_dfs(graph):
  vertices = copy.deepcopy(graph.vertices)
  visited = set()
  has_cycle = False
  if graph.isDirected:
    current_path = deque()
    start = next(iter(graph.vertices))
    while not has_cycle and len(vertices) > 0: # run until we find cycle or until we checked all nodes
      start = vertices.pop()
      has_cycle =  cycle_dir_iter(start, visited, current_path, graph)
      vertices -= visited
  else:
    while not has_cycle and len(vertices) > 0: # run until we find cycle or until we checked all nodes
      start = vertices.pop()
      has_cycle = cycle_iter(None, start, visited, graph)
      vertices -= visited # remove all nodes we already checked
  return has_cycle

def main():
  vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'}
  edges = {('A', 'B'), ('C', 'D'), ('C', 'E'), ('A', 'F'), ('A', 'G'), ('D', 'E'), ('B', 'C')}
  someGraph = Graph.from_vertices_edges(vertices, edges, True)
  print(someGraph.graph)

  print(has_cycle_dfs(someGraph))

if __name__ == '__main__':
  main()