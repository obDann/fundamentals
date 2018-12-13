package highlevel;
public class Adapter implements ITarget{
	// given an adaptee I must be able to do the
	// adaptee's request
	
	private Adaptee adaptee;
	
	/**
	 * Instantiate an adapter, given an adaptee
	 * @param injAdaptee an adaptee
	 */
	public Adapter(Adaptee injAdaptee) {
		adaptee = injAdaptee;
	}

	/**
	 * Do 
	 */
	public void request() {
		adaptee.specificRequest();
	}
}
