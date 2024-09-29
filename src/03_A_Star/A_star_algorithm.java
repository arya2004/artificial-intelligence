

import java.util.PriorityQueue;
import java.util.HashSet;
import java.util.Set;
import java.util.List;
import java.util.Comparator;
import java.util.ArrayList;
import java.util.Collections;

public class A_star_algorithm{


    //h scores is the stright-line distance from the current city to Bucharest
    public static void main(String[] args){

        //initialize the graph 
        Node n1 = new Node("Pune",366);
        Node n2 = new Node("Amravati",374);
        Node n3 = new Node("Mumbai",380);
        Node n4 = new Node("Kolhapur",253);
        Node n5 = new Node("Solapur",178);
        Node n6 = new Node("Sangli",193);
        Node n7 = new Node("Ratnagiri",98);
        Node n8 = new Node("Latur",329);
        Node n9 = new Node("Nagpur",244);
        Node n10 = new Node("Nanded",241);
        Node n11 = new Node("SambhajiNagar",242);
        Node n12 = new Node("Nashik",160);
        Node n13 = new Node("Gadchiroli",0);
        Node n14 = new Node("Buldhana",77);

        //initialize the edges


        n1.adjacencies = new Edge[]{
                new Edge(n2,75),
                new Edge(n4,140),
                new Edge(n8,118)
        };

        n2.adjacencies = new Edge[]{
                new Edge(n1,75),
                new Edge(n3,71)
        };

        n3.adjacencies = new Edge[]{
                new Edge(n2,71),
                new Edge(n4,151)
        };

        n4.adjacencies = new Edge[]{
                new Edge(n1,140),
                new Edge(n5,99),
                new Edge(n3,151),
                new Edge(n6,80),
        };

        n5.adjacencies = new Edge[]{
                new Edge(n4,99),

                //178
                new Edge(n13,211)
        };

        n6.adjacencies = new Edge[]{
                new Edge(n4,80),
                new Edge(n7,97),
                new Edge(n12,146)
        };

        n7.adjacencies = new Edge[]{
                new Edge(n6,97),
                new Edge(n13,101),
                new Edge(n12,138)
        };

        n8.adjacencies = new Edge[]{
                new Edge(n1,118),
                new Edge(n9,111)
        };

        n9.adjacencies = new Edge[]{
                new Edge(n8,111),
                new Edge(n10,70)
        };

        n10.adjacencies = new Edge[]{
                new Edge(n9,70),
                new Edge(n11,75)
        };

        n11.adjacencies = new Edge[]{
                new Edge(n10,75),
                new Edge(n12,120)
        };

        n12.adjacencies = new Edge[]{
                new Edge(n11,120),
                new Edge(n6,146),
                new Edge(n7,138)
        };

        n13.adjacencies = new Edge[]{
                new Edge(n7,101),
                new Edge(n14,90),
                new Edge(n5,211)
        };

        n14.adjacencies = new Edge[]{
                new Edge(n13,90)
        };

        AstarSearch(n1,n14);

        List<Node> path = printPath(n14);

        System.out.println("Path: " + path);


    }

    public static List<Node> printPath(Node target){
        List<Node> path = new ArrayList<Node>();

        for(Node node = target; node!=null; node = node.parent){
            path.add(node);
        }

        Collections.reverse(path);

        return path;
    }

    public static void AstarSearch(Node source, Node goal){

        Set<Node> explored = new HashSet<Node>();

        PriorityQueue<Node> queue = new PriorityQueue<Node>(20,
                new Comparator<Node>(){
                    //override compare method
                    public int compare(Node i, Node j){
                        if(i.f_scores > j.f_scores){
                            return 1;
                        }

                        else if (i.f_scores < j.f_scores){
                            return -1;
                        }

                        else{
                            return 0;
                        }
                    }

                }
        );

        //cost from start
        source.g_scores = 0;

        queue.add(source);

        boolean found = false;

        while((!queue.isEmpty())&&(!found)){

            //the node in having the lowest f_score value
            Node current = queue.poll();

            explored.add(current);

            //goal found
            if(current.value.equals(goal.value)){
                found = true;
            }

            //check every child of current node
            for(Edge e : current.adjacencies){
                Node child = e.target;
                double cost = e.cost;
                double temp_g_scores = current.g_scores + cost;
                double temp_f_scores = temp_g_scores + child.h_scores;


                                /*if child node has been evaluated and 
                                the newer f_score is higher, skip*/

                if((explored.contains(child)) &&
                        (temp_f_scores >= child.f_scores)){
                    continue;
                }

                                /*else if child node is not in queue or 
                                newer f_score is lower*/

                else if((!queue.contains(child)) ||
                        (temp_f_scores < child.f_scores)){

                    child.parent = current;
                    child.g_scores = temp_g_scores;
                    child.f_scores = temp_f_scores;

                    if(queue.contains(child)){
                        queue.remove(child);
                    }

                    queue.add(child);

                }

            }

        }

    }

}

class Node{

    public final String value;
    public double g_scores;
    public final double h_scores;
    public double f_scores = 0;
    public Edge[] adjacencies;
    public Node parent;

    public Node(String val, double hVal){
        value = val;
        h_scores = hVal;
    }

    public String toString(){
        return value;
    }
}

class Edge{
    public final double cost;
    public final Node target;

    public Edge(Node targetNode, double costVal){
        target = targetNode;
        cost = costVal;
    }
}