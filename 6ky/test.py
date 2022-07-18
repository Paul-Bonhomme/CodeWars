import operator
from functools import reduce

str = "999"

print(reduce(operator.mul, [int(x) for x in str], 1))