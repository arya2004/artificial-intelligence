import java.util.*;

class Node {
    int x, y; // Position in the grid
    int g; // Cost from start to current node
    int h; // Heuristic cost to the goal
    Node parent; // Parent node to trace the path

    public Node(int x, int y, int g, int h, Node parent) {
        this.x = x;
        this.y = y;
        this.g = g;
        this.h = h;
        this.parent = parent;
    }

    public int getF() {
        return g + h;
    }
}

public class AStarSearch {
    private static final int[][] DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // Up, Right, Down, Left

    public static List<Node> aStar(int[][] grid, int[] start, int[] goal) {
        PriorityQueue<Node> openSet = new PriorityQueue<>(Comparator.comparingInt(Node::getF));
        Set<String> closedSet = new HashSet<>();

        Node startNode = new Node(start[0], start[1], 0, heuristic(start, goal), null);
        openSet.add(startNode);

        while (!openSet.isEmpty()) {
            Node current = openSet.poll();

            if (current.x == goal[0] && current.y == goal[1]) {
                return reconstructPath(current);
            }

            closedSet.add(current.x + "," + current.y);

            for (int[] dir : DIRECTIONS) {
                int newX = current.x + dir[0];
                int newY = current.y + dir[1];

                if (isValid(grid, newX, newY) && !closedSet.contains(newX + "," + newY)) {
                    int newG = current.g + 1;
                    Node neighbor = new Node(newX, newY, newG, heuristic(new int[]{newX, newY}, goal), current);
                    openSet.add(neighbor);
                }
            }
        }

        return Collections.emptyList(); // Return empty list if no path found
    }

    private static boolean isValid(int[][] grid, int x, int y) {
        return x >= 0 && y >= 0 && x < grid.length && y < grid[0].length && grid[x][y] == 0;
    }

    private static int heuristic(int[] node, int[] goal) {
        return Math.abs(node[0] - goal[0]) + Math.abs(node[1] - goal[1]); // Manhattan Distance
    }

    private static List<Node> reconstructPath(Node node) {
        List<Node> path = new ArrayList<>();
        while (node != null) {
            path.add(node);
            node = node.parent;
        }
        Collections.reverse(path);
        return path;
    }

    public static void main(String[] args) {
        int[][] grid = {
                {0, 0, 0, 1, 0},
                {1, 1, 0, 1, 0},
                {0, 0, 0, 0, 0},
                {0, 1, 1, 1, 1},
                {0, 0, 0, 0, 0}
        };

        int[] start = {0, 0};
        int[] goal = {4, 4};

        List<Node> path = aStar(grid, start, goal);

        if (path.isEmpty()) {
            System.out.println("No path found!");
        } else {
            System.out.println("Path:");
            for (Node node : path) {
                System.out.println("(" + node.x + ", " + node.y + ")");
            }
        }
    }
}
