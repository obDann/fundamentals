package decorator;

public class RainbowJelly extends AddOn{

	public RainbowJelly(Beverage base) {
		super(base);
		description = base.description + "\n\twith: Rainbow Jelly";
		cost = base.cost + 0.35;
	}

}
