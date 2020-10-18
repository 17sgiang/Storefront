import java.io.*;


import javax.swing.*;


import java.awt.*;



public class webListing extends JFrame{

private JEditorPane editorpane;
JScrollPane editorScrollPane;
String files = "A.txt";;
Reader filereader;

public webListing() throws IOException
{       
        editorpane= new JEditorPane();
        editorpane.setEditable(true);

      
        filereader=new FileReader(files);
        File file = new File(files);
        editorpane.setPage(file.toURI().toURL());
          
        editorScrollPane = new JScrollPane(editorpane);
        editorScrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        editorScrollPane.setPreferredSize(new Dimension(250, 145));
        editorScrollPane.setMinimumSize(new Dimension(10, 10)); 
        getContentPane().add(editorScrollPane);


}
}