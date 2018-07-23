"""
On the game show The Last Word, the host begins a round by showing the contestant a string S of uppercase English letters. 

The host will then present the contestant with the letters of S, one by one, in the order in which they appear in S. When the host presents the first letter, the contestant writes it on the whiteboard. Each time the host presents a letter, the contestant must write it at the beginning or the end of the word on the whiteboard before the host moves on to the next letter. 

The contestant wins the game if their word is the last of an alphabetically sorted list of all of the possible words that could have been produced.
"""

def solution(s):
   result = s[0] 
   for letter in s[1:]:
       if letter < result[0]:
           result = result + letter
       else:
           result = letter + result
   return result


with open('input', 'r') as infile, open('output', 'w') as out:
    num_testcases = int(next(infile))
    for i in range(num_testcases):
        out.write("Case #{0}: {1}".format(i+1, solution(next(infile))))
