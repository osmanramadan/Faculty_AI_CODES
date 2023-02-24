problem = "go to l"
initial_state = {"go to l": 'A'}
goal_test = {"go to l": 'L'}
state_space = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
               'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}


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
    stat_space_node = state_space[node.STATE]
    for result in stat_space_node:
        s = Node(node)
        s.STATE = result
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = insert(s, successors) #visited
    return successors


def tree_search(problem, fringe):
    initial = initial_state[problem]#'A'
    nd = make_node(initial)
    fringe = insert(nd, fringe)
    while True:
        node = remove_first(fringe)
        if goal_test[problem] == node.STATE:#check if state equal to problem
            return node.path()
        success = expand(node)
        for i in success:
            if goal_test[problem] == i.STATE: return node.path()
        fringe = insert_all(success, fringe)


def run():
    print('solution path\nState Depth')
    for node in tree_search(problem, []):
        node.display()
run()