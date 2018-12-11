package decorator;

public class RunExample {

	public static void main(String args[]) {
		Beverage niceSmoothie = new WhippedCream(new RainbowJelly(new Smoothie()));
		Beverage niceSlush = new RainbowJelly(new Slush());
		Beverage plainSmoothie = new Tapioca(new Smoothie());
		
		System.out.println(niceSmoothie.getDescription());
		System.out.println("\tcost: $" + niceSmoothie.getCost().toString() + "\n\n");
		
		System.out.println(niceSlush.getDescription());
		System.out.println("\tcost: $" + niceSlush.getCost().toString() + "\n\n");
		
		System.out.println(plainSmoothie.getDescription());
		System.out.println("\tcost: $" + plainSmoothie.getCost().toString());
		
	}
}
