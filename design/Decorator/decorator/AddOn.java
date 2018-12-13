package decorator;

public abstract class AddOn extends Beverage{
	
	protected Beverage previousDrink;
	
	public AddOn(Beverage base) {
		previousDrink = base;
	}

	public Beverage remove() {
		return previousDrink;
	}

}
