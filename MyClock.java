import java.awt.*;
import java.awt.event.*;
import static java.lang.Double.min;
import java.util.Calendar;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.*;
public class MyClock extends JLabel implements Runnable{

    private Object hour;
   
    public void run() {
        try{
             while(true){
            Calendar d = Calendar.getInstance();
            int sec = d.get(Calendar.SECOND);
            int min = d.get(Calendar.MINUTE);
            int hour = d.get(Calendar.HOUR_OF_DAY);
            Thread.sleep(1000);
            setFont(new Font("TimesRoman", Font.BOLD,60));
            if(hour<10){
                if(min<10){
                    if(sec<10){
                        setText("0"+hour+":0"+min+":0"+sec);
                    }
                    else{
                        setText("0"+hour+":0"+min+":"+sec);
                    }
                }
                else{
                    if(sec<10){
                        setText("0"+hour+":"+min+":0"+sec);
                    }
                    else{
                        setText("0"+hour+":"+min+":"+sec);
                    }
                }
                
            }else{
                 if(min<10){
                    if(sec<10){
                        setText(hour+":0"+min+":0"+sec);
                    }
                    else{
                        setText(hour+":0"+min+":"+sec);
                    }
                }
                else{
                     if(sec<10){
                        setText(hour+":"+min+":0"+sec);
                    }
                    else{
                        setText(hour+":"+min+":"+sec);
                    }
                    
                }
            }
           
}
        }
        catch(InterruptedException e){
            Thread.currentThread().interrupt();
        }
       
}
}

