import java.util.*;

public class MatrixTraversal {

    // BFS Implementation
    public static void bfs(int[][] matrix, int start, int goal) {
        int n = matrix.length;
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];

        queue.add(start);
        visited[start] = true;

        System.out.println("BFS Traversal:");
        while (!queue.isEmpty()) {
            int current = queue.poll();
            System.out.println("Visiting node: " + current);

            if (current == goal) {
                System.out.println("Goal node " + goal + " found using BFS!");
                return;
            }

            for (int i = 0; i < n; i++) {
                if (matrix[current][i] == 1 && !visited[i]) { // Check for a connection
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }

        System.out.println("Goal node " + goal + " not found using BFS.");
    }

    // DFS Implementation
    public static void dfs(int[][] matrix, int start, int goal) {
        int n = matrix.length;
        Stack<Integer> stack = new Stack<>();
        boolean[] visited = new boolean[n];

        stack.push(start);

        System.out.println("DFS Traversal:");
        while (!stack.isEmpty()) {
            int current = stack.pop();

            if (!visited[current]) {
                visited[current] = true;
                System.out.println("Visiting node: " + current);

                if (current == goal) {
                    System.out.println("Goal node " + goal + " found using DFS!");
                    return;
                }

                for (int i = n - 1; i >= 0; i--) { // Traverse neighbors in reverse for stack order
                    if (matrix[current][i] == 1 && !visited[i]) {
                        stack.push(i);
                    }
                }
            }
        }

        System.out.println("Goal node " + goal + " not found using DFS.");
    }

    public static void main(String[] args) {
        // Adjacency matrix representation of a graph
        // 0 - A, 1 - B, 2 - C, 3 - D, 4 - E
        int[][] matrix = {
            {0, 1, 1, 0, 0}, // A -> B, C
            {1, 0, 0, 1, 1}, // B -> A, D, E
            {1, 0, 0, 0, 1}, // C -> A, E
            {0, 1, 0, 0, 0}, // D -> B
            {0, 1, 1, 0, 0}  // E -> B, C
        };

        int start = 0; // Start from node A (index 0)
        int goal = 4;  // Goal is node E (index 4)

        // Perform BFS
        bfs(matrix, start, goal);

        // Perform DFS
        dfs(matrix, start, goal);
    }
}
