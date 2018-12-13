# Null Object Design Pattern
Avoid checking for nulls in your structure by making your own null object

### Highlights:
* Make an interface to define the behaviour of your structure. In this example, it is a Node.
* Make a *null class* that implements the interface. Implement appropriately. In this example, it is a NullNode.
* Make a *real class* that implements the interface. It uses the *null class* where the composition-property is not injected. This can be seen in the RealNode upon different types of instantiation.
* The example of benefit is seen in the sum() method of the RealNode.
