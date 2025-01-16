import java.util.Scanner;
class Account {
    int bal;
    public Account(int amt) {
        this.bal = amt;
    }
    public boolean isSuff(int wAmt) {
        if(bal < wAmt) {
            return false;
        } else {
            return true;
        }
    }
    public void withDraw(int wAmt, String s1) {
        bal = bal - wAmt;
        System.out.println(wAmt + " Successfully Withdraw.." + s1);
        System.out.println("Current balance is: " + bal);
    }
}
class Customer implements Runnable{
    Account a1;
    String s1;
    Customer(Account a1, String s1, Scanner sc) {
        this.a1 = a1;
        this.s1 = s1;
        this.sc = sc;
    }
    public void run() {  
        synchronized(a1) {
            System.out.println("Enter withdraw amount: " + s1);
            int amt = sc.nextInt();
            if(a1.isSuff(amt)) {
                a1.withDraw(amt, s1);
            } else {
                System.out.println("Insufficient Balance.");
            }
        }
        
    }
}
class Multithreading_in_java {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Account a1 = new Account(5000);
        Customer c1 = new Customer(a1, "Surya", sc);
        Customer c2 = new Customer(a1, "Rohit", sc);
        Thread t1 = new Thread(c1);
        Thread t2 = new Thread(c2);
        t1.run();
        t2.run();
        // sc.close();
    }
}