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

