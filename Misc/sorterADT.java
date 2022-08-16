package librarySorter;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.sql.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class sorterADT
   {

      @SuppressWarnings("unchecked")
      public static void main(String[] args) throws FileNotFoundException, IOException{
         int numBooks = 0;
         
         
         // TODO Auto-generated method stub
         File myFile = new File("C:\\Working_ Academic Search Complete.xlsx");
         FileInputStream fis = new FileInputStream(myFile);

         // Finds the workbook instance for XLSX file
         XSSFWorkbook myWorkBook = new XSSFWorkbook (fis);
        
         // Return first sheet from the XLSX workbook
         XSSFSheet mySheet = myWorkBook.getSheetAt(0);
        
         // Get iterator to all the rows in current sheet
         Iterator<Row> rowIterator = mySheet.iterator();
         
         Iterator<Row> dankiterator = mySheet.iterator();
         
         while (dankiterator.hasNext())
            {
               numBooks += 1;
               Row row = dankiterator.next();
            }
        
         Book[] libraryBooks = new Book[numBooks];

         int diabetus = 0;
         // Traversing over each row of XLSX file
         while (rowIterator.hasNext()) {
             Row row = rowIterator.next();
             Book newBook = new Book();

             // For each row, iterate through each columns
             int colCounter = 0;
             Iterator<Cell> cellIterator = row.cellIterator();
             while (cellIterator.hasNext()) {
                Cell cell = cellIterator.next();
                
                //If on first col, get name
                if (colCounter == 0)
                   {
                      newBook.setName(cell.getStringCellValue() + "\t");
                      colCounter += 1;
                      cellIterator.next();
                   }
                
                if (colCounter == 1)
                   {
                      switch(cell.getCellType())
                      {
                         case STRING:
                            String newName = cell.getStringCellValue();
                            System.out.println(newName);
                            newBook.setPublisher(newName);
                            break;
                            
                         case NUMERIC:
                            int newID = (int)cell.getNumericCellValue();
                            newBook.setID(newID);
                            break;                            
                            
                         default:
                            newBook.setID((int)666);
                            
                      }
                      
                      colCounter += 1;
                   }
                

         }
             libraryBooks[diabetus] = newBook;
             diabetus++;
      }
         Book testBook = new Book();
         for (int counter = 0; counter < numBooks; counter++)
            {
               testBook = libraryBooks[counter];
               System.out.println(testBook.toString());
            }

   }
   }
