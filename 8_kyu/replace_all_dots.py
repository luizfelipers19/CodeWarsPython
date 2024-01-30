# The code provided is supposed replace all the dots . in the specified String str with dashes -

# But it's not working properly.

# Task
# Fix the bug so we can all go home early.

# Notes
# String str will never be null.


import re

def replace_dots(s):
    return s.replace(".", "-")

    
# def replace_dots(s):
#     answer = ""
#     for i in range(len(s)):
#         if s[i] == ".":
#             answer += "-"
#         else:
#             answer += s[i]
#     return answer