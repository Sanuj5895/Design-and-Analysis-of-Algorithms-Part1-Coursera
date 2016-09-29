import random
import math
import copy

class Adjacency(object):
    def __init__(self, node, edge):
        self.node = node
        self.edge = edge

    def contract(self, other):
        self.node += other.node
        self.edge = [i for i in self.edge + other.edge
                     if i not in self.node]

    def __repr__(self):
        return 'Adjacency(node = %r, edge = %r)' % (self.node, self.edge)

def cut(graph):
    if len(graph) == 2:
        return graph
    else:
        rand_pick = random.choice(graph)
        merge_node = random.choice(rand_pick.edge)
        merge_pick = [i for i in graph if merge_node in i.node]
        rand_pick.contract(merge_pick[0])
        graph.remove(merge_pick[0])
        return cut(graph)


def min_cut(graph):
    trial_nu = int(math.pow(len(graph), 1) * math.log(len(graph)))
    min_cross = float('inf')
    for i in range(trial_nu):
        #!!!must call cut on a DEEP COPY of the graph!!!
        trial = cut(copy.deepcopy(graph))
        cut_cross = len(trial[0].edge)
        if cut_cross < min_cross:
            min_cross = cut_cross
            out = trial
    return out, min_cross


file_in = open('graph.txt')
data = [[[int(line.split()[0])], [int(i) for i in line.split()[1:]]]
        for line in file_in]
graph = [Adjacency(i[0], i[1]) for i in data]
return min_cut(graph)
