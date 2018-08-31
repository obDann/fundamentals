import java.util.Observable;
import java.util.Observer;

public class Archival implements Observer {

  public Archival(){

  }


  public void update(Observable obs, Object record){
    Database temp = (Database) obs;
    // does it know which publisher called the update method?
    System.out.println("The archiver says a " + temp.getOperation()
        + "operation was performed" + temp.getRecord());
    System.out.println(record);
  }
}
