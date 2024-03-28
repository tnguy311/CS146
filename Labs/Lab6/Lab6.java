import java.util.*;

public class CourseSchedule {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[0]).add(prerequisite[1]);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] recStack = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i] && hasCycle(graph, i, visited, recStack)) {
                return false;
            }
        }
        return true;
    }

    private boolean hasCycle(List<List<Integer>> graph, int v, boolean[] visited, boolean[] recStack) {
        if (recStack[v]) return true; 
        if (visited[v]) return false; 

        visited[v] = true;
        recStack[v] = true;

        for (int neighbor : graph.get(v)) {
            if (hasCycle(graph, neighbor, visited, recStack)) {
                return true;
            }
        }

        recStack[v] = false;
        return false;
    }

    public static void main(String[] args) {
        CourseSchedule courseSchedule = new CourseSchedule();
        int[][] prerequisites1 = {{1, 0}};
        int[][] prerequisites2 = {{1, 0}, {0, 1}};
        System.out.println("Test Case 1: " + courseSchedule.canFinish(2, prerequisites1)); 
        System.out.println("Test Case 2: " + courseSchedule.canFinish(2, prerequisites2)); 
    }
}


//Create a graph to represent the courses and their prerequisites using a dictionary where keys represent courses and values are lists of prerequisite courses.
//Then check if there are any cycles in the graph by using a recursive (DFS) approach. Cycles mean that the courses cannot be completed due to circular dependencies.
//During DFS traversal maintain two arrays 'visited' to keep track of visited nodes and 'recStack' to detect cycles.
//Perform a topological sort assuming that there are no cycles. This gives order in which the courses can be taken while ensuring that prerequisites are fulfilled.
//Once the oder is sorted, revisit the order and ensure that all courses can be taken. If any course is encountered that hasn't been marked as completed return False, Otherwise, return True.
