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
