from collections import deque
"""
Breadth First Search -> BFS
Operate Time: O(Vertice + Edge)
Graph: Get 'Thom', directed graph, unweighted graph
You -> Bob, Alice, Claire -> level one
Bob -> Anna, Peggy -> level two
Alice -> Peggy -> level two
Claire -> Thom, Jone -> level two
"""
graph = dict()
graph['You'] = ['Bob', 'Alice', 'Claire']  # hash table
graph['Bob'] = ['Anna', 'Peggy']
graph['Alice'] = ['Peggy']
graph['Claire'] = ['Thom', 'Jone']
graph['Anna'] = []
graph['Peggy'] = []
graph['Thom'] = []
graph['Jone'] = []


def search_BFS(name):
    # 创建一个双向列表
    search_queue = deque()
    search_queue += graph['You']
    searched = []  # 检查过的人不必检查，否则可能无限循环
    while search_queue:
        print('The queue is: ', search_queue)
        person = search_queue.popleft()
        if person not in searched:
            if person == name:
                print('I find the Thom!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    search_BFS('Thom')

