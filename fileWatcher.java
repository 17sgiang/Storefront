import java.util.*;
import java.io.*;

public abstract class fileWatcher extends TimerTask {
  private long timeStamp;
  private File file;

  public fileWatcher( File file ) {
    this.file = file;
    this.timeStamp = file.lastModified();
  }

  public final void run() {
    long timeStamp = file.lastModified();

    if( this.timeStamp != timeStamp ) {
      this.timeStamp = timeStamp;
      onChange(file);
    }
  }

  protected abstract void onChange( File file );
}
