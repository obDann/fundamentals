package composite;

public class Directory extends FileSystemObject{

	public Directory(String name) {
		super(name);
	}

	public void addFso(FileSystemObject fso) {
		fso.setParent(this);
	}
}
