def Dijkstra(AG, AS, AD = None):
    unvisited = []
    for i in AG.keys():
        unvisited.append(i)
    D = dict()
    for v in unvisited:
        D[v] = [[],float('inf')]
    D[AS][1] = 0.0
    while len(unvisited) > 0:
        minD, curr = min([(D[n][1],n) for n in unvisited])
        D[curr][0].append(curr)
        if curr == AD:
            return AD, D[AD]
        for n, d in AG[curr].items():
            if n in unvisited:
                currd = minD + d
                if currd < D[n][1]:
                    D[n][1] = currd
                    D[n][0] = D[curr][0][:]
        unvisited.remove(curr)
    return D 
 
graph = dict()
for vertex in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph[vertex] = {}
graph['A'].update({'B':9})
graph['A'].update({'C':7})
graph['A'].update({'F':13})
graph['B'].update({'C':15})
graph['B'].update({'D':10})
graph['C'].update({'A':9})
graph['C'].update({'B':2})
graph['C'].update({'F':10})
graph['D'].update({'B':6})
graph['D'].update({'E':15})
graph['E'].update({'D':6})
graph['E'].update({'F':9})
graph['F'].update({'A':14})
D = Dijkstra(graph,'A')
print("Shortest paths are: ")
print(D)
