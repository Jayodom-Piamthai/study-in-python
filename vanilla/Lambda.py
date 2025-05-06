#Lambda expression:ultra complexing,but shorten the lines to a simple 1-3 lines of code
#structure:
#Lambda arguments:expression

#Example
add10  = lambda x: x + 10 
print(add10(5))

def add10Func(x):
    return x+10
print(add10Func(5))


mult = lambda x,y:x*y
print(mult(3,5))

points2D = [(1,2),(15,1),(5,-1),(10,-4)]
pointSorted = sorted(points2D,key = lambda x:x[1])
pointSortedX = sorted(points2D,key = lambda x:x[0]+x[1])
print(points2D)
print(pointSorted)
print(pointSortedX)


#map(func,seq)
#Example
a=[1,2,3,4,8,12,69]
b=map(lambda x:x+2,a)
print(list(b))
c = [x*2 for x in a]
print(c)
d=filter(lambda x:x%2==0,a)
print(list(d))
e=[x for x in a if x%2==0]
print(list(e))

from functools import reduce
numbs =[2,5,7,9,86]
product_a = reduce(lambda x,y:x*y,numbs)
print(product_a)