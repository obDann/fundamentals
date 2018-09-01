# Publish Subscribe Pattern
Allows many objects to automatically react when behaviour of an observable changes

### Highlights:
* A class that reacts to an observable is called an observer
* Observers implement the "Observer" class, thus it is necessary to have an *update()* method to react to an observer
* An observable extends from the class "Observable", where the "Observable" class can add/remove observers
* If behaviour of an observable changed, it is in protocol to call *setChanged()* and then *notifyObservers("with an optional communicative pipe that need not be a string")*
