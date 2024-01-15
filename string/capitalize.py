def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))


st = input()
print(solve(st))

"""
--- Method 2
def solve(s):
    return ' '.join([s.capitalize() for s in s.split(' ')])
    
    
st = input()
print(solve(st))
"""
