class Deque {

    ListNode head;
    ListNode tail;
    int size;


    public Deque() {
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void append(int value) {
        if (isEmpty()) {
            head = new ListNode(value);
            tail = head;
        } else {
            ListNode newNode = new ListNode(value);
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    public void appendleft(int value) {
        if (isEmpty()) {
            head = new ListNode(value);
            tail = head;
        } else {
            ListNode newNode = new ListNode(value);
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        int value = tail.value;
        if (size == 1) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        size--;
        return value;
    }

    public int popleft() {
        if (isEmpty()) {
            return -1;
        }

        var val = head.value;
        var next = head.next;

        if (next != null) {
            next.prev = null;
            head = next;
        } else {
            head = null;
            tail = null;
        }
        
        size--;
        return val;
    }

}

class ListNode {
    int value;
    ListNode next;
    ListNode prev;

    public ListNode(int value) {
        this.value = value;
    }
}
