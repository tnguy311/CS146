from collections import defaultdict, deque

def topological_sort_kahn(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    queue = deque([node for node in indegree if indegree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_order) != len(graph):
        return []  
    
    return sorted_order

def topological_sort_bfs(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    queue = deque([node for node in indegree if indegree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_order) != len(graph):
        return []  
    
    return sorted_order

def topological_sort_dfs(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        sorted_order.append(node)
    
    visited = set()
    sorted_order = []
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return sorted_order[::-1]

# Sample input
sample_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Sample
print("Sample Input Graph:")
print(sample_graph)
print()

print("Topological Sort using Kahn's Algorithm:", topological_sort_kahn(sample_graph))
print("Topological Sort using BFS:", topological_sort_bfs(sample_graph))
print("Topological Sort using DFS:", topological_sort_dfs(sample_graph))



      -> B -> D
    /
   A
    \
      -> C -> D

#Kahn's Algorithm Approach (`topological_sort_kahn`):
# - This method starts by counting how many edges are coming into each vertex "in-degree."
#- Then begins with vertices that have an in-degree of 0, adding them to a queue.
#- The algorithm run through the queue removing a vertex and adding it to the sorted list.
#- For each removed vertex, it decreases in-degree of its neighbors.
#- If a neighbor's in-degree becomes 0, it's added to the queue.
#- The process repeats until the queue is empty.
#- If the sorted list's length isn't the same as the number of vertices there's a cycle in the graph.

#BFS Approach (`topological_sort_bfs`):
#- This method calculates the in-degree for each vertex and starts with vertices having an in-degree of 0.
#- It iteratively removes vertices, adds them to the sorted list and decreases the in-degree of their neighbors.
#- If a neighbor's in-degree becomes 0, it's added to the queue for processing.
#- It's similar to Kahn;s algorithm that it checks if the sorted list length matches the number of vertices to detect cycles.

#DFS Approach (`topological_sort_dfs`):
#- This method uses DFS to explore vertices deeply.
#- It visits each vertex, marking it as visited then adds it to the sorted list after visiting its neighbors.
#- It continues the prcess until all vertices are visited.
#- However, This method assumes the input graph doesn't have cycles, so it doesn't explicitly check for them.
