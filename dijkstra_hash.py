"""
conditions: undirected acyclic graph, no negative weight
three hash table: graph, costs, parents
start (A, 6), (B, 2)
A (final, 1)
B (final, 5), (A, 3)
"""


def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs, parents


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_code = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_code = node
    return lowest_cost_code


def get_path(node):
    path = []
    while node != 'start':
        path.append(parent[node])
        node = parent[node]
    path.reverse()
    return path


if __name__ == '__main__':
    graph = {'start': {'A': 6, 'B': 2}, 'A': {'final': 1}, 'B': {'final': 5, 'A': 3}, 'final': {}}
    infinity = float('inf')
    costs = {'A': 6, 'B': 2, 'final': infinity}
    parents = {'A': 'start', 'B': 'start', 'final': None}
    processed = []
    cost, parent = dijkstra()
    print('Costs: ', cost)
    print('Parents: ', parent)
    path_final = get_path('final')
    path_final.append('final')
    print('Path: ', path_final)
