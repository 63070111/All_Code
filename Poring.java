import java.awt.*;
import java.awt.event.*;
import static java.lang.Math.random;
import javax.swing.*;
import java.util.*;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Poring implements Runnable,MouseListener{
    private JFrame fr;
    private ImageIcon icon;
    private JPanel p1;
    private JLabel l1;
    private JLabel l2;
    private int num;
    public Poring(int num){
        this.num = num;
        fr = new JFrame("Poring");
        icon = new ImageIcon(getClass().getResource("1.jpg"));
        l1 = new JLabel(icon);
        l2 = new JLabel(this.num+"");
        p1 = new JPanel();
        p1.add(l1);
        p1.add(l2);
        fr.getContentPane().add(p1);
        l1.addMouseListener(this);
        //แสดง
        fr.setFont(new Font("TimesRoman", Font.BOLD,60));
        fr.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        fr.pack();
        fr.setVisible(true);
        Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
        int x = (int)(((dimension.getWidth()-100)*Math.random()));
        int y = (int)(((dimension.getHeight()-100)*Math.random()));
        fr.setLocation(x, y);
        fr.setResizable(false);
        
        
        
    }
   
    public void run(){
        try {
        while(true){
            fr.setLocation((int)((fr.getLocationOnScreen().x)+((Math.random()*10))),(int)((fr.getLocationOnScreen().y)+((Math.random()*10))));
            fr.setLocation((int)((fr.getLocationOnScreen().x)-((Math.random()*10))),(int)((fr.getLocationOnScreen().y)-((Math.random()*10))));
       
            Thread.sleep(500);
        }
        
        } catch (InterruptedException ex) {
            Logger.getLogger(Poring.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
    }

    @Override
    public void mouseClicked(MouseEvent me) {
        this.fr.dispose();
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
