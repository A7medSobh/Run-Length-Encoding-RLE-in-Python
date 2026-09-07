'''
This is a vowel counter function, it reads a string in either uppercase or lowercase letters
and counts the number of vowels in it (The letters a,e,i,o,u)

EXPLANATION:
the function takes a parameter 's' which is the string to be analyzed, then iterates through each character
using a for loop. It checks if each character is a vowel (uppercase and lowercase), if so, it adds 1 to the counter variable.
At the end it returns the counter variable which has the total number of vowels found in the string.

With a simple function call, we can test the function with a sample string.
'''

def vowels(s):
    counter = 0
    for i in range (len(s)):
        if s[i] in "aeiouAEIOU":
            counter = counter +1
    return counter

word = "I am taking Algorithms this semester and I will try my best in this course!"
print( "number of vowels:",vowels(word), "letters")