class mySolution {
    public TreeNode sortedListToBST(ListNode head) {
        return put(head, null);
    }

    private TreeNode put(ListNode front, ListNode back) {
        if (front == back) {
            return null;
        }
        ListNode fast = front;
        ListNode slow = front;
        while (fast != back && fast.next != back) {
            fast = fast.next.next;
            slow = slow.next;
        }
        TreeNode root = new TreeNode(slow.val);
        root.left = put(front, slow);
        root.right = put(slow.next, back);
        return root;
    }
}