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
print('original  ->', point_lst)

# implement interface
def linked_in(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    ################
    # quick union #
    ##############
    root = min(r1, r2)
    if r1 == root:
        point_lst[r2] = root
    elif r2 == root:
        point_lst[r1] = root

def is_linked(p1, p2):
    return find_root(p1) == find_root(p2)

def find_root(point):
    ################
    # find deeply #
    ##############
    root = point
    while point_lst[root] != root:
        root = point_lst[root]
    point_lst[point] = root
    return root

# connect each union
for (p1, p2) in union_lst:
    if not is_linked(p1, p2):
        linked_in(p1, p2)
print('connected ->', point_lst)

# point to root
root_point_lst = list()
for point in point_lst:
    root_point_lst.append(find_root(point))
print('point root->', root_point_lst)