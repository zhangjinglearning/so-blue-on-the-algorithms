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
# root ref
point_lst = [i for i in range(0, 10)]
print(point_lst)

# implement interface
def linked_in(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    root = min(r1, r2)

    if r1 == root:
        point_lst[r2] = root
        linked_sibling(r2, root)
    elif r2 == root:
        point_lst[r1] = root
        linked_sibling(r1, root)

def linked_sibling(from_root, to_root):
    for (p1, p2) in union_lst:
        if point_lst[p1] == from_root:
            point_lst[p1] = to_root
        elif point_lst[p2] == from_root:
            point_lst[p2] = to_root

def is_linked(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    return r1 == r2

def find_root(point):
    current_point = point
    while point_lst[current_point] != current_point:
        current_point = point_lst[current_point]
    return current_point

# connect to be a line
for union in union_lst:
    p1 = union[0]
    p2 = union[1]
    flag = is_linked(p1, p2)
    if not flag:
        linked_in(p1, p2)

print(point_lst)