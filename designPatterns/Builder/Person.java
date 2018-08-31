public class Person {

  //there should be 6 fields
  private final String firstName;
  private final String lastName;
  private final String dateOfBirth;

  private String email;
  private String phoneNumber;
  private String address;


  public static class Builder {

    // required parameters (3)
    private final String firstName;
    private final String lastName;
    private final String birthday;

    //TODO

    // optional parameters (3)-initialized to default values
    // (of course these should be more reasonable default values)
    // why are these not final? (bc these can change if you want to log them)
    private String phoneNumber = "123-DEF-AULT";
    private String address;
    private String email;
    //TODO

    // Builder constructor with required fields (3)
    public Builder(String fname, String lname, String bday) {
      // just inject the first name, last name, and the birthday
      firstName = fname;
      lastName = lname;
      birthday = bday;
    }

    //methods below are to change the default values of the optional parameters
    public Builder address(String add) {
      address = add;
      return this;
    }

    public Builder phoneNumber(String pNumber) {
      phoneNumber = pNumber;
      return this;
    }

    public Builder email(String em) {
      email = em;
      return this;
    }

    public Person build() {
      //TODO
      // the inner Builder class can call the
      // private constructor of the outer
      // Person class
      return new Person(this);
    }
  }

  Person(Builder b) {
    this.firstName = b.firstName;
    this.lastName = b.lastName;
    this.address = b.address;
    this.dateOfBirth = b.birthday;
    this.phoneNumber = b.phoneNumber;
    this.email = b.email;
  }

  public String toString() {
    String fname = "First name: " + this.firstName;
    String lname = "Last name: " + this.lastName;
    String address = "Address: " + this.address;
    String dob = "Date of birth: " + this.dateOfBirth;
    String number = "Number: " + this.phoneNumber;
    String email = "Email: " + this.email;
    return fname + "\n" + lname + "\n" + dob + "\n" + address + "\n" + number
        + "\n" + email + "\n";
  }

}
