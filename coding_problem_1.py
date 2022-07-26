# Problem 1
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

list_sample = [10, 15, 3, 7]
k = 17

from typing import Optional, List

def add_upto_k(k: int, array: Optional[List] = None) -> bool:
    assert array, "Non array input"
    assert len(array) != 0, "Array is empty"
    
    diff_set = set()
    
    for iterator in array:
        diff = k - iterator
        if iterator in diff_set:
            return True
        diff_set.add(diff)
    return False

if __name__ == '__main__':
    print(add_upto_k(k, list_sample))
