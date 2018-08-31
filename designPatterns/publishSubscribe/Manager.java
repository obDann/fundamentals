import java.util.Observable;
import java.util.Observer;

public class Manager implements Observer {

  public Manager(){

  }


  public void update(Observable obs, Object record){
    Database temp = (Database) obs;
    // does it know which publisher called the update method?
    System.out.println("The Manager says a " + temp.getOperation()
        + "operation was performed" + temp.getRecord());
  }
}
