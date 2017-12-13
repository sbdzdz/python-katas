def draw_triangle(n):
    for i in range(n):
        print (i+1) * '* '

def draw_reversed_triangle(n):
    for i in range(n, 0, -1):
        print 2*(n-i) * ' ' + (2*i-1) * ' *'
