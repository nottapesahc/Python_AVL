
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

/**
 * Used to generate dummy data in the format "ABC 123456 123456"
 *
 * @author stevenpatton
 */
public class DataGenerator {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("SuperImportantData.txt");
        Random rand = new Random();

        //number of lines in the file
        int NumberOfEntries = rand.nextInt(100) + 10;

        //the false means it can be overwrote
        PrintWriter pw = new PrintWriter(new FileWriter(file, false));

        //loops for each line
        while (NumberOfEntries > 0) {
            int dataEntryLength = rand.nextInt(5) + 3;
            char[] letArr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
            
            String line = "";
            String line2 = "";
            //loops for each data entry name
            while (dataEntryLength > 0) {
                int randLetter = rand.nextInt(25);
                line += letArr[randLetter];

                int anotherRandLetter = rand.nextInt(25);
                line2 += letArr[anotherRandLetter];

                dataEntryLength--;
            }

            int id = rand.nextInt(900000);
            pw.println(id + " " + line + " " + line2);
            NumberOfEntries--;
        }
        pw.close();
    }
}
