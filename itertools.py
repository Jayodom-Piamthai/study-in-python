#Itertools-collection of tools for handling iterators
#product,permutations,combunations,accumulate,groupby,infinite itteration
from itertools import permutations, product,combinations,accumulate,groupby
#01-product-all possible powerset combinations
a =[1,2]
b=[5,8]
prod = product(a,b)
prodRep = product(a,b,repeat=2)
print(list(prod))
print(list(prodRep))


#02-permutations-all possible arrangement combinations
set = [1,3,5,8]
perm = permutations(set)
permof2 = permutations(set,2)#combinations from lenght of two digits,or specific paramiter
print(list(perm))
print(list(permof2))
 

#03 combinations-combinations of arrangements(?????)
congii = [3,5,9,6]
comb = combinations(congii,2)

