import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class myFrame2 implements MouseListener{
        private JFrame fr;
        private clock2 clock;
        private Thread t;
        private boolean  o=true;
        public myFrame2(){
          fr = new JFrame();
          clock = new clock2();
          t = new Thread(clock);
          fr.add(clock);
          fr.addMouseListener(this);
          fr.setSize(270, 200);
          fr.setVisible(true);
          fr.setResizable(false);
          fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
          t.start();
        }
        public static void main(String[] args) {
         new myFrame2();
    }
    

    @Override
    public void mouseClicked(MouseEvent me) {
        if(o){
           clock.pauseThread();
           o=false;
        }
        else{
           clock.resumeThread();
           o=true;
        }
        
    }

    @Override
    public void mousePressed(MouseEvent me) {}

    @Override
    public void mouseReleased(MouseEvent me) {}

    @Override
    public void mouseEntered(MouseEvent me) {}

    @Override
    public void mouseExited(MouseEvent me) {}
}

