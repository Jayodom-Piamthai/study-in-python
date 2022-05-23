#5 types of collections-container of values:Counter,Namedtuple,orderdirect,defaultdict,deque
from collections import Counter
#01--counter
eyyo = "sdfghjkjhgertyu"
my_counter = Counter(eyyo)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))