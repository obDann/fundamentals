# Design Patterns

A Design Pattern is described as a template/repeatable solution to common software engineering problems.

### Design Patterns in this directory


#### Behaviour Design Patterns: Focuses in communication among classes.

[Command:](./Command) Treating classes as commands; the main responsibility of a command is to execute an action

[Iterator:](./Iterator) Allows clients to sequentially traverse through a collection of objects in a class

[Publish Subscribe:](./PublishSubscribe) Allows many objects to automatically react when behaviour of an observable changes

[Null Object:](./NullObject) Avoid checking for nulls in your structure by making your own null object


#### Creational Design Patterns: Focuses in class instantiation.

[Builder:](./Builder) A way to instantiate an object, injecting multiple attributes in a clear and concise way

[Factory](./Factory) A descriptive abstraction of a constructor, allowing multiple ways to instantiate an object without guessing the constructor's purpose

[Singleton:](./Singleton) Global access to a class that has only one reference

#### Structural Design Patterns: Focuses in organizing small pieces to generate large structures

[Adapter:](./Adapter) Lets an object make a request with incompatible (but fully implemented) resources injected into it

[Composite:](./Composite) Allows an object hold other objects of its interface. The example is further extended on a [project I worked on](https://github.com/obDann/project-archive/tree/master/JShell)

[Decorator:](./Decorator) A core object that can have additional properties with each layer

---

# SOLID design principles

Fundamentally all design patterns come from SOLID design principles:

**Single Responsibility Principle:** A class should only have one main, but abstract responsibility; this responsibility should be entirely encapsulated by this class.

**Open/Close Principle:** Open for extension, closed for modification. Objectively, never rewrite code.

Concurrently using the dependency inversion principle, never modify the contracted structure of your code as many other classes may depend on it (to solve this, interfaces/abstract classes may be ideal so that other dependencies know the contract of such class).

The idea of 'extension' portion is to either appropriately add methods to the class or to appropriately inherit the class (and add more methods/change behaviour due to specialization of the class).

**Liskov Substitution Principle:** When to use inheritance and when to use composition

Suppose Class A has methods/attributes w, x, y, z and suppose Class B is described to only have methods/attributes y and z (same methods from class A)

A first-year computer science student would have the basic intuition that Class B should inherit from Class A. However, the Liskov Substitution principle argues otherwise. If Class B inherits from Class A, then clients will have access to methods/attributes to w and x within Class B even though Class B is not intended to have those methods/attributes.

In this case for encapsulation, it is best to use composition (Class B HAS-A Class A). It is only best to use inheritance when Class B can replicate all of Class A's methods/attributes, while providing additions and/or inheritable changes (i.e. method overriding).

**Interface Segregation Principle:** Better to have many small interfaces rather than having few big interfaces. Create interfaces for smaller roles and give all roles to a particular specialized class.

**Dependency Inversion Principle:** High level objects should not depend on low level implementations. This goes hand in hand with dependency injection and mock objects in testing.

* **Unit Testing:** Testing bits of code in isolation, concisely allows refactoring of code while maintaining behaviour
* **Dependency Injection:** When a class that is contracted by an interface, an instantiation of the contracted class is passed into another object's parameters to replicate dependent behaviour, allowing objects to be loosely coupled
* **Mock Object:** An instantiation of a class that is contracted by an interface, mocking the behaviour of a class that is yet to be implemented in a very small scale. Mock objects are mainly used in dependency injection for unit testing

# Agile Methodology

Agile methodology usually consists of the following:

**Product Backlog:** The master list of all functionalities/features desired in the project (typically from the client as a user story)
  * Personas: A representation of users/clients. These are the stereotypical people that will react to your software. Defining personas may help to find any features that are not directly stated by the client.
  * User Stories: A feature in your software that is in the form: "As [persona], I want to be able to [feature], so that [purpose]."
    * Though many places state that defining the purpose is optional, I disagree with it. Defining the purpose helps with sculpting the feature in the event that you can recommend something better.

**Task Backlog:** High level derivation from the product backlog that can be used as directions for coding. Typically, a magnitude is assigned to these tasks in the form of "story points".

**Scrum Meetings:** Frequent meetings during the sprint that answers the following questions. The last one is added since all meetings are supposed to have some purpose:
  * "What did you work on (from the past scrum meeting until now)?"
  * "What will you work on (until the next scrum meeting)?"
  * "Is there anything that you are blocked on?"
  * "What are the main takeaways from this meeting?"

#### Tracking Progress:
Before each sprint, the following may be completed:
* **Sprint Backlog:** The list of tasks that the scrum team is committing to upcoming sprint. Items on the sprint backlog are re-drawn from the Product Backlog, and detailed into a smaller list of things needed to be done.
* **Provisional Burndown Chart:** The expected amount of points completed/"burned" per day. Typically, a chart is drawn to track expected progression.

After or during each sprint, the following are supposed to be used to track progress:
* **Kanban:** An operational way of keeping track of tasks with the team. It is usually a board (or even an excel file) that consists of the tasks to do (using proper allocation), and the completed tasks.
* **Actual burndown chart:** The actual amount of user story points burned during the sprint. Use this to assess your team and even the magnitude of the tasks made in the task backlog.

# Definitions and other tools worth noting

**Encapsulation**: Separating the implementation details from the behaviour exposed to clients

**Inheritance**: "IS-A" relationship between two classes

**Composition**: "HAS-A" relationship between two classes

**CRC (Class Responsibility Collaborator):** A tool used to enforce the Single Responsibility Principle; three main questions exists:
* What is my class
* What responsibilities does my class have?
* What is my class collaborating with?
