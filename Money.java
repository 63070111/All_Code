import java.util.*;
public class Money {
    public static void main(String[] args) {
        double moneys,full;
        char word;
        Scanner value = new Scanner(System.in);
        System.out.println("Input your money: ");
        System.out.println("Input your account type(please type A B C or X in uppercase) : ");
        moneys = value.nextDouble();
        word = value.next().charAt(0);
        if((word=='A') ||(word =='C')){
            full = moneys+(moneys*0.015);
            System.out.println("Your total money in one year = "+full);
        }else if(word == 'B'){
            full = moneys+(moneys*0.02);
            System.out.println("Your total money in one year = "+full);
        }else{
            full = moneys+(moneys*0.05);
            System.out.println("Your total money in one year = "+full);
        }
    }
}
