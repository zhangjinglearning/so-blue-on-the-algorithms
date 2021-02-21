# Social network connectivity. Given a social network containing n members and a log file containing m timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be m log n or better and use extra space proportional to n.

# Note: these interview questions are ungraded and purely for your own enrichment. To get a hint, submit a solution.

# union (member, member, date)
u1 = (1, 2, 1964)
u2 = (3, 4, 1965)
u3 = (5, 6, 1987)
u4 = (7, 8, 1997)
u5 = (7, 9, 1998)
u6 = (2, 8, 2008)
u7 = (0, 5, 2012)
u8 = (1, 9, 1019)
u9 = (0, 1, 2020)
u10 = (1, 3, 2021)
u11 = (2, 7, 2022)
union_log_lst = (u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11)
point_lst = [i for i in range(0, 10)]

# implement interface
def linked_in(m1, m2):
    r1 = find_root(m1)
    r2 = find_root(m2)
    # link rule
    root = min(r1, r2)
    ##############
    # link more #
    ############
    for index in range(0, 10):
        point = point_lst[index]
        if point == r1 or point == r2:
            point_lst[index] = root

def is_linked(m1, m2):
    return find_root(m1) == find_root(m2)

def find_root(point):
    ###############
    # quick find #
    #############
    return point_lst[point]

def is_percolation():
    flag = True
    root = point_lst[0]
    for point in point_lst:
        if root != point:
            flag = False
    return flag

# connect each union
for (m1, m2, date) in union_log_lst:
    if not is_linked(m1, m2):
        linked_in(m1, m2)
        if is_percolation():
            print(date)
            break