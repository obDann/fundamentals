# Design Patterns

A Design Pattern is described as a template/repeatable solution to common software engineering problems.

### Design Patterns in this directory
[Builder:](./Builder) A way to instantiate an object, injecting multiple attributes in a clear and concise way

[Command:](./Command) Treating classes as commands; the main responsibility of a command is to execute an action

[Factory](./Factory) A descriptive abstraction of a constructor, allowing multiple ways to instantiate an object without guessing the constructor's purpose

[Iterator:](./Iterator) Allows clients to sequentially traverse through a collection of objects in a class

[Publish Subscribe:](./publishSubscribe) Allows many objects to automatically react when behaviour of an observable changes

[Singleton:](./Singleton) Global access to a class that has only one reference

---

# Definitions and other things worth noting

**Encapsulation**: Separating the implementation details from the behaviour exposed to clients  
**Inheritance**: "IS-A" relationship between two classes  
**Composition**: "HAS-A" relationship between two classes  

### Liskov Substitution Principle: When to use inheritance and when to use composition

Suppose Class A has methods/attributes w, x, y, z and suppose Class B is described to only have methods/attributes y and z (same methods from class A)

A first-year computer science student would have the basic intuition that Class B should inherit from Class A. However, the Liskov Substitution principle argues otherwise. If Class B inherits from Class A, then clients will have access to methods/attributes to w and x within Class B even though Class B is not intended to have those methods/attributes.

In this case for encapsulation, it is best to use composition (Class B HAS-A Class A). It is only best to use inheritance when Class B can replicate all of Class A's methods/attributes, while providing additions and/or inheritable changes (i.e. method overriding).

---

**Single Responsibility Principle:** A class should only have one main, but abstract responsibility; this responsibility should be entirely encapsulated by this class  
**CRC (Class Responsibility Collaborator):** A tool used to enforce the Single Responsibility Principle; three main questions exists:
* What is my class
* What responsibilities does my class have?
* What is my class collaborating with?

---

**Unit Testing:** Testing bits of code in isolation, concisely allows refactoring of code while maintaining behaviour  
**Dependency Injection:** When a class that is contracted by an interface, an instantiation of the contracted class is passed into another object's parameters to replicate dependent behaviour, allowing objects to be loosely coupled  
**Mock Object:** An instantiation of a class that is contracted by an interface, mocking the behaviour of a class that is yet to be implemented in a very small scale. Mock objects are mainly used in dependency injection for unit testing

---

### Scrum Methodology: Iterative incremental methodology

**Product Backlog:** The master list of all functionalities desired in the project (typically from the client as a user story)  
**Sprint Backlog:** The list of tasks that the scrum team is committing that they will complete in the current sprint. Items on the sprint backlog are re-drawn from the Product Backlog, and detailed into a smaller list of things needed to be done.  
**Scrum Meetings:** Frequent meetings during the sprint that answers the following questions:
* "What did you work on (yesterday)?"
* "What will you work on (until the next scrum meeting)?"
* "Is there anything that you are blocked on?"
