"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array.

    >>> output_all_items([1, 'hello', True])
    1
    hello
    True
    """

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers.
    
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """

    # even_nums = []
    # for num in nums:
    #     if num % 2 == 0:
    #         even_nums.append(num)
    # return even_nums
    return [num for num in nums if num % 2 == 0]


def get_odd_indices(items):
    """ Given an array, return all elements at odd numbered indices.

    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
    """

    # index_list = []
    # for i in range(len(items)):
    #     if i % 2 != 0:
    #         index_list.append(items[i])    
    # return index_list
    return [items[i] for i in range(len(items)) if i % 2 != 0]


def print_as_numbered_list(items):
    """Given an array, output a numbered list.

    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    """
    
    for i,item in enumerate(items):
        print(f"{i+1}. {item}")
        

def get_range(start, stop):
    """"Return an array of numbers in a certain range.

    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]
    >>> get_range(1, 3);
    [1, 2]
    """

    return list(range(start, stop))


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'. 
        
    >>> censor_vowels('hello world');
    'h*ll* w*rld'
    """

    replaced_vowels = ""
    for letter in word:
        if letter in 'aeiou':
            replaced_vowels += "*"
        else:
            replaced_vowels += letter
    return replaced_vowels
    # return "".join('*' if letter in 'aeiou' else letter for letter in word)


def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case.

    >>> snake_to_camel('hello_world')
    'HelloWorld'
    """
    
    # new_string = ""
    # split_list = string.split("_")
    # for word in split_list:
    #     new_string += word.title()
    # return new_string
    return "".join(word.title() for word in string.split("_"))


def longest_word_length(words):
    """Return the length of the longest word in the given array of words.

    >>> longest_word_length(['hello', 'world'])
    5
    
    >>> longest_word_length(['jellyfish', 'zebra'])
    9
    """

    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length


def truncate(string):
    """Truncate repeating characters into one character.

    >>> truncate('aaaabbbbcccca')
    'abca'

    >>> truncate('hi***!!!! wooow')
    'hi*! wow'
    """

    truncated = string[0]
    for index in range(len(string)-1):

        if string[index] != string[index + 1]:
             truncated += string[index + 1]
          
    return truncated


def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced.

    >>> has_balanced_parens('()')
    True

    >>> has_balanced_parens('((This) (is) (good))')
    True

    >>> has_balanced_parens('(Oh no!)(')
    False
    """


def compress(string):
    """Return a compressed version of the given string.

    >>> compress('aabbaabb');
    'a2b2a2b2'

    If a character appears once, it shouldn't be followed by a number:
    >>> compress('abc');
    'abc'

    The function should handle all types of characters:
    >>> compress('Hello, world! Cows go moooo...');
    'Hel2o, world! Cows go mo4.3'
    """
