import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

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
	public userGui()
    {
	  
      }
    
	
    public static void main(String args[]) throws IOException{
     
    	JPanel panel = new JPanel();
        JFrame frame = new JFrame();
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.add(panel);
        
        panel.setLayout(null);
        
        label = new JLabel("Radius");
        label.setBounds(10, 20, 40, 25);
        panel.add(label);
        
        radius = new JTextField(20);
        radius.setBounds(100, 20, 75, 25);
        panel.add(radius);
        
        label2 = new JLabel("Lat");
        label2.setBounds(10, 50, 80, 25);
        panel.add(label2);
        
        lat = new JTextField(20);
        lat.setBounds(100, 50, 75, 25);
        panel.add(lat);
        
        label3 = new JLabel("Long");
        label3.setBounds(10, 80, 80, 25);
        panel.add(label3);
        
        notLat = new JTextField(20);
        notLat.setBounds(100, 80, 75, 25);
        panel.add(notLat);
        
        button = new JButton("Search!");
        button.setBounds(10, 120, 150, 25);
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
			PrintStream console = System.out;
			
			System.setOut(o);
			System.out.println(radi); 
			System.out.println(latt);  
			System.out.println( notLatt);
		        
		    new textReader().setVisible(true);
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
			
			TimerTask task = new fileWatcher( new File("A.txt") ) {
			      protected void onChange( File file ) {
			        // here we code the action on a change
			        System.out.println( "File "+ file.getName() +" have change !" );
			      }
			    };

			    Timer timer = new Timer();
			    // repeat the check every second
			    timer.schedule( task , new Date(), 1000 );
		}
    
    	
	}
}