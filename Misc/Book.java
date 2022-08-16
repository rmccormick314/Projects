package librarySorter;

import java.util.Date;

/**Book class for spreadsheet sorter
 * @author richard_mccormick
 *
 */
public class Book extends Exception
{
   //Constant for failed field access
   int FAILED_ACCESS = -999999;
   String NO_NAME = "FFFFF";
   Date NO_DATE = new Date(1);
   
   
   //Variables for book info
   String name = "";
   String publisher = "";
   int ID;
   Date dateOne;
   Date dateTwo;
   
   
   /**Default constructor class
    * 
    */
   Book()
   {
      name = NO_NAME;
      publisher = NO_NAME;
      ID = FAILED_ACCESS;
      dateOne = NO_DATE;
      dateTwo = NO_DATE;
   }
   
   /**Param constructor for easier testing
    * 
    * @param name       - String val
    * @param publisher  - String val
    * @param ID         - int val
    */
   Book(String name, String publisher, int ID)
   {
      this.name = name;
      this.publisher = publisher;
      this.ID = ID;
      dateOne = NO_DATE;
      dateTwo = NO_DATE;
   }
   
   
   /**Checks to see if a book is EBSCO property
    * @return check  - Boolean value indicator
    */
   public boolean isEBSCO()
   {
      boolean check = false;
      
      if (getID() != FAILED_ACCESS)
         {
            check = true;
         }
      
      return check;
   }
   
   /**Sets the publisher of a book
    * @param newPublisher  - String value of publisher name (if exists)
    */
   public void setPublisher(String newPublisher)
   {
      this.publisher = newPublisher;
   }
   
   /**Gets the name of publisher
    * @return publisherName   - String value
    */
   public String getPublisher()
   {
      String pub = this.publisher;
      
      return pub;
   }
   
   /**Sets a book ID as numeric value
    * @param newID   - ID to be set
    */
   public void setID(int newID)
   {
      this.ID = newID;
   }
   
   /**Gets a given books ID
    * @return bookID - Integer value
    */
   public int getID()
   {
      return ID;
   }
   
   /**Gets the name of book
    * @return bookName  - String value
    */
   public String getName()
   {
      return this.name;
   }
   
   /**Sets the name of book
    * @param newName - Sets new name of book
    */
   public void setName(String newName)
   {
      this.name = newName;
   }
   
   /**Prints string value of book to screen
    * (name, publisher, id, etc)
    */
   public String toString()
   {
      String itemThing = "";
      
      itemThing += "Name: " + this.name + " | ";
      itemThing += "ID: " + this.ID + " | ";
      itemThing += "Publisher: " + this.publisher + " | ";
      
      return itemThing;
   }
   
   public void setDate(Date newDate, int num)
   {
      if (num == 1)
         {
            dateOne = newDate;
         }
      
      if (num == 2)
         {
            dateTwo = newDate;
         }
   }
   
   /**Gets the date values of book
    * @param num     - indicates if date one or two should be used
    * @return date   - Date value at given index
    */
   public Date getDate(int num)
   {
      Date returnDate = null;
      
      if (num == 1)
         {
            returnDate = this.dateOne;
         }
      
      if (num == 2)
         {
            returnDate = this.dateTwo;
         }
      
      return returnDate;
   }
   
   
   
}
