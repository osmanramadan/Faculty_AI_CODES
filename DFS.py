def DFS(tree, start, dest) :
 stack = list()
 visited = list()
 stack.append(start)
 print('Visited', start)
 result = ["Not reachable", list()]
 while stack:
  node = stack.pop()
  visited.append(node)
  if node == dest:
    print('Destination node found', node)
    result[0] = 'Reachable'
    break
  print(node, 'Is not a destination node')
  for child in tree[node]:
    if child not in visited:
      stack.append(child)
 result[1] = visited
 return result
tree={'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
               'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}
result = DFS(tree, 'A', 'H')
print(result[0])
print("Path used to traverse :-", result[1])
