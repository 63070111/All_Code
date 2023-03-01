import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class MyFrame {
    public static void main(String[] args) {
        JFrame fr = new JFrame();
        MyClock clock = new MyClock();
        Thread t = new Thread(clock);
        t.start();
        fr.add(clock);
        fr.setSize(270, 200);
        fr.setVisible(true);
    }
}
