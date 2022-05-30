
#Python Dictonaries.
programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again.",
 "Loop": "The action of doing something over and over again.",
}

#In dictionary we retrive data through indexing of keys.
# print(programming_dictionary["Bug"])

#Adding Data in dictionary.

# programming_dictionary["Rare"] = "Hello there this is a rare scene"
# print(programming_dictionary)

#Empty dictionary.
#empty_dictionary = {}

#Edit item in a dictionary.

# programming_dictionary["Bug"] = "I am editing an item here i don't care but its balue"
# print(programming_dictionary)

#Loop through the dictionary.
for key in programming_dictionary:
    print(key) #It will print the key inside the dictionary
    print(programming_dictionary[key]) #Now it will print key and its value.
