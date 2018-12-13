package nullObject;

public class RealNode implements Node{
	private int value;
	private Node leftChild;
	private Node rightChild;

	/**
	 * Instantiates a node with no children
	 * @param val the value of the node
	 */
	public RealNode(int val) {
		value = val;
		leftChild = new NullNode();
		rightChild = new NullNode();
	}
	
	
	/**
	 * Instantiates a node with only a left child
	 * @param val the value of the node
	 * @param lc the left child
	 */
	public RealNode(int val, Node lc) {
		value = val;
		leftChild = lc;
		rightChild = new NullNode();
	}
	
	/**
	 * Instantiates a node with children
	 * @param val the value of the node
	 * @param lc the left node
	 * @param rc the right node
	 */
	public RealNode(int val, Node lc, Node rc) {
		value = val;
		leftChild = lc;
		rightChild = rc;
	}

	public int sum() {
		return value + leftChild.sum() + rightChild.sum();
	}

}
