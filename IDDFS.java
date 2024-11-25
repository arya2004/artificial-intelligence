import java.util.*;

public class IDDFS {

    static class Node {
        int value;
        List<Node> children;

        Node(int value) {
            this.value = value;
            this.children = new ArrayList<>();
        }

        void addChild(Node child) {
            children.add(child);
        }
    }

    public static boolean iddfs(Node root, int target) {
        int depth = 0;

        while (true) {
            System.out.println("Searching at depth: " + depth);
            boolean found = dls(root, target, depth);
            if (found) {
                return true;
            }
            depth++;
        }
    }

    public static boolean dls(Node node, int target, int depth) {
        if (node == null) return false;

        System.out.println("Visiting Node: " + node.value + " at depth: " + depth);

        if (depth == 0 && node.value == target) {
            System.out.println("Found target: " + target);
            return true;
        }

        if (depth > 0) {
            for (Node child : node.children) {
                if (dls(child, target, depth - 1)) {
                    return true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {
        // Create a larger tree
        Node root = new Node(1);

        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        Node node7 = new Node(7);
        Node node8 = new Node(8);
        Node node9 = new Node(9);
        Node node10 = new Node(10);
        Node node11 = new Node(11);
        Node node12 = new Node(12);
        Node node13 = new Node(13);
        Node node14 = new Node(14);
        Node node15 = new Node(15);

        // Level 1
        root.addChild(node2);
        root.addChild(node3);
        root.addChild(node4);

        // Level 2
        node2.addChild(node5);
        node2.addChild(node6);

        node3.addChild(node7);
        node3.addChild(node8);

        node4.addChild(node9);
        node4.addChild(node10);

        // Level 3
        node5.addChild(node11);
        node6.addChild(node12);

        node7.addChild(node13);
        node8.addChild(node14);

        node9.addChild(node15);

        // Set the target to search
        int target = 15;

        // Perform IDDFS
        boolean result = iddfs(root, target);
        if (result) {
            System.out.println("Target " + target + " was found in the tree.");
        } else {
            System.out.println("Target " + target + " was not found in the tree.");
        }
    }
}
