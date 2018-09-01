# Builder Design Pattern
A way to instantiate an object, injecting multiple attributes in a clear and concise way

### Highlights:
* Classes that use the builder design pattern typically uses a nested static class, *Builder*
* The builder class initially takes in required attributes in the constructor
* The builder class "builds" onto itself by its other descriptive methods that returns a builder *return this;*
* The builder class has a *build()* method that returns the intended object with the attributes that is demanded
