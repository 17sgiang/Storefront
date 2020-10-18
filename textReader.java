import javax.swing.*;
import java.io.*;
import java.util.Vector;
class textReader extends JFrame
{
  public textReader() throws IOException
  {
	  File storeList = new File("A.txt");
	    FileReader fr = new FileReader(storeList);
	    BufferedReader br = new BufferedReader(fr);

	    Vector<String> row = new Vector<String>();

	    String line;
	    while ((line = br.readLine()) != null) {
	      row.add(line);
	    }
	    JOptionPane.showMessageDialog(null, new JScrollPane(new JList(row)));
	    fr.close();
 
}
}