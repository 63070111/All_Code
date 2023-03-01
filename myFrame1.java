import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class myFrame1 {
     public static void main(String[] args) {
        JFrame fr = new JFrame();
        clock1 clock = new clock1();
        Thread t = new Thread(clock);
        t.start();
        fr.add(clock);
        fr.setSize(270, 200);
        fr.setVisible(true);
    }
}
