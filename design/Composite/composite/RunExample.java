package composite;

public class RunExample {
	
	public static void main(String args[]) {
		Directory root = new Directory("");
		File someFile1 = new File("file1");
		File someFile2 = new File("file2");
		File someFile3 = new File("file3");
		File someFile4 = new File("file4");
		Directory subDir1 = new Directory("d1");
		Directory subDir2 = new Directory("d2");
		Directory subDir3 = new Directory("d3");
		root.addFso(someFile1);
		root.addFso(subDir1);
		root.addFso(subDir2);
		subDir1.addFso(subDir3);
		subDir2.addFso(someFile2);
		subDir3.addFso(someFile3);
		subDir3.addFso(someFile4);
		/*Making a file system that looks like the following:
		 * 
		 *  \
		 *    file1
		 *    d1
		 *      d3
		 *        File3
		 *        File4
		 *    d2
		 *      file2
		 * 
		 */
		
		System.out.println(subDir3.pwd());
		System.out.println(someFile1.pwd());
		System.out.println(someFile2.pwd());
		System.out.println(someFile3.pwd());
		System.out.println(someFile4.pwd());
	}

}
