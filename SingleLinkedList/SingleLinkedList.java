class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

class SingleLinkedList {
    Node head;

    public void pushfirstOfNode(int newData) {
        Node newNode = new Node(newData);
        newNode.next = head;
        head = newNode;
    }

    public void pushNodeAtEnd(int newData) {
        Node newNode = new Node(newData);
        if (head == null) {
            head = newNode;
            return;
        }

        Node temp = head;
        while (temp.next != null)
            temp = temp.next;
        temp.next = newNode;
    }

    public void printLinkedList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data);
            if (temp.next != null)
                System.out.print(" --> ");
            temp = temp.next;
        }

    }

    public static void main(String[] args) {
        SingleLinkedList s = new SingleLinkedList();
        // s.pushfirstOfNode(1);
        // s.pushfirstOfNode(2);
        // s.pushfirstOfNode(3);
        // s.pushfirstOfNode(4);

        s.pushNodeAtEnd(1);
        s.pushNodeAtEnd(2);
        s.pushNodeAtEnd(3);
        s.pushNodeAtEnd(4);

        s.printLinkedList();

    }

}