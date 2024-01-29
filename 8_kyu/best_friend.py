# Task
# Given a string, return if a given letter always appears immediately before another given letter.

# Worked Example
# ("he headed to the store", "h", "e") ➞ True

# # All occurences of "h": ["he", "headed", "the"]
# # All occurences of "h" have an "e" after it.
# # Return True

# ('abcdee', 'e', 'e') ➞ False

# # For first "e" we can get "ee"
# # For second "e" we cannot have "ee"
# # Return False

# Examples
# ("i found an ounce with my hound", "o", "u") ➞ True

# ("we found your dynamite", "d", "y") ➞ False
# Notes
# All sentences will be given in lowercase.




def best_friend(txt, a, b):
    result = True
    for i in range(len(txt)):
        if txt[i] == a:
            if i+1 < len(txt) and txt[i+1] == b:
                result = True
            else:
                return False
    return result
