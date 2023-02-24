tree= {
    'A': ['B', 'C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F':[]
}

path = list()

def DFS(currentNode,destination,tree,maxDepth,curList):
    print("Checking for destination",currentNode)
    curList.append(currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in tree[currentNode]:
        if DFS(node,destination,tree,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,tree,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,tree,i,curList):
            return True
    return False

if not iterativeDDFS('A','E',tree,4):
    print("Path is not available")
else:
    print("A path exists")
    print(path.pop())
