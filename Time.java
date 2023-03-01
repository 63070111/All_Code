
import java.util.Scanner;

public class Time {
    public static void main(String[] args) {
    int Hour, Mins, Secs;
    Scanner hour = new Scanner(System.in);
    Scanner mins = new Scanner(System.in);
    System.out.println("Enter hour and mins");
    Hour = hour.nextInt();
    Mins = mins.nextInt();
    Hour = Hour*3600;
    Mins = Mins * 60;
    Secs = Hour+Mins;
        System.out.println("Second is "+Secs);
}
    
}
