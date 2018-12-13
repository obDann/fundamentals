package example;

public class RunExample {

	public static void main(String args[]) {
		// create a phone and a battery
		Phone myPhone = new IPhone();
		AndroidBattery myBattery = new AndroidBattery();
		// state the initial state of the phone
		System.out.println("My phone is not charged");
		// attempt to charge the phone with the android battery
		myPhone.chargeMyPhone(myBattery);

		// check if the phone is still not charged
		if (!myPhone.getCharge()) {
			System.out.println("My phone is still not charged");
		}
		
		// create the adapter and charge it
		iPhoneAdapter adapter = new iPhoneAdapter(myBattery);
		myPhone.chargeMyPhone(adapter);
		if (!myPhone.getCharge()) {
			System.out.println("My phone is still not charged");
		}
		else {
			System.out.println("My phone is charged");
		}
	}
}
