public class FileSystem {

  // create a single reference
  private static FileSystem singleReference = null;

  // let the constructor be private, only allowing the user to use the
  // factory method
  private FileSystem() {
  }

  /**
   * Returns the only file system
   * @return the only file system
   */
  public FileSystem getFileSystem() {
    // check if the single reference is null
    if (singleReference == null) {
      // if it is, then create a new file system
      singleReference = new FileSystem();
    }
    // then return the file system
    return singleReference;
  }

  // this idea of the file system class is expanded in the MockFileSystem
  // project under the project-archive repository
}
