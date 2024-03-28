from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1
    
    queue = deque(course for course in range(numCourses) if in_degree[course] == 0)
    count = 0
    while queue:
        course = queue.popleft()
        count += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == numCourses

#Create a graph to represent the courses and their prerequisites using dictionar and the values are lists of prerequisite courses.
#Then check if there are any cycles in the graph by using a recursive DFS approach. Cycles indicate that the courses cannot be completed due to circular dependencies.
#Then traverse the graph, keeping track of visited nodes to detect cycles.
#Perform a topological sort on the graph, assuming that there are no cycles. This gives an order in which the courses can be taken, while make sure that prerequisites are fulfilled.
#Once the sorted order, revisit through it and ensure that all courses can be taken. If any course is encountered that hasn't been marked as completed, it return False. Otherwise, return True.
