package example;

public class iPhoneAdapter extends ChargingComponent{

	AndroidBattery Bat;

	/**
	 * Initialize an adapter from android to iPhone
	 * @param theBat a battery that is strictly for Android Phones
	 */
	public iPhoneAdapter(AndroidBattery theBat) {
		Bat = theBat;
	}
	
	/**
	 * Determines if the phone can charge with this adapter
	 */
	public boolean canCharge(Phone thePhone) {
		Bat.in = "iPhone";
		boolean ret = Bat.canCharge(thePhone);
		Bat.in = "Android";
		return ret;
	}

}
