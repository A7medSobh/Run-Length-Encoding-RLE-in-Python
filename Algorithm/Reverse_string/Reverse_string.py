'''
A simple python function that reverse a given string. 
'''
def reverse_string(s):
    res = ""
    end = len(s) -1
    while end >=0:
        res += s[end]
        end -= 1
    return res

word = "Hobbies help reduce stress"
print("\nthe original sentence is :", word)
print("\nthe reversed sentence is :", reverse_string(word))