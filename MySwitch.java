import java.util.*;
public class MySwitch {
    public static void main(String[] args) {
        int x;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        x = sc.nextInt();
        
        switch(x)
        {
            case 1: case 2:
                System.out.println("Green");
                break;
            case 3: case 4: case 5:
                System.out.println("Blue");
                break;
            default:
                System.out.println("numbers 1-5 only");
                
        }
        System.out.println("Red");
    }
    
}
