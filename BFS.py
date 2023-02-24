def BFS(tree, start, dest) :
 queue = list()
 visited = list()
 queue.append(start)
 print('Visited', start)
 result = ["Not reachable", list()]
 while queue:
  node = queue.pop(0)
  visited.append(node)
  if node == dest:
    print('Destination node found', node)
    result[0] = 'Reachable'
    break
  print(node, 'Is not a destination node')
  for child in tree[node]:
    if child not in visited:
      queue.append(child)
 result[1] = visited
 return result
tree={'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
               'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}
result = BFS(tree, 'A', 'H')
print(result[0])
print("Path used to traverse :-", result[1])
