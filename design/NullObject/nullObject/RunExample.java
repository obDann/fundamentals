package nullObject;

public class RunExample {
	
	public static void main(String args[]) {
		/**
		 * Make a Tree like the following
		 * 
		 *                   5
		 *                /     \
		 *               4       3
		 *             /  \
		 *            2    7
		 *           /
		 *          1 
		 */
		RealNode oneLeaf = new RealNode(1);
		RealNode twoInternal = new RealNode(2, oneLeaf);
		RealNode sevenLeaf = new RealNode(7);
		RealNode fourInternal = new RealNode(4, twoInternal, sevenLeaf);
		RealNode threeLeaf = new RealNode(3);
		RealNode root = new RealNode(5, fourInternal, threeLeaf);
		System.out.println(root.sum());
	}

}
