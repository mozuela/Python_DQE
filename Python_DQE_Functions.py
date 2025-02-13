#Python DQE Functions: Julia Mendoza Verduzco

import re
from string import punctuation
from unicodedata import normalize

inital_string = ""
position_for_insert = "paragraph." #position to insert the last words after the sentence ending in paragraph

def count_whitespaces(text): #counting all whitespaces using isspace() method
    count = 0 #initialize count
    for char in text: #loop through the text
        if char.isspace():  #check if the character is a whitespace
            count += 1 #increment count
    return count #return total count of whitespaces found

def get_last_words(text):#
    sent = text.split('\n') #split the text into sentences
    last_words = [] #initialize list to store last words
    for sentence in sent: #for each sentence
        if sentence: #check if the sentence is not empty
            words = sentence.split() #split the sentence into words
            if words: #check if the words are not empty
                last_words.append(words[-1]) #append the last word to the list for each sentence
    return last_words #return the list of last words

def normalize_text(text): #function to normalize the text
    sentences = text.split('\n')  # splitting the text into sentences to normalize
    normalized_sentences = [sentence.strip().capitalize() for sentence in sentences]  # capitalize each sentence
    normalized_text = ' \n'.join(normalized_sentences)  # joining the sentences back together
    return normalized_text #return the normalized text

def clean_mul(text):
    text = re.sub(r'\xa0', '', text) #removing non-breaking character/code
    sentences = text.split('\n') #splitting the text into sentences to normalize
    normalized_sentences = [sentence.strip().capitalize() for sentence in sentences] #capitalize each sentence
    normalized_text = ' \n'.join(normalized_sentences) #joining the sentences back together
    fixed_iz = normalized_text.replace(' iz ', ' is ') #replacing iz with is just when is followed by a space/it's a mistake
    last_words = get_last_words(fixed_iz) #get the last words of each sentence
    last_words_phrase = ' '.join(last_words)    #joining the last words together
    insert_index = fixed_iz.find(position_for_insert)+len(position_for_insert)+1 #find the position of the end of the "paragraph." sentence
    paragraph_with_last_words = fixed_iz[:insert_index] + last_words_phrase + fixed_iz[insert_index:] #insert the last words after the sentence ending in paragraph
    clean_line = re.sub(r'[ \t]+', ' ', paragraph_with_last_words)    #removing extra spaces and tabs
    clean_line = re.sub(r'\n\s*\n', '\n', clean_line) #removing extra new lines
    return clean_line #return the cleaned text


def main():
    clean_multiline = clean_mul(inital_string) #cleaning the text

    count_spaces = count_whitespaces(clean_multiline) #counting all whitespaces
    print("Initial text: \n ", inital_string) #printing the initial text
    print("Final text: \n ", clean_multiline) #printing the processed text
    print("Count whitespaces: ",count_spaces) #total count of whitespaces found in the text

if __name__ == '__main__':  # if the script is executed directly
    main()  # call the main function
