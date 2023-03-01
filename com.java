import java.util.*;
public class com {
    public static void main(String[] args) {
        Double monitor, dvd, printer, price = 375.99,full;
        Double DVD = 65.99, Printer = 125.00;
        Scanner value = new Scanner(System.in);
        
        System.out.println("please insert your monitor size 38 or 43 only");
        monitor = value.nextDouble();
        System.out.println("Do you want DVD-ROM? 1 is Yes/ 0 is No");
        dvd = value.nextDouble();
        System.out.println("Do you want printer? 1 is Yes / 0 is No");
        printer = value.nextDouble();
        
        if(monitor == 38)
        {
            if(dvd == 1)
            {
                if(printer == 1)
                {
                    full = price+Printer+DVD+75.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("38'Monitor >>> 75.99$");
                    System.out.println("DVD-Rom >>> "+DVD+" $");
                    System.out.println("Printer >>> "+Printer+"$");
                    System.out.println("Total price >>> "+full);
                }
                else
                {
                    full = price+DVD+75.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("38'Monitor >>> 75.99$");
                    System.out.println("DVD-Rom >>> "+DVD+"$");
                    System.out.println("Total price >>> "+full);
                }
            }
            else
            {
                if(printer == 1)
                {
                    full = price+Printer+75.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("38'Monitor >>> 75.99$");
                    System.out.println("Printer >>> "+Printer+"$");
                    System.out.println("Total price >>> "+full);
                }
                else
                {
                    full = price+75.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("38'Monitor >>> 75.99$");
                    System.out.println("Total price >>> "+full);
                }
            }
        }
        else
        {
            if(dvd == 1)
            {
                if(printer == 1)
                {
                    full = price+Printer+DVD+99.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("43'Monitor >>> 99.99$");
                    System.out.println("DVD-Rom >>> "+DVD+"$");
                    System.out.println("Printer >>> "+Printer+"$");
                    System.out.println("Total price >>> "+full);
                }
                else
                {
                    full = price+DVD+99.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("43'Monitor >>> 99.99$");
                    System.out.println("DVD-Rom >>> "+DVD+"$");
                    System.out.println("Total price >>> "+full);
                }
            }
            else
            {
                if(printer == 1)
                {
                    full = price+Printer+99.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("43'Monitor >>> 99.99$");
                    System.out.println("Printer >>> "+Printer+"$");
                    System.out.println("Total price >>> "+full);
                }
                else
                {
                    full = price+99.99;
                    System.out.println("computer >>> "+price+"$");
                    System.out.println("43'Monitor >>> 99.99$");
                    System.out.println("Total price >>> "+full);
                }
            }
        }
       
       
        
    }
    
}
