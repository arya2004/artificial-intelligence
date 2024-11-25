
//7. **Best-First Search (Simplified)**: Time \( O(E \cdot \log V) \), Space \( O(V) \).


import java.util.*;

// Custom Node class
class Node {
    String name;
    int heuristic;
    List<Node> neighbors;

    public Node(String name, int heuristic) {
        this.name = name;
        this.heuristic = heuristic;
        this.neighbors = new ArrayList<>();
    }

    public void addNeighbor(Node neighbor) {
        this.neighbors.add(neighbor);
    }
}

public class BestFirstSearchSimple {

    public static void bestFirstSearch(Node start, Node goal) {
        PriorityQueue<Node> openList = new PriorityQueue<>(Comparator.comparingInt(n -> n.heuristic));
        Set<Node> visited = new HashSet<>();

        openList.add(start);

        while (!openList.isEmpty()) {
            Node current = openList.poll();
            System.out.println("Visiting: " + current.name);

            if (current == goal) {
                System.out.println("Goal Found: " + current.name);
                return;
            }

            visited.add(current);

            for (Node neighbor : current.neighbors) {
                if (!visited.contains(neighbor)) {
                    openList.add(neighbor);
                }
            }
        }

        System.out.println("Goal not found.");
    }

    public static void main(String[] args) {
        // Create nodes
        Node A = new Node("A", 3);
        Node B = new Node("B", 2);
        Node C = new Node("C", 1);
        Node D = new Node("D", 4);
        Node E = new Node("E", 0); // Goal node

        // Add neighbors
        A.addNeighbor(B);
        A.addNeighbor(C);
        B.addNeighbor(D);
        C.addNeighbor(E);

        // Run Best-First Search
        bestFirstSearch(A, E);
    }
}
