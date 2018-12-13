# Command Design Pattern
Treating classes as commands; the main responsibility of a command class is to execute an action

### Highlights:
* The class that is in control of executing commands has the commands in a hash table, allowing the controller to unknowingly execute a command (i.e. through user input) via reflection. Doing this greatly reduces the number of conditional statments
* Commands are typically composed of an interface/abstract class; the commands are contracted to (at the very least) have a type of an *execute(…)* method
