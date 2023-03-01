import java.awt.*;
import javax.swing.*;
public class MmGUI {
    private JFrame fr;
    private JMenuBar mb;
    private JMenu b1, b2, b3, b4;
    private JMenuItem m1, m2, m3, m4, m5, m6;
    private JDesktopPane desktopPane;
    private JInternalFrame frame1, frame2, frame3;
    private JPanel panel;
    
    public MmGUI(){
        fr = new JFrame("SubMenuItem Demo");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new JPanel();
        mb = new JMenuBar();
        b1 = new JMenu("File");
        b2 = new JMenu("Edit");
        b3 = new JMenu("View");
        m1 = new JMenu("New");       
        m2 = new JMenuItem("Open");
        m3 = new JMenuItem("Save");
        m4 = new JMenuItem("Exit");
        m5 = new JMenuItem("Window");
        m6 = new JMenuItem("Message");
        
  
        fr.setJMenuBar(mb);
        mb.add(b1); 
        mb.add(b2);
        mb.add(b3);   
        b1.add(m1);
        b1.add(m2);
        b1.add(m3);
        b1.add(m4);        
        m1.add(m5);    
        m1.add(m6);
        
        desktopPane = new JDesktopPane();
        frame1 = new JInternalFrame ("Application 01", true, true , true, true);
        frame2 = new JInternalFrame ("Application 02", true, true , true, true);
        frame3 = new JInternalFrame ("Application 03", true, true , true, true);
       
        frame1.getContentPane().add(new JLabel("Frame1"));
        frame1.pack();
        frame1.setVisible(true);
        
        frame2.getContentPane().add(new JLabel("Frame2"));
        frame2.pack();
        frame2.setVisible(true);
        
        frame3.getContentPane().add(new JLabel("Frame3"));
        frame3.pack();
        frame3.setVisible(true);
        
        int x2 = frame1.getX()+frame1.getWidth()+10;
        int y2 = frame1.getY();
        int x3 = frame2.getX()+frame2.getWidth()+150;
        int y3 = frame2.getY();
        frame2.setLocation(x2, y2);
        frame3.setLocation(x3, y3);
        
        desktopPane.add(frame1);
        desktopPane.add(frame2);
        desktopPane.add(frame3);
        panel.setLayout(new FlowLayout());
        panel.add(desktopPane, BorderLayout.CENTER);
        panel.setMinimumSize(new Dimension(300,300));
        
        fr.pack();              
        fr.setExtendedState(fr.MAXIMIZED_BOTH);
        fr.setVisible(true);
    }
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e){
            e.printStackTrace();
        }
        new MmGUI();
    }

    
}
