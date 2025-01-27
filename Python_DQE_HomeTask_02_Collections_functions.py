# Home task 02: Python collections Julia Mendoza Verduzco
"""1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example:{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}"""

import random #import random module to generate random numbers and letters

#Create random list of dictionaries
def create_list_of_dicts():
    list_of_dicts = [] #list of dictionaries
    for i in range(random.randint(2, 10)): #random number of dictionaries from 2 to 10
        dict_of_numbers = {} #dictionary for the iteration
        for j in range(random.randint(1, 26)): #random number of keys using letters from a to z
            dict_of_numbers[random.choice('abcdefghijklmnopqrstuvwxyz')] = random.randint(0, 100) #random letter key from a to z and random numeric value from 0 to 100
            sorted_dict = {key: dict_of_numbers[key] for key in sorted(dict_of_numbers)} #sort the dictionary by keys
        list_of_dicts.append(sorted_dict) #adding the dictionary to the list
    return list_of_dicts #retunrning the list of dictionaries

dictionaries = create_list_of_dicts() #create the list of dictionaries
print("Initial data: ", dictionaries)

all_keys = set(key for d in dictionaries for key in d.keys()) #get all the keys from the dictionaries
sorted_keys = sorted(all_keys) #sort the keys

def clean_dict(d): #function to clean the dictionary
    #get the max value for each key and create a new key with the dictionary number
    for key in sorted_keys: #for each key in the sorted keys
        max_value = 0 #initialize the max value
        max_key = '' #initialize the max key
        for i, d in enumerate(dictionaries): #iterate the dictionaries
            if key in d: #if the key is in the dictionary get the index/number of the dictionary for the max value
                if d[key] > max_value: #if the value is greater than the max value
                    max_value = d[key] #set the max value
                    max_key = key #set the max key
                    max_i = i #set the dictionary number
        if max_value > 0: #if the max value is greater than 0
            for i, d in enumerate(dictionaries): #iterate the dictionaries
                if i == max_i: #if this dictionary has the max value
                    d[key + '_' + str(i + 1)] = d.pop(key) #rename the key with the dictionary number
                elif key in d : #remove the key from the other dictionaries
                    d.pop(key) #remove the key to leave it just in the dictionary with the max value

    final_dictionary = {}  #initialize the final dictionary to combine the multiple dictionaries in one
    for d in dictionaries: #iterate the dictionaries
        for key, value in d.items(): #iterate the items in the dictionary
            if key in final_dictionary: #if the key already exist in the final/combined dictionary get the max value
                if value > final_dictionary[key]: #if the value is greater than the value in the final dictionary
                    final_dictionary[key] = value #set the value in the final dictionary
            else:
                final_dictionary[key] = value #if not leave the key/value as is

    #sort the dictionary with unique key/values pairs
    sorted_dict = dict(sorted(final_dictionary.items())) #sort the dictionary by keys
    return sorted_dict #return the sorted dictionary

#removing _1 for the unique values
cleaned_dict = {} #initialize the cleaned dictionary
dictionary = clean_dict(dictionaries) #clean the dictionary
for key, value in dictionary.items(): #for each
    if key.endswith('_1'): #if key has _1 at the end
        key = key[:-2] #remove the _1
        cleaned_dict[key] = value #add the key without _1 to the cleaned dictionary
    else: #if was a unique key
        cleaned_dict[key] = value #just move the key/value to the cleaned dictionary

print("Final dictionary sorted ", cleaned_dict) #print the cleaned dictionary



