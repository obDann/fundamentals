# Iterator Design Pattern
Allows clients to sequentially traverse through a collection of objects in a class

### Highlights:
* The class that uses the iterator design pattern implements an *iterable*; it is necessary to have an *iterator()* method that returns an iterator
* Typically, there exists a nested class, and it is contracted to implement an *iterator*; it is necessary to have *hasNext()* and *next()* methods within the nested class
