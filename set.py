set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8}

print(set1)

# Union
union = set1.union(set2)
print('Union: {}'.format(union))

# Intersection
intersection = set1.intersection(set2)
print('Intersection: {}'.format(intersection))

# Difference
difference1 = set1.difference(set2)
print('Difference between 1 to 2: {}'.format(difference1))
difference2 = set2.difference(set1)
print('Difference between 2 to 1: {}'.format(difference2))

# Symetric Difference
symetric = set1.symmetric_difference(set2)
print('Symetric difference: {}'.format(symetric))

# Subset and Superset
set_a = {'dog', 'cat', 'mouse'}
set_b = {'dog', 'cat', 'mouse', 'horse', 'cow'}
print('A is subset from B: {}'.format(set_a.issubset(set_b)))
print('B is superset from A: {}'.format(set_b.issuperset(set_a)))
