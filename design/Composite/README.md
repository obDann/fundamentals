# Composite Design Pattern
Allows an object hold other objects of its interface. The example is further extended on a [project I worked on](https://github.com/obDann/project-archive/tree/master/JShell).

### Highlights:
* An interface is made, a *Component*. The example here is a FileSystemObject
* A "dead end", but concrete class exists and implements the Component interface. The example here is a File
* A composite class exists and implements the Component interface as well. The example here is a directory.
  * The composite class usually has an "add method" for any Components, but it is arugable where this method should go on a per-case basis (some literature points that the add method should go into a Component abstract class).
