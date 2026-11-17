# Dictionaires

# Dictionaries are implemented as hash maps or hash tables with hash functions.
# A dictionary is a pairing between the set of keys and the set of values.
# Every entry in the dictionary is key : value pair.

# reminder: when it comes to a dictionary you already have knowledge about the keys
phone_pair = {"Mia" : "555-424-3376"} # creating a dictionary | key first, value second
print(phone_pair)
print(phone_pair["Mia"]) # looking up Mia's phone number

# Immutable vs. Mutable types
# Mutable data can be changed and often is in memory. A structured data list
# is a mutable data structure. Strings are immutable. When it looks like a
# string is betin changed, there is actually a new string object created and
# the old one is discarded.
# username = ''
# username = last + '_' + first[0]
# username = username + first[1]

# The keys of the dictionary have to be an immutable type. This is so that the
# hash function obtains the same value every time.

# The values in a dictionary can be of any type.

# Empty dictionary
my_dict ={}

phone_list = {"Caroline" : "555-3691", "Mori" : "555-2211", "Keoki" : "555-1133"}

print(phone_list.keys()) # gets you the keys
print(phone_list.values()) # gets you the values

# Add to a dictionary

phone_list["Saanvi"] = "222-3145"
print(phone_list)

phone_list["Keoki"] = "555-1313" # edit a specific part of the dictionary 
print(phone_list)

# An Exercise for you
def freq_count(phrase):
    '''
    Purpose: Count the number of occurences for each character in the prase
    and return a dictionary with those counts.

    Parameters: phrase - the phrase we are getting the frequency for; str

    Return Value: - a dictionary with a freq count for each character in phrase; dict
    '''

    char_count ={}

    for character in phrase:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

def freq_count_words(phrase):
    '''
    Change freq_count so that it returns the frequency count of words in
    the phrase instead of the characters.
    '''

    word_count ={}

    words = phrase.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Write a function

def classList(students, year):
    '''
    Purpose: To take a dictionary students with student : grad year pairs
    and produce a list with students who graduate in the parameter year.

    Parametes
        students - a dictionary with names as keys and class year as values; dict
        year - the year that the students are graduating; int

    Return Value: List of students who are graduating in the year; list
    
    Example: 
        >>> student_list = ["Caroline" : 2027, "Xavier" : 2030, "Melissa" : 2029, "Kathy" : 2027]
        >>> classList(student_list, 2030)
        '["Xavier"]'
        >>> classList(student_list, 2027)
        '["Caroline", "Kathy"]'
        >>> classList(studen_list), 2022)
        '[]'
    '''

    names = []

    for person in students:
        if students[person] == year:
            names.apppend(person)
    return names
    

if __name__ == "__main__":
    my_phrase = "Today is my birthday and I'm turning 16!"
    print(freq_count(my_phrase))

    my_phrase = "Hello, hello everyone!"
    print(freq_count_words(my_phrase))

    student_list = {"Caroline" : 2027, "Xavier" : 2030, "Melissa" : 2029, "Kathy" : 2027}
    print(classList(student_list, 2027))