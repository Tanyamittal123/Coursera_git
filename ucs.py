from queue import PriorityQueue
def buildgraph():
    graph = {}
    e = int(input("Enter number of edges"))
    print("Enter edges as source destination cost")
    for i in range(e):
        src,dest,cost = input().split()
        cost = int(cost)
        if src not in graph:
            graph[src] = []
        graph[src].append((dest,cost))
    return graph
def usc(start,goal,graph):
    explored = set()
    pq = PriorityQueue()
    pq.put((0,start,[start]))
    while not pq.empty():
        cost,curnode,path = pq.get()
        if curnode == goal:
            return cost,path
        if curnode in explored:
            continue
        explored.add(curnode)
        for neighbour,ecost in graph.get(curnode,[]):
            if neighbour not in explored:
                totalcost = cost + ecost
                pq.put((totalcost,neighbour,path+[neighbour]))
    return None, float('inf')
graph = buildgraph()
start = input("Enter starting node")
end = input("Enter ending node")
cost,path = usc(start,end,graph)
if path:
    print(f"Path : {'->'.join(path)}",)
    print("Cost : ",cost)
else:
    print("No path found")