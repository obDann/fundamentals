import java.util.Observable;  // Observable is a publisher

// Database is my publisher
public class Database extends Observable {
  private String operation;
  private String record;

  // constructor
  public Database() {
  }

  // some change has happened
  public void editRecord(String operation, String record) {
    this.operation = operation;
    this.record = record;
    // ensure an object has changed
    setChanged();
    // then notify the observers
    notifyObservers("Yahoo");
  }

  // write some code now, that will notify observers/subscribers that the
  // database has been changed

  public String getRecord() {
    return record;
  }

  public String getOperation() {
    return operation;
  }
}
