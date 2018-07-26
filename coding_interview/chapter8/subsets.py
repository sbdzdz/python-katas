def find_subsets(s):
    if not s:
        return [[]]
    if len(s) == 1:
        return [[], s]
    subsets = [] 
    for subset in find_subsets(s[1:]):
        print(subset)
        subsets.append([s[0]]+subset)
    return subsets

print(find_subsets([0, 1, 2, 3, 4]))
