package highlevel;
public class Client {
	// I expect the adaptee's behavior with the resources I have

	/**
	 * Simulating the Adapter Design Pattern
	 * @param args None
	 */
	public static void main(String args[]) {
		Adaptee theInjectedAdaptee = new Adaptee();
		ITarget myTarget = new Adapter(theInjectedAdaptee);
		myTarget.request();
	}
}
