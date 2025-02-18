## Home task 08: JSON Julia Mendoza Verduzco
"""Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""
import json
import os  # import os module to manipulate the files
import sys
from datetime import datetime  # import datetime module to get the current date

from Python_DQE_Functions import normalize_text as cleanText  # import the function to clean the text
from Python_DQE_HomeTask_05_OOP import add_news, add_private_ad, add_book_recommendation, process_statistics  # import the functions from the previous homework
from Python_DQE_HomeTask_05_OOP import main as manually_add  # import the main function from the previous homework

FILE_NAME = 'news_feed.txt' #file to write the news feed
WORDS_FILE_NAME = 'words_statistics.txt' #file to write the news feed
LETTER_FILE_NAME = 'letters_statistics.txt' #file to write the news feed
DEFAULT_FOLDER = 'Files' #default folder  to save the files
sys.path.append(os.path.dirname(__file__))

def load_records_from_file(file_path): #function to load records from a file
    if not os.path.exists(file_path): #check if the file exists
        print("The file does not exist\n") #print a message that the file does not exist
        return #return to the main function
    print(f"Loading records from file: {file_path}\n") #print a message that the records are being loaded from the file
    try:
        with open(file_path, 'r') as file: #open the file in read mode
            for line in file: #for each line in the file
                process_record(line.strip()) #strip the line
        os.remove(file_path) #remove the file after processing
        print("File processed and removed successfully\n") #print a message that the file was processed and removed
    except Exception as e:
        print(f"An error occurred processing the file: {e}\n") #print a message that an error occurred

def load_records_from_file_json(file_path):
    if not os.path.exists(file_path): #check if the file exists
        print("The file does not exist\n") #print a message that the file does not exist
        return #return to the main function
    print(f"Loading records from file: {file_path}\n") #print a message that the records are being loaded from the file
    try:
        with open(file_path, 'r') as file: #open the file in read mode
            records = json.load(file)
            if isinstance(records, list):
                for record in records:
                    process_json_record(record) #strip the line
            else:
                    process_json_record(records) #strip the line
        os.remove(file_path) #remove the file after processing
        print("File processed and removed successfully\n") #print a message that the file was processed and removed
    except Exception as e:
        print(f"An error occurred processing the JSON file: {e}\n") #print a message that an error occurred

def process_record(line): #function to process the record
    parts = line.split('|') #split the line into parts
    record_type = parts[0] #get the record type
    if record_type == 'News': #if the record type is News
        text = cleanText(parts[1]) #get the text
        city = cleanText(parts[2]) #get the city
        add_news(text, city) #add the news
    elif record_type == 'Private Ad': #if the record type is Private Ad
        text = cleanText(parts[1]) #get the text
        expiration_date = datetime.strptime(parts[2], '%Y-%m-%d') #get the expiration date
        add_private_ad(text, expiration_date) #add the private ad
    elif record_type == 'Book Recommendation': #if the record type is Book Recommendation
        title = cleanText(parts[1]) #get the title
        author = cleanText(parts[2]) #get the author
        genre = cleanText(parts[3]) #get the2 genre
        reason = cleanText(parts[4]) #get the reason
        add_book_recommendation(title, author, genre, reason) #add the book recommendation
    else:
        print("Invalid record type\n") #print a message that the record type is invalid

def process_json_record(record): #function to process the record
    record_type = record.get('type') #get the record type
    if record_type == 'News': #if the record type is News
        text = cleanText(record.get('text')) #get the text
        city = cleanText(record.get('city')) #get the city
        add_news(text, city) #add the news
    elif record_type == 'Private Ad': #if the record type is Private Ad
        text = cleanText(record.get('text')) #get the text
        expiration_date = datetime.strptime(record.get('expiration_date'), '%Y-%m-%d') #get the expiration date
        add_private_ad(text, expiration_date) #add the private ad
    elif record_type == 'Book Recommendation': #if the record type is Book Recommendation
        title = cleanText(record.get('title'))
        author = cleanText(record.get('author'))
        genre = cleanText(record.get('genre'))
        reason = cleanText(record.get('reason'))
        add_book_recommendation(title, author, genre, reason) #add the book recommendation
    else:
        print("Invalid record type in JSON file \n")

def main(): #main function
    while True: #infinite loop to keep adding records
        print("\n \n Insert manual or from file:")
        print("1. Manual")
        print("2. File")
        print("3. Exit")
        option = input("Enter your choice: ") #get the option from the user
        if option == '1': #if the option is 1 add news, adds or book recommendations manually
            manually_add() #call the main function from the previous homework to add records manually
            process_statistics()  # call the function to process the statistics
        elif option == '2': #if the option is 2 add add news, adds or book recommendations from a file
            custom_file_path = input("Enter the file path fr the input file or press Enter to use default folder: ").strip() #request the file path from the user
            if not custom_file_path: #check if the file path is empty
                custom_file_path = DEFAULT_FOLDER #use the defaul folder file path
            file_name = input("Enter the file name (txt or json): ").strip() #request the file name from the user
            file_path = os.path.join(custom_file_path, file_name) #join the folder and file name to get the file path
            print(f"File path: {file_path}\n") #print the file path
            if os.path.splitext(file_path)[1] == '.txt': #check if the file extension is json
                load_records_from_file(file_path)  # load the records from the file
            elif os.path.splitext(file_path)[1] == '.json': #check if the file extension is json
                load_records_from_file_json(file_path)  # load the records from the file
            process_statistics()  # call the function to process the statistics
        elif option == '3': #if the option is 3 exit the program
            break
        else:
                print("Invalid choice. Please, try again\n") #if the option is invalid print a message
if __name__ == '__main__': #if the script is executed directly
    main() #call the main function