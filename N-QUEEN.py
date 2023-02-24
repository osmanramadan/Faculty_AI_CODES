class Node:

    def __init__(self, state, parent=None, depth=0, action=None):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):
        x, result = self, [self]
        while x.PARENT_NODE:
            result.append(x.PARENT_NODE)
            x = x.PARENT_NODE
        return result

    def display(self):
        print(self.STATE, ' ', self.DEPTH, )


def make_node(state):
    return Node(state)


def insert(node, queue):
    queue[:0] = [node]
    return queue


def insert_all(list, queue):
    for node in list:
        insert(node, queue)
    return queue


def remove_first(queue):
    if len(queue) != 0:
        first = queue[0]
        queue[0:1] = []
        return first
    return []


def expand(node):
    successors = []

    for result in successor_fin(node.STATE):
        s = Node(node)
        s.STATE = result
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = insert(s, successors)
    return successors


def tree_search(problem, fringe):
    initial = initial_state[problem]
    nd = make_node(initial)
    fringe = insert(nd, fringe)
    while True:
        node = remove_first(fringe)
        if goal_test[problem] == node.STATE:
            return node.path()
        success = expand(node)

        fringe = insert_all(success, fringe)


def successor_fin(state):
    global N
    if state[-1] is not None:
        return ['solution']
    else:
        def place(col, row):
            new = state[:]
            new[col] = row
            return new
            print(new)
    col = state.index(None)
    return [place(col, row) for row in range(N) if not conflicted(state, row, col)]


def conflicted(state, row, col):
    for c in range(col):
        if conflict(row, col, state[c], c):
            return True
    return False


def conflict(row1, col1, row2, col2):
    return (row1 == row2 or col1 == col2 or row1 - col1 == row2 - col2 or row1 + col1 == row2 + col2)


problem = 'N Queens'
goal_test = {'N Queens': 'solution'}
initial_state = {}


def run(n):
    global N, initial_state
    N = n
    initial_state = {'N Queens': [None] * n}
    for node in tree_search(problem, []):
        node.display()
run(4)
