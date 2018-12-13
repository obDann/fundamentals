package decorator;

public abstract class Beverage {
	
	protected String description;
	protected double cost;

	/**
	 * Returns the description of the beverage
	 * @return the description of the beverage
	 */
	public String getDescription() {
		return description;
	};

	/**
	 * Returns the cost of the beverage
	 * @return the cost of the beverage
	 */
	public Double getCost() {
		return cost;
	};

}
