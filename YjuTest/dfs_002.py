def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            print(i, '도는중')
            print(visited)

graph = [
    [],
    [2, 3, 8], # 1번 노드 연결
    [1, 7], # 2번 노드 연결
    [1, 4, 5], # 3번 노드 연결
    [3, 5], # 4번 노드 연결
    [3, 4], # 5번 노드 연결
    [7], # 6번 노드 연결
    [2, 6, 8], # 7번 노드 연결
    [1, 7] # 8번 노드 연결
]

visited = [False] * 9

dfs(graph, 1, visited)