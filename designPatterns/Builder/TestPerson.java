public class TestPerson {

  public static void main(String[] args) {

    Person Hermione = new Person.Builder("Hermione", "Granger", "09/19/1979")
        .address("Platform 9 and 3/4").email("ms.smarties@hogwarts.uk")
        .build();
    System.out.println(Hermione);


    Person newPerson = new Person.Builder("New", "Person", "59/33/1922")
        .address("123 Main St.").email("new@person.ca")
        .phoneNumber("647-111-2932").build();
    System.out.println(newPerson);
  }
}
