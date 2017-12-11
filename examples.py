# TODO
# I need prepared examples of common tasks

a = range(10)
b = range(100,110)
c = ['apple', 'banana', 'cranberry', 'contoloupe', 'cantaloupe', 'durian', 'fig']

print('a', list(a))
print('b', list(b))
print()

tmp = zip(a,b)
print('zip', list(tmp))

tmp = map(lambda x: x+5, a)
print('map', list(tmp))

tmp = sorted(c)
print('lexico sort', tmp)

tmp = sorted(c, key=len)
print('len sort', tmp)

tmp = sorted(c, key=len, reverse=True)
print('len sort', tmp)



# class TreeNode

# dfs
# bfs

# Graphs
# dfs
# bfs
# A*


print()