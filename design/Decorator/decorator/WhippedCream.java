package decorator;

public class WhippedCream extends AddOn{

	public WhippedCream(Beverage base) {
		super(base);
		description = base.description + "\n\twith: Whipped Cream";
		cost = base.cost + 1.5;
	}

}
