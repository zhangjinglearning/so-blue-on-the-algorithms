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
# root map
rootDict = dict()

# implement interface
def linked_in(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    root = min(r1, r2)

    if root not in rootDict:
        rootDict[root] = set()
    rootDict.get(root).add(p1)
    rootDict.get(root).add(p2)

    silbing = max(r1, r2)
    linked_sibling(silbing, root)

def linked_sibling(from_root, to_root):
    del_root_lst = list()
    for root in rootDict:
        if root == from_root:
            toggl = rootDict[to_root].union(rootDict[root])
            rootDict[to_root] = toggl
            del_root_lst.append(root)
    for root in del_root_lst:
        del rootDict[root]

def is_linked(p1, p2):
    r1 = find_root(p1)
    r2 = find_root(p2)
    return r1 == r2

def find_root(point):
    current_root = point
    for root in rootDict:
        if point in rootDict[root]:
            current_root = root
    return current_root

# connect to be a line
for union in union_lst:
    p1 = union[0]
    p2 = union[1]
    flag = is_linked(p1, p2)
    if not flag:
        linked_in(p1, p2)

for root in rootDict:
    print(root, ':', rootDict[root])