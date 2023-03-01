import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class PoringConstructor extends Thread implements Runnable, ActionListener{
    private JFrame fr;
    private JButton b1;
    private JPanel p1;
    private Poring po;
    private int count=1;
    public PoringConstructor(){
    fr = new JFrame("PoringConstructor");
    b1 = new JButton("Add");
    p1 = new JPanel();
    fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    b1.addActionListener(this);
    
    p1.setLayout(new FlowLayout());
    p1.add(b1);
    p1.setSize(10, 10);
    fr.add(p1);
    fr.pack();
    fr.setVisible(true);
    Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
    int x = (int) ((dimension.getWidth() - fr.getWidth()) / 2);
    int y = (int) ((dimension.getHeight() - fr.getHeight()) / 2);
    fr.setLocation(x, y);
    
}
    public static void main(String[] args) {
        new PoringConstructor(); 
            
    }
 

    @Override
    public void actionPerformed(ActionEvent ae) { 
        if(ae.getSource().equals(b1)){
            po = new Poring(count++);
            Thread t = new Thread(po);
            t.start();
          
        }
        
    }
}