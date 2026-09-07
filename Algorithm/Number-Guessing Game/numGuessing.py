import random as rand

def binary_search(array, target):
    
    low = 0  
    high = len(array) -1 # low is the first index and high is the last index in the array
    guesses_num = 0 # number of guesses it takes to get the correct number
    while high >= low: 
        mid = (high + low) // 2 #devide the range in half every iteration of the loop (if target not found)
        guesses_num = guesses_num + 1
        if array[mid] == target:
            return mid, guesses_num # condition 1: target found, return the index and number of guesses

        elif array[mid] < target: 
            low = mid + 1 # condition 2: target is in the right half of the array, so we search the right half

        else:
            high = mid -1 # condition 3: target is in the left half of the array, so we search the left half

    return -1, guesses_num # condition 4: target not found


array = list(range(1, 10001))
target = rand.randint(1, 10000)
index, guesses_num = binary_search(array, target)

print("The target number is:", target)
print("The target number is at index:", index, "\nThe number of guesses:", guesses_num)