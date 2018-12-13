# Singleton Design Pattern
Global access to a class that has only one reference

### Highlights:
* The class has a private static variable for the single reference; an instantiation is not needed
* Private constructor
* Public "Factory" method called *getReference()*
* Check if the single reference is null, if it is, create an instantiation and return the existing reference
