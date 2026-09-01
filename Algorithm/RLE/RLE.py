####################################################
#Author: Ahmed Sobh
#Algorithm: Homework #1, Run Length Encoding (RLE)
####################################################

def compress(message):

    compressed = "" # starting with an empty string and append to it later
    count = 1 
    if len(message) == 0: # returns empty string if message is empty
        return ""
    for i in range(1, len(message)):
        if message[i] == message [i-1]: # compares the current char in the message with previous char
            count += 1 # add 1 to the count they are equal

        else: # if not equal, append the count and the previous char to the compressed string
            compressed = compressed + str(count) + message[i-1] 
            count = 1 # resets the counter to 1 for next char in the message
    compressed = compressed + str(count) + message[-1] # appends the last count and char to the compressed string
    return compressed

message = "AAAABBBCCDAA"
compressed_message = compress(message) # function call  (assigned it to a variable)

print("\n\nCompressed message:", compressed_message, "\n" ) # print the assigned variable

def decompress(compressed_message):
    decompressed = "" # start with empty decompressed string
    count = "" # start with empty count string
    for c in range (len(compressed_message)):
        if compressed_message[c].isdigit():
            count += compressed_message[c] # if the character is a digit, append it to the count string
        else:
            decompressed += compressed_message[c] * int(count) # if the character is not a digit, multiply it by the count and append to the decompressed string
            count = "" # reset the count string for the next character
    return decompressed

decoded_message = decompress(compressed_message) # function call (assigned it to a variable)

print("Decoded message:", decoded_message)
print("Correct:", decoded_message == message, "\n")