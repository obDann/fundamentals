package example;

public abstract class ChargingComponent {
	// a basic charging component that determines if it can charge a phone

	protected String in;
	
	public boolean canCharge(Phone thePhone) {
		if (thePhone.name != in) {
			System.out.println("cannot charge phone");
			return false;
		}
		System.out.println("can charge phone");
		return true;
	}

	
}
