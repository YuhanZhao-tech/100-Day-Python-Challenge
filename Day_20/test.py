# vec = {'right': [1, 0], 'left': [-1, 0],
#        'up': [0, 1], 'down': [0, -1]}['left']
# vec = list(map(lambda n: n*5, vec))
# print(vec)

# head_position = [5, 0]

# head_position = [vec[i]+head_position[i] for i in range(2)]

# print(head_position)

inv = ['a', 'c', 'b']
che = ['d', 'e']

inv = inv+che
print(inv)
inv.sort()

print([1, 2] == list((1, 2)))
