# Task
# Create a function that always returns True for every item in a given list. However, if an element is the word 'flick', switch to always returning the opposite boolean value.

# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.


def flick_switch(lst):
    result = []
    defaultBool = True
    for i in range(len(lst)):
        if lst[i] != "flick":
            result.append(defaultBool)
        else:
            defaultBool = switch_bool(defaultBool)
            result.append(defaultBool)
        
    return result

def switch_bool(givenBool):
    return not givenBool