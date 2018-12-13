class TestObs{
  public static void main(String args[]){
    // create a publisher
    Database database = new Database();

    // Create the subscribers
    Archival archiver = new Archival();
    Client client = new Client();
    Manager manager = new Manager();

    // add subscribers
    database.addObserver(archiver);
    database.addObserver(client);
    database.addObserver(manager);

    // subscribers will be notified by an action
    database.editRecord("delete", "record1");
  }

}
