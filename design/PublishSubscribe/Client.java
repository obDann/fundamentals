import java.util.Observable;
import java.util.Observer;

public class Client implements Observer {

  public Client(){

  }


  public void update(Observable obs, Object record){
    Database temp = (Database) obs;
    // does it know which publisher called the update method?
    System.out.println("The client says a " + temp.getOperation()
        + "operation was performed" + temp.getRecord());
  }
}
