import java.awt.Dimension;
import java.awt.TextArea;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.nio.file.WatchKey;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.TimeUnit;

// Using Frame class in package java.awt
import javax.swing.*;
public class userGui implements ActionListener {
	
	private static JLabel label;
	private static JLabel label2;
	private static JLabel label3;
	private static JTextField radius;
	private static JTextField lat;
	private static JTextField notLat;
	private static JButton button;

    
	
    public static void main(String args[]) throws IOException{
    	
    	//new textAreaExample();
     
    	JPanel panel = new JPanel();
        JFrame frame = new JFrame();
        frame.setSize(210, 200);
        Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
        int x = (int) ((dimension.getWidth() - frame.getWidth()) / 2);
        int y = (int) ((dimension.getHeight() - frame.getHeight()) / 2);
        frame.setLocation(x, y);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(panel);
     
        
        panel.setLayout(null);
        
        label = new JLabel("Radius (miles)");
        label.setBounds(10, 20, 100, 25);
        panel.add(label);
        
        radius = new JTextField(20);
        radius.setBounds(100, 20, 75, 25);
        panel.add(radius);
        
        label2 = new JLabel(" Latitude  ");
        label2.setBounds(25, 50, 80, 25);
        panel.add(label2);
        
        lat = new JTextField(20);
        lat.setBounds(100, 50, 75, 25);
        panel.add(lat);
        
        label3 = new JLabel("Longitude");
        label3.setBounds(25, 80, 80, 25);
        panel.add(label3);
        
        notLat = new JTextField(20);
        notLat.setBounds(100, 80, 75, 25);
        panel.add(notLat);
        
        button = new JButton("Search");
        button.setBounds(25, 125, 150, 20);
        button.addActionListener(new userGui());
        panel.add(button);
        
        frame.setVisible(true);
        
        
     
    }
   
    
	@Override
	public void actionPerformed(ActionEvent e){
		
		
		String radi = radius.getText();
    	String latt = lat.getText();
    	String notLatt = notLat.getText();
    	
    	try {
			PrintStream o = new PrintStream(new File("A.txt"));
			
			System.setOut(o);
			System.out.println(radi); 
			System.out.println(latt);  
			System.out.println(notLatt);
			
			
			Thread.sleep(1000);
			webListing wind= new webListing();
		    wind.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		    wind.setSize(800,300);
		    Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
	        int x = (int) ((dimension.getWidth() - wind.getWidth()) / 2);
	        int y = (int) ((dimension.getHeight() - wind.getHeight()) / 2);
	        wind.setLocation(x, y);
		    wind.setVisible(true);
			//new textAreaExample();
			//new textReader().setVisible(true);  
			
		} catch (IOException e1) {
		
			e1.printStackTrace();
			
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
    	
    	
	}
}