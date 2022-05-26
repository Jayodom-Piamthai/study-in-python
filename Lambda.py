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
print(points2D)
print(pointSorted)