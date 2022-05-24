#Itertools-collection of tools for handling iterators
#product,permutations,combunations,accumulate,groupby,infinite itteration
from itertools import combinations_with_replacement, permutations, product,combinations,accumulate,groupby




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
print(list(perm))
 

#03 combinations-combinations of arrangements(permutations,but better)
congii = ["a","c","e","r"]
comb = combinations(congii,2)
comb_wr = combinations_with_replacement(congii,2)#can use same shits
print(list(comb))
print(list(comb_wr))


#4 accumulate-compute the sums or maximun
import operator

ac=[15,20,25,35,12,13,14]
acx=accumulate(ac)#accumulate all stuff
acm=accumulate(ac, func=max)#max number
print(ac)
print(list(acx))
print(list(acm))




