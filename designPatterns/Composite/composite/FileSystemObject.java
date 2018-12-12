package composite;

public abstract class FileSystemObject {

	protected String fsoName;
	protected FileSystemObject parent = null;

	public FileSystemObject(String name) {
		fsoName = name;
	}

	protected FileSystemObject getParent() {
		return parent;
	}

	protected void setParent(FileSystemObject theParent) {
		parent = theParent;
	}

	public String pwd() {
		// make some String
		String pwdString = "";
		// get this parent's pwd
		if (parent != null) {
			pwdString += parent.pwd();
		}
		// then add this string 
		pwdString += fsoName;
		return pwdString + "/";
	}
}
