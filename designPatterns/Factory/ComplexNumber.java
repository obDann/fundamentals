import java.lang.Math;

public class ComplexNumber {

  // create a real part and an imaginary part
  private float realPart;
  private float imgPart;

  // for the factory design pattern, the constructor is private

  /**
   * Initializes a complex number, provided a real number and an imaginary
   * number
   *
   * @param real the real part in a complex number
   * @param img  the imaginary part in a complex number
   */
  private ComplexNumber(float real, float img) {
    // assign the real part
    realPart = real;
    // and then assign the imaginary part
    imgPart = img;
  }

  /**
   * Creates a complex number through cartesian coordinates
   *
   * @param real the real number in a complex number
   * @param img  the imaginary number in a complex number
   * @return
   */
  public static ComplexNumber createByCartesian(float real, float img) {
    // just return an instantiation of a complex number
    return new ComplexNumber(real, img);
  }

  /**
   * Creates a complex number through polar coordinates
   *
   * @param mod   the modulus in the complex number
   * @param angle the angle measured in radians
   * @return
   */
  public static ComplexNumber createByPolar(float mod, float angle) {
    // create the real part
    float r = (float) (mod * Math.cos(angle));
    // and the imaginary part
    float i = (float) (mod * Math.sin(angle));
    // then return a new instantiation of a complex number
    return new ComplexNumber(r, i);
  }
}
