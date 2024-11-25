//5. **Iterative Deepening DFS (IDDFS)**: Time \( O(b^d) \), Space \( O(d) \).
import java.util.ArrayList;
import java.util.List;
class Node {
    String name;
    List<Node> children;

    public Node(String name) {
        this.name = name;
        this.children = new ArrayList<>();
    }

    public void addChild(Node child) {
        children.add(child);
    }
}

public class IDDFS {
    public static boolean depthLimitedSearch(Node current, String goal, int depth) {
        if (current == null) return false;
        if (depth == 0) {
            return current.name.equals(goal);
        }
        if (depth > 0) {
            for (Node child : current.children) {
                if (depthLimitedSearch(child, goal, depth - 1)) {
                    return true;
                }
            }
        }
        return false;
    }

    public static boolean iterativeDeepeningSearch(Node start, String goal, int maxDepth) {
        for (int depth = 0; depth <= maxDepth; depth++) {
            if (depthLimitedSearch(start, goal, depth)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // Creating nodes
        Node root = new Node("A");
        Node b = new Node("B");
        Node c = new Node("C");
        Node d = new Node("D");
        Node e = new Node("E");
        Node f = new Node("F");

        // Building the graph
        root.addChild(b);
        root.addChild(c);
        b.addChild(d);
        b.addChild(e);
        c.addChild(f);

        // Performing IDDFS
        String goal = "E";
        int maxDepth = 3;
        boolean found = iterativeDeepeningSearch(root, goal, maxDepth);

        if (found) {
            System.out.println("Goal node " + goal + " found!");
        } else {
            System.out.println("Goal node " + goal + " not found within depth " + maxDepth);
        }
    }
}
