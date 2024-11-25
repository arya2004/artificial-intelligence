//



//1. **Graph Traversal (BFS)**: Time \( O(V + E) \), Space \( O(V) \).
//2. **Graph Traversal (DFS)**: Time \( O(V + E) \), Space \( O(V) \).



import java.util.*;

class Node {
    String name;
    List<Node> neighbors;

    public Node(String name) {
        this.name = name;
        this.neighbors = new ArrayList<>();
    }

    public void addNeighbor(Node neighbor) {
        neighbors.add(neighbor);
    }
}

public class GraphTraversal {

    // BFS Implementation
    public static void bfs(Node start, String goal) {
        Queue<Node> queue = new LinkedList<>();
        Set<Node> visited = new HashSet<>();

        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            System.out.println("Visiting: " + current.name);

            if (current.name.equals(goal)) {
                System.out.println("Goal node " + goal + " found using BFS!");
                return;
            }

            for (Node neighbor : current.neighbors) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }

        System.out.println("Goal node " + goal + " not found using BFS.");
    }

    // DFS Implementation
    public static void dfs(Node start, String goal) {
        Stack<Node> stack = new Stack<>();
        Set<Node> visited = new HashSet<>();

        stack.push(start);

        while (!stack.isEmpty()) {
            Node current = stack.pop();

            if (!visited.contains(current)) {
                visited.add(current);
                System.out.println("Visiting: " + current.name);

                if (current.name.equals(goal)) {
                    System.out.println("Goal node " + goal + " found using DFS!");
                    return;
                }

                for (Node neighbor : current.neighbors) {
                    if (!visited.contains(neighbor)) {
                        stack.push(neighbor);
                    }
                }
            }
        }

        System.out.println("Goal node " + goal + " not found using DFS.");
    }

    public static void main(String[] args) {
        // Creating nodes
        Node a = new Node("A");
        Node b = new Node("B");
        Node c = new Node("C");
        Node d = new Node("D");
        Node e = new Node("E");
        Node f = new Node("F");

        // Building the graph
        a.addNeighbor(b);
        a.addNeighbor(c);
        b.addNeighbor(d);
        b.addNeighbor(e);
        c.addNeighbor(f);

        // Perform BFS
        System.out.println("Performing BFS:");
        bfs(a, "E");

        // Perform DFS
        System.out.println("\nPerforming DFS:");
        dfs(a, "E");
    }
}
