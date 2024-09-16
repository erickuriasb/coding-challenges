'''
    Given two strings, write a method to decide if one is a permutation of the other.

    Hints:
        - 1. Describe what it means for two strings to be permutations of each other. 
            Now, look at that definition you provided. Can you check the strings against that 
            definition?
        - 84. There is one solution that is 0(N log N) time. Another solution uses some space, 
            but isO(N) time.
        - 122. Could a hash table be useful?
        - 131. Two strings that are permutations should have the same characters, but in different 
            orders. Can you make the orders the same?

        Solution:
        Like in many questions, we should confirm some details with our interviewer. We should 
        understand if the permutation comparison is case sensitive. That is: is God a permutation 
        of dog? Additionally, we should ask if whitespace is significant. We will assume for this 
        problem that the comparison is case sensitive and whitespace is significant. So, "god " is 
        different from "dog".
        Observe first that strings of different lengths cannot be permutations of each other. There 
        are two easy ways to solve this problem, both of which use this optimization.
'''


def check_permutation(phrase_1, phrase_2):
    '''
        docstring
    '''
    if len(phrase_1) != len(phrase_2):
        return False
    phrase_1 = list(phrase_1)
    phrase_2 = list(phrase_2)
    phrase_1.sort()
    phrase_2.sort()
    if phrase_1 != phrase_2:
        return False
    return True
