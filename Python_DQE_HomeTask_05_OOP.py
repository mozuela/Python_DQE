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
import csv
from collections import Counter

FILE_NAME = 'news_feed.txt' #file to write the news feed
WORDS_FILE_NAME = 'words_statistics.txt' #file to write the news feed
LETTER_FILE_NAME = 'letters_statistics.txt' #file to write the news feed

from datetime import datetime #import datetime module to get the current date
from Python_DQE_HomeTask_03_String_functions import preprocess_text as cleanText #import the preprocess_text function from the previous homework

def add_news(text, city): #function to add news
    publish_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #get the current date
    record =f'News--------------------------------------\n {text}\n in {city}\nPublish date:  {publish_date}\n\n' #record with a city news
    save_record(record) #save the record into the file

def add_private_ad(text, expiration_date ): #function to add private ad
    days_left = (expiration_date - datetime.now()).days #calculate the days left for the expiration date
    record = f'Private Ad--------------------------------\n {text}\nExpiration date: {expiration_date.strftime("%Y-%m-%d")}\nDays left: {days_left}\n\n' #record with a private ad
    save_record(record) #save the record into the file

def add_book_recommendation(title, author, genre, reason): #function to add book recommendation
    record = f'Book Recommendation------------------------\n {title}\n by {author}\nGenre: {genre}\nReason: {reason}\n\n' #record with a book recommendation
    save_record(record) #save the record into the file

def save_record(record): #function to save the record into the file
    with open(FILE_NAME, 'a') as file: #open the file in append mode
        file.write(record) #write the record into the file
    #print("Record saved successfully\n") #print message that the record was saved

def words_count(inputFile, outputFile): #generate cvs with word-count (all words are preprocessed in lowercase) from news_feed.txt
    with(open(inputFile, 'r')) as file: #open the file in read mode
        text = file.read() #read the file
        words = cleanText(text) #lowwer case and remove non-alphanumeric characters
        word_count = Counter(words) #count the words
    with open(outputFile, 'w', newline='', encoding='utf-8') as csvfile: #
        writer = csv.writer(csvfile) #create a csv writer
        writer.writerow(['WORD', 'COUNT'])  # Write header in capital letters
        for word, count in word_count.most_common():  # Sort by most common words
            writer.writerow([word, count]) #write the word and the count
    print(f'Word count statistics saved in {outputFile}')

def letters_count(inputFile, outputFile): #2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)
    with(open(inputFile, 'r')) as file: #open the file in read mode
        text = file.read() #read the file
        text = ''.join([char for char in text if char.isalpha()]) #remove all non-alphabetic characters
        count_all = {} #initialize the count_all dictionary
        for char in text.lower(): #for each character in the text
            count_all[char] = count_all.get(char, 0) + 1 #count the characters
        count_uppercase = {} #initialize the count_uppercase dictionary
        for char in text: #
            if char.isupper():#check if the character is uppercase
                char_lower = char.lower() #convert the character to lowercase
                count_uppercase[char] = count_uppercase.get(char, 0) + 1 #count the uppercase characters

        data = []#initialize the data list
        for letter in sorted(count_all.keys()):#for each letter in the sorted keys
            count_all_letter = count_all[letter] #get the count of all occurrences of the letter
            count_upper_letter = count_uppercase.get(letter, 0) #get the count of uppercase occurrences of the letter
            percentage_uppercase = (count_upper_letter / count_all_letter) * 100  # Percentage of uppercase out of all occurrences of the letter
            data.append([letter.upper(), count_all_letter, count_upper_letter, round(percentage_uppercase, 2)]) #append the data to the list
    with open(outputFile, 'w', newline='', encoding='utf-8') as csvfile: #open the file in write mode
        writer = csv.writer(csvfile) #create a csv writer
        writer.writerow(['LETTER', 'COUNT_ALL', 'COUNT_UPPERCASE', 'PERCENTAGE']) #write the header in capital letters
        for row in data: #for each row in the data
            writer.writerow(row) #write the row
    print(f'Letter count statistics saved in {outputFile}') #print a message that the letter count statistics were saved

def process_statistics(): #function to process the statistics
    words_count(FILE_NAME, WORDS_FILE_NAME) #call the word count function
    letters_count(FILE_NAME, LETTER_FILE_NAME) #call the letter count function
    pass

def main(): #main function
    while True: #infinite loop to keep adding records
        print("Select the type of record to add:")
        print("1. News")
        print("2. Private Ad")
        print("3. Book Recommendation")
        print("4. Exit")
        option = input("Enter your choice: ") #get the option from the user
        if option == '1': #if the option is 1 add news
            text = input('Enter the news text: ')  # get the text for the news
            city = input('Enter the city: ')  # get the city for the
            add_news(text,city)
        elif option == '2': #if the option is 2 add private ad
            text = input('Enter the private ad text: ')  # get the text for the private ad
            expiration_date = input('Enter the expiration date (yyyy-mm-dd): ')  # get the expiration date
            expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d') #convert the expiration date to datetime
            add_private_ad(text, expiration_date)
        elif option == '3': #if the option is 3 add book recommendation
            title = input('Enter the book title: ')  # get the title of the book
            author = input('Enter the author: ')  # get the author of the book
            genre = input('Enter the genre: ')  # get the genre of the book
            reason = input('What do you love about this book?: ')  # Why is so amazing this book?
            add_book_recommendation(title, author, genre, reason)
        elif option == '4': #if the option is 4 exit the program
            break
        else:
            print("Invalid choice. Please, try again\n") #if the option is invalid print a message

if __name__ == '__main__': #if the script is executed directly
    main() #call the main function