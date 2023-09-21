import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class MapReduce {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new File("myfile.txt"));
            while (in.hasNext()) {
                process(in.next());
            }
            in.close(); // Close the scanner to release resources.
        } catch (FileNotFoundException e) {
            e.printStackTrace(); // Handle the case where the file is not found.
        }
    }

    // Define the process method to handle each word.
    public static void process(String word) {
        // Your processing logic here...
        System.out.println("Processing word: " + word);

        // counter for each unique word
        int uniquecounter = 0;

        // counter for each word
        int wordcounter = 0;

    }
}
