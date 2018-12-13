# Adapter
Lets an object make a request with incompatible (but fully implemented) resources injected into it.

### Highlights:
* Two interfaces are made, one relies on the other. In the example I provided, a Phone depends on a Battery.
* However, suppose a dependent class is incompatible with the only other independent class instantiated. In the example I provided, I used an iPhone and an Android Battery.
* In this case, an *Adapter* is made so that the two objects are compatible (possibly changing underlying implementation through protected fields). In the example I provided, it is an iPhone adapter.
* The dependent object can sufficiently make the request, by having the adapter wrap the independent object.
