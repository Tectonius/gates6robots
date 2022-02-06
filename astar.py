from graph import *
from queue import PriorityQueue

def aStarSearch(graph, inttoroom, roomtoxy, start, end, heur, pathHeur):
    q = PriorityQueue()
    q.put((heur(inttoroom, roomtoxy, start, end), [start]))
    explored = []
    while(not q.empty()):
        (v, curr) = q.get()
        if (curr[0] == end):
            return curr
        explored.append(curr[0])
        children = graph.get_children(curr[0])
        for child in children:
            if (child not in explored):
                path = [child] + list(curr)
                value = heur(inttoroom, roomtoxy, child, end) + pathHeur(graph, path)
                q.put((value, path))
    return []


