import java.awt.*;
import java.awt.event.*;
import static java.lang.Double.min;
import java.util.Calendar;
import java.util.Locale;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.*;
public class clock1 extends JLabel implements Runnable{

    private Object hour;
   
    public void run() {
        try{
             while(true){
            int sec = 0;
            int min = 0;
            int hour = 0;
            setFont(new Font("TimesRoman", Font.BOLD,60));     
            for(int p=0;p<24;p++){
                for(int i=0;i<60;i++){
                    for(int j=0;j<60;j++){
                        Thread.sleep(1000);
                        sec++;
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
                    sec=0;
                    min++;
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
                min=0;
                hour++;
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
            hour=0;
            min=0;
            sec=0;
        } 
            
        }
       
        catch(InterruptedException e){
            Thread.currentThread().interrupt();
        }
        }     

  
}


