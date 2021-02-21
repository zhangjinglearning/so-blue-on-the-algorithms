# Successor with delete. Given a set of n integers  S = { 0, 1, ... , n-1 } and a sequence of requests of the following form:

# Remove x from S
# Find the successor of x: the smallest y in S such that y>= x.
# design a data type so that all operations (except construction)  take logarithmic time or better in the worst case.

s = [i for i in range(0, 10)]
print(s)

def successor_with_delete(index):
    if index == 10:
        return False
    elif s[index] != -1:
        s[index] = -1
    else:
        successor_with_delete(index + 1)

# the -1 means deleted
s[2] = -1
successor_with_delete(2)
print(s)
s[0] = -1
successor_with_delete(0)
print(s)
s[2] = -1
successor_with_delete(2)
print(s)
s[1] = -1
successor_with_delete(1)
print(s)