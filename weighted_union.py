# -*- coding: utf-8
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
# weight|width of tree
width_size = [1 for i in range(0, 10)]
# group size by root
group_size = 10

print('group size:', group_size)
print('width_sz  ->', width_size)
print('original  ->', point_lst)

# implement interface
def linked_in(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    ###################
    # weighted union #
    #################
    s1 = width_size[p1]
    s2 = width_size[p2]
    root = r1
    if s1 < s2:
        root = r2
    if r1 == root:
        point_lst[r2] = root
        width_size[p1] = s1 + 1
        width_size[p2] = 0
    elif r2 == root:
        point_lst[r1] = root
        width_size[p2] = s2 + 1
        width_size[p1] = 0
    # set group size
    global group_size
    group_size = group_size - 1

def is_linked(p1, p2):
    return find_root(p1) == find_root(p2)

def find_root(point):
    root = point
    while point_lst[root] != root:
        root = point_lst[root]
    # 压缩路径 提高 find 效率
    if root != point:
        point_lst[point] = root
        width_size[point] = 0
    return root

# connect each union
for (p1, p2) in union_lst:
    if not is_linked(p1, p2):
        linked_in(p1, p2)
print('connected ->', point_lst)

###
# point to root with re-find
###
for index in range(0, 10):
    point_lst[index] = find_root(index)

print('point root->', point_lst)
print('width_sz  ->', width_size)
print('group size:', group_size)