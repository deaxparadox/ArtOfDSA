class Node {
    int data;
    Node next = null;
}


public class Stack {

    public Node head = null;

//    public Stack() {
//        head = new Node();
//    }

    public void push(int data) {
        Node new_node;
        if (head == null) {
            new_node = new Node();
            new_node.data = data;
            head = new_node;
        } else {
            new_node = new Node();
            new_node.data = data;
            new_node.next = head;
            head = new_node;
        }
    }

    public void print_stack() {
        Node temp = head;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }


    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(1);
        s.push(1);
        s.push(3);
        s.push(6);
        s.push(1121);
        s.print_stack();
    }
}

