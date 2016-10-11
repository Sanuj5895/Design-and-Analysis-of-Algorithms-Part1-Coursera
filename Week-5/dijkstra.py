def dijkstra(graph,src):
        global visited, distances
        for i in xrange(1,201):
            minW = 1000000
            for node in visited:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        new_distance = distances[node] + graph[node][neighbor]
                        if new_distance < minW:
                            minW = new_distance
                            minNbour = neighbor
            if minW == 1000000:
                continue
            distances[minNbour] = minW
            visited.append(minNbour)

visited = []
distances = {}

if __name__ == "__main__":
    global visited, distances
    graph = {}
    with open('dijkstraData.txt', 'r') as f:
        for line in f:
            line = line.rstrip().split('\t')
            node = int(line[0])
            line = line[1:]
            for ch in line:
                v,w = ch.split(',')
                v=int(v)
                w=int(w)
                if node not in graph:
                    graph[node] = {v:w}
                else:
                    graph[node][v] = w

    visited.append(1)
    distances[1] = 0
    dijkstra(graph,1)
    print distances[7],distances[37],distances[59],distances[82],distances[99],distances[115],distances[133],distances[165],distances[188],distances[197]
