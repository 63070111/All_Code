 import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
public class Text_Editor implements ActionListener{
    private JFrame fr;
    private JTextArea tx;
    private JMenuBar mb;
    private JMenu b1;
    private JMenuItem m1, m2, m3, m4;
    private JDesktopPane desktopPane;
    private JPanel panel;
    
    
    public Text_Editor(){
        fr = new JFrame("My Text Editor");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new JPanel();
        tx = new JTextArea();
        mb = new JMenuBar();
        b1 = new JMenu("File");
        m1 = new JMenuItem("New");       
        m2 = new JMenuItem("Open");
        m3 = new JMenuItem("Save");
        m4 = new JMenuItem("Close");
        Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
        int x = (int) ((dimension.getWidth() - fr.getWidth()) / 2);
        int y = (int) ((dimension.getHeight() - fr.getHeight()) / 2);
        fr.setLocation(x, y);
        
  
        fr.setJMenuBar(mb);
        mb.add(b1);    
        b1.add(m1);
        b1.add(m2);
        b1.add(m3);
        b1.add(m4);

        m1.addActionListener(this);
        m2.addActionListener(this);
        m3.addActionListener(this);
        m4.addActionListener(this);
        
                
        panel.setLayout(new FlowLayout());
        panel.add(tx, BorderLayout.CENTER);
        fr.add(tx);
        fr.setSize(450,350);              
        fr.setVisible(true);
    }
    public static void main(String[] args) {
        new Text_Editor();
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        if(ae.getSource().equals(m1)){
            tx.setText("");
        }
        else if(ae.getSource().equals(m2)){
            JFileChooser fc = new JFileChooser();
            fc.showOpenDialog(fr);
            File fo = fc.getSelectedFile();
            try(FileInputStream fin = new FileInputStream(fo);
                ObjectInputStream in = new ObjectInputStream(fin);){
                   in.read();
                   tx.setText(""+(String) in.readObject());
           }catch(IOException i){
                i.printStackTrace();
           }catch(ClassNotFoundException c){
                c.printStackTrace();
            }
        
        }
        else if(ae.getSource().equals(m3)){
            JFileChooser fc = new JFileChooser();
            fc.showSaveDialog(fr);
            File fo = fc.getSelectedFile();
             try(FileOutputStream fOut = new FileOutputStream(fo);
            ObjectOutputStream oout = new ObjectOutputStream(fOut);){
                oout.writeObject(tx.getText());
                System.out.print("Serialized data is saved");
        }catch(IOException i){
                i.printStackTrace();
        }
            
        }
         else if(ae.getSource().equals(m4)){
             fr.setVisible(false);
             fr.dispose();
         }
            
        }  
}
