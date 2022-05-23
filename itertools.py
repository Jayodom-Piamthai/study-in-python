#Itertools-collection of tools for handling iterators
#product,permutations,combunations,accumulate,groupby,infinite itteration
from itertools import product
a =[1,2]
b=[5,8]
prod = product(a,b)
prodRep = product(a,b,repeat=2)
print(list(prod))
print(list(prodRep))