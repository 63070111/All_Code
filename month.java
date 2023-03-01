import java.util.*;
public class month {
    public static void main(String[] args) {
        int month;
        Scanner day = new Scanner(System.in);
        System.out.println("Enter a Month ID: ");
        month = day.nextInt();
        switch(month)
        {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12: 
                System.out.println("31 Days");
                break;
            case 4: case 6:case 9: case 11:
                System.out.println("30 Days");
                break;
            case 2:
                System.out.println("28 Days");
                break;
            default:
                System.out.println("Please enter 1-12 only");
        }
    }
    
}
