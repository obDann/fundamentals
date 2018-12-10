package example;

public class IPhone extends Phone{
	// a specialized phone
	
	private boolean charge;
	
	/**
	 * Initialize the phone
	 */
	public IPhone() {
		charge = false;
		name = "iPhone";
	}

	/**
	 * Charges the phone with the appropriate charging component
	 */
	public void chargeMyPhone(ChargingComponent charger) {
		if (charger.canCharge(this)) {
			charge = true;
			System.out.println("The iPhone has been charged");
		}
	}

	@Override
	public boolean getCharge() {
		return charge;
	}
}
