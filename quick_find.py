# Dynamic Connectivity
# Question
# How many connected components result after performing the following sequence of union operations on a set of items?

# init data
# constantly data
u1 = (1, 2)
u2 = (3, 4)
u3 = (5, 6)
u4 = (7, 8)
u5 = (7, 9)
u6 = (2, 8)
u7 = (0, 5)
u8 = (1, 9)
union_lst = (u1, u2, u3, u4, u5, u6, u7, u8)
# point to itself
point_lst = [i for i in range(0, 10)]
# group size by root
group_size = 10

print('group size:', group_size)
print('original ->', point_lst)

# implement interface
def linked_in(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    # link rule
    root = min(r1, r2)
    ##############
    # link more #
    ############
    for index in range(0, 10):
        point = point_lst[index]
        if point == r1 or point == r2:
            point_lst[index] = root
    # set group size
    if find_root(root) == root:
        global group_size
        group_size = group_size - 1

def is_linked(p1, p2):
    return find_root(p1) == find_root(p2)

def find_root(point):
    ###############
    # quick find #
    #############
    return point_lst[point]

# connect each union
for (p1, p2) in union_lst:
    if not is_linked(p1, p2):
        linked_in(p1, p2)
print('connected->', point_lst)

###
# point to root
# already linked by link more
###
print('point to ->', point_lst)
print('group size:', group_size)