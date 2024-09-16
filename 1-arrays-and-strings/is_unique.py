'''
    Implement an algorith to determine if a string has all unique characters.
    What if you cannot use additional data structures?

    Hints:
        - 1. Describe what it means for two strings to be permutations of each other. Now, look at 
        that definition you provided. Can you check the strings against that definition?
        - 84. There is one solution that is 0(N log N) time. Another solution uses some space, but 
        isO(N) time.
        - 122. Could a hash table be useful?
        - 131. Two strings that are permutations should have the same characters, but in different 
        orders. Can you make the orders the same?

    Solution:
    You should first ask your interviewer if the string is an ASCII string or a Unicode string. 
    Asking this question will show an eye for detail and a solid foundation in computer science. 
    We'll assume for simplicity the char­ acter set is ASCII. If this assumption is not valid, we 
    would need to increase the storage size.
    One solution is to create an array of boolean values, where the flag at index i indicates 
    whether character i in the alphabet is contained in the string. The second time you see this 
    character you can immediately return false.
    We can also immediately return false if the string length exceeds the number of unique 
    characters in the alphabet. After all, you can't form a string of 280 unique characters out 
    of a 128-character alphabet.

    It's also okay to assume 256 characters. This would e the case in extended ASCII. You should 
    clarify your assumptions with the interviewer.

    The code below implements the algoritm: 
'''


def is_unique_chars(phrase):
    '''
        docstring
    '''
    unique_chars = {}

    for char in phrase:
        if char in unique_chars:
            return False
        unique_chars[char] = True

    return True


print(is_unique_chars("abcde!a"), end='\n')
# EOF
