class ExceptionHandling {
  public static void main(String[] args) {
    String s1;
    s1 = null;
    try {
      System.out.println(s1.length());
    } catch(NullPointerException e1) {
      System.out.println(e1.getMessage());
    }
    try {
      System.out.println(5/0);
    }
    catch(ArithmeticException a1) {
      System.out.println(a1.getMessage());
    } finally {
      System.out.println('A');
      System.out.println("End");
    }
    /*
    try {
      System.out.println(s1.length());
      System.out.println(5/0);   // This will be skipped
    } catch(NullPointerException e1) {
      System.out.println(e1.getMessage());
    } catch(ArithmeticException a1) {
      System.out.println(a1.getMessage());
      // The first exception that occurs in the try block determines which catch block gets executed.
      // Once an exception is caught, the rest of the try block is skipped, and control moves to the corresponding catch block or finally block.
    } finally {
      System.out.println('A');
      System.out.println("End");
    }
    */
  }
}