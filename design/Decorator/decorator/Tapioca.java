package decorator;

public class Tapioca extends AddOn{

	public Tapioca(Beverage base) {
		super(base);
		description = base.description + "\n\twith: Tapioca";
		cost = base.cost + 0.50;
	}

}
