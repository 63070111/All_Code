import java.util.*;
public class Vat {
    public static void main(String[] args) {
        Scanner price = new Scanner(System.in);
        double fullprice, vat, total;
        System.out.println("Enter price ");
        fullprice = price.nextDouble();
        vat = fullprice*0.07;
        total = fullprice+vat;
        System.out.println("Vat is "+total);
        
    }
    
    
}
