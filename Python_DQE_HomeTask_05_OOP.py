# Home task 05: Python OOP  Julia Mendoza Verduzco
"""Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format
You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.
Each new record should be added to the end of file"""

from datetime import datetime #import datetime module to get the current date

FILE_NAME = 'news_feed.txt' #file to write the news feed

def add_news(): #function to add news
    text = input('Enter the news text: ') #get the text for the news
    city = input('Enter the city: ') #get the city for the
    publish_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #get the current date
    record =f'News--------------------------------------\n {text}\n in {city}\nPublish date:  {publish_date}\n\n' #record with a city news
    save_record(record) #save the record into the file

def add_private_ad(): #function to add private ad
    text = input('Enter the private ad text: ') #get the text for the private ad
    expiration_date = input('Enter the expiration date (yyyy-mm-dd): ') #get the expiration date
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d') #convert the expiration date to datetime
    days_left = (expiration_date - datetime.now()).days #calculate the days left for the expiration date
    record = f'Private Ad--------------------------------\n {text}\nExpiration date: {expiration_date.strftime("%Y-%m-%d")}\nDays left: {days_left}\n\n' #record with a private ad
    save_record(record) #save the record into the file

def add_book_recommendation(): #function to add book recommendation
    title = input('Enter the book title: ') #get the title of the book
    author = input('Enter the author: ') #get the author of the book
    genre = input('Enter the genre: ') #get the genre of the book
    reason = input('What do you love about this book?: ') #Why is so amazing this book?
    record = f'Book Recommendation------------------------\n {title}\n by {author}\nGenre: {genre}\nReason: {reason}\n\n' #record with a book recommendation
    save_record(record) #save the record into the file

def save_record(record): #function to save the record into the file
    with open(FILE_NAME, 'a') as file: #open the file in append mode
        file.write(record) #write the record into the file
    print("Record saved successfully\n") #print message that the record was saved

def main(): #main function
    while True: #infinite loop to keep adding records
        print("Select the type of record to add:")
        print("1. News")
        print("2. Private Ad")
        print("3. Book Recommendation")
        print("4. Exit")
        option = input("Enter your choice: ") #get the option from the user
        if option == '1': #if the option is 1 add news
            add_news()
        elif option == '2': #if the option is 2 add private ad
            add_private_ad()
        elif option == '3': #if the option is 3 add book recommendation
            add_book_recommendation()
        elif option == '4': #if the option is 4 exit the program
            break
        else:
            print("Invalid choice. Please, try again\n") #if the option is invalid print a message

if __name__ == '__main__': #if the script is executed directly
    main() #call the main function