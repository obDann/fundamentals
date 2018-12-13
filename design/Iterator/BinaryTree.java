import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.ArrayList;

public class BinaryTree<T> implements Iterable<T> {

  private Node<T> root;

  public BinaryTree() {
    root = null;
  }

  public void addDataInTree(T d) {
    Node<T> node = new Node<>(d);
    if (root == null) {
      root = node;
      return;
    }
    root.addData(node);
  }


  public String toString() {
    return _toString(root);
  }

  /**
   * @param n root
   * @return
   */
  private String _toString(Node<T> n) {
    if (n != null)
      return n.data.toString() + _toString(n.left) + _toString(n.right);
    else
      return "";
  }

  private static class Node<T> {
    T data;
    Node<T> left;
    Node<T> right;

    public Node(T d) {
      data = d;
      left = null;
      right = null;
    }

    public String toString() {
      return data.toString();
    }

    private void addData(Node<T> n) {
      Queue<Node<T>> q = new LinkedList<>();
      q.add(this);
      while (true) {
        Node<T> candidate = q.poll();
        if (candidate.left == null) {
          candidate.left = n;
          break;
        } else if (candidate.right == null) {
          candidate.right = n;
          break;
        } else {
          q.add(candidate.left);
          q.add(candidate.right);
        }
      }
    }
  }


  private static class PreOrderIterator<T> implements Iterator<T> {

    Stack<Node<T>> stk;

    public PreOrderIterator(Node<T> root) {
      // TODO Auto-generated constructor stub
      stk = new Stack<>();
      if (root != null)
        stk.add(root);
    }

    @Override public boolean hasNext() {
      // TODO Auto-generated method stub
      return !(stk.isEmpty());
    }

    @Override public T next() {
      // TODO Auto-generated method stub
      if (hasNext()) {
        Node<T> ret = stk.pop();
        if (ret.right != null)
          stk.push(ret.right);
        if (ret.left != null)
          stk.push(ret.left);
        return ret.data;
      }
      return null;
    }
  }


  private static class InOrderIterator<T> implements Iterator<T> {

    Stack<Node<T>> stk;
    Node<T> curr;

    /**
     * Creates an inorder iterator
     *
     * @param root the root of a binary tree
     */
    public InOrderIterator(Node<T> root) {
      stk = new Stack<>();
      curr = root;
    }

    /**
     * Determines if there is a "next" value
     *
     * @return true iff there is a next value
     */
    @Override public boolean hasNext() {
      return !stk.isEmpty() || curr != null;
    }

    /**
     * returns the next possible value
     *
     * @return the next possible value
     */
    @Override public T next() {

      while (curr != null) {
        stk.push(curr);
        curr = curr.left;
      }

      if (hasNext()) {
        curr = stk.pop();

        T ret = curr.data;
        curr = curr.right;
        return ret;
      }

      return null;
    }

  }

  @Override public Iterator<T> iterator() {
    // TODO Auto-generated method stub

    return new InOrderIterator<>(root);
    //return new InOrderIterator<>(root);
  }

  public static void main(String[] args) {
    BinaryTree<Integer> bTree = new BinaryTree<>();
    bTree.addDataInTree(1);
    bTree.addDataInTree(2);
    bTree.addDataInTree(3);
    bTree.addDataInTree(4);
    bTree.addDataInTree(5);
    bTree.addDataInTree(6);
    bTree.addDataInTree(7);
    /*
     *              1
     *             / \
     *      2               3
     *     / \             / \
     *  4       5       6       7
     *
     */
    System.out.println(bTree);
    System.out.println();
    for (Integer item : bTree) {
      System.out.println(item);
    }
  }
}
