# Dyllan Vangemert
# 06/03/2020
# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """
    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                w = w.lower()
                count = ht.get(w)
                if ht.contains_key(w):
                    ht.put(w, count+1)
                else:
                    ht.put(w, 1)

    # Add all items in hash table to list
    sorted_list = []
    for list in ht.get_buckets():
        current = list.head
        for tuple in range(list.size):
            sorted_list.append((current.key, current.value))
            current = current.next

    # Sort list by value in descending order. Return given number of 'top-words'.
    sorted_list = sorted(sorted_list, key=get_second, reverse=True)
    return_list = []
    for i in range(number):
        return_list.append(sorted_list[i])
    return return_list

def get_second(elem):
    """Returns the second element of an array"""
    return elem[1]
