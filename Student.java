import java.util.*;
public class Student {
    public String name;
    public double mScore;
    public double fScore;
    public void showGrade() 
    {
        double score = (mScore*0.4)+(fScore*0.4)+20;
        if((100>=score)&&(score>=80)){System.out.println("Your grade is A");}
        else if((80>score)&&(score>=70)){System.out.println("Your grade is B");}
        else if((70>score)&&(score>=60)){System.out.println("Your grade is C");}
        else if((60>score)&&(score>=50)){System.out.println("Your grade is D");}
        else if(50>score){System.out.println("Your grade is F");}
        
    }
    public static void main(String[] args) {
        Student s = new Student();
        s.mScore = 80;
        s.fScore = 80;
        s.showGrade();
    }

    
}
