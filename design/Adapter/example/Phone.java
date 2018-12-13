package example;

public abstract class Phone {
	protected String name;

	/**
	 * Returns the name of the phone
	 * @return the name of the phone
	 */
	public String getName() {
		return name;
	}
	
	/**
	 * Charges the phone with the appropriate charging component
	 * @param charger a charging component
	 */
	public abstract void chargeMyPhone(ChargingComponent charger);
	
	/**
	 * Returns the status of the charge
	 * @return the status of the charge
	 */
	public abstract boolean getCharge();
}
