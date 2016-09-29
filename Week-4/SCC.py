import sys
sys.setrecursionlimit(10 ** 6)
explored_nodes = []
leaders = {}
finishing_times = {}
t = 0
s = 0
def dfs(graph,node):
    global explored_nodes, finishing_times, leaders, s, t
    explored_nodes.append(node)
    leaders[node] = s
    if node in graph:
        for n in graph[node]:
            if n not in explored_nodes:
                dfs(graph,n)
    t+=1
    finishing_times[node] = t
    
def dfs_loop(graph):
    global explored_nodes, finishing_times, leaders, s, t
    for i in xrange(len(graph.keys()),0,-1):
        if i not in explored_nodes:
            s = i
            dfs(graph,i)

def dfs_loop2(graph):
    global explored_nodes, finishing_times, leaders, s, t, neworder
    for i in l:
        if i not in explored_nodes:
            s = i
            dfs(graph,i)

print 'Creating Graph'
graph = {}
with open('graph.txt', 'r') as f:
    for line in f:
    	s,t = line.rstrip().split(' ')
    	s,t = int(s), int(t)
    	if s not in graph:
            graph[s] = [t]
        else:
            graph[s].append(t)

print 'Creating Reverse Graph'
rev_graph ={}
for k,v in graph.items():
    for num in v:
        if num not in rev_graph:
            rev_graph[num] = [k]
        else:
            rev_graph[num].append(k)

print 'First Pass'
dfs_loop(graph)
print 'First Pass Done'

l = []
for i in xrange(len(finishing_times.keys())):
    v=list(finishing_times.values())
    k=list(finishing_times.keys())
    l.append(k[v.index(max(v))])
    del finishing_times[k[v.index(max(v))]]
neworder = l
explored_nodes = []
leaders = {}
s = 0

print 'Second Pass'
dfs_loop2(rev_graph)
print 'Second Pass Done'

lead = {}
for k,v in leaders.items():
    if v in lead:
        lead[v]+=1
    else:
        lead[v] = 1

v=list(lead.values())
while v:
    print max(v)
    v.remove(max(v))
