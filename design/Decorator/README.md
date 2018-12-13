# Decorator
A core object that can have additional properties with each layer.

### Highlights:
* An interface is made, this is called a *Component*. In the example I provided, it is called a Beverage
* All *bases* implement a Component. In the example I provided, there are two: a Slush and a Smoothie
* A *decorator* is an interface that also implements a Component. In the example I provided, this is an AddOn
  * The different types of decorators are supposed to inject a Component. In the example I provided, a possible example is smoothie with tapioca. You must have a beverage already instantiated before a Tapioca decorator can get instantiated.
