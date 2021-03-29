import random
import copy
import math

number_lst = []
for index in range(10):
    number_lst.append(random.random())

print('original  list:', number_lst)

# bubble sort
bubble_lst = copy.copy(number_lst)
bubble_lst.sort()
print('bubble    list:', bubble_lst)

# selection sort
selection_lst = []
copy_number_lst = copy.copy(number_lst)
for index in range(10):
    smallest = min(copy_number_lst)
    selection_lst.append(smallest)
    copy_number_lst.remove(smallest)
print('selection list:', selection_lst)

# insertion sort
insertion_lst = []
for num in number_lst:
    insertion_flag = False
    index = 0
    for ins in insertion_lst:
        if ins > num:
            insertion_lst.insert(index, num)
            insertion_flag = True
            break
        index = index + 1
    if not insertion_flag:
        insertion_lst.append(num)
print('insertion list:', insertion_lst)

# shell sort
# 分成多段 insertion sort，有意思吗？难得写不嘛( ╯□╰ )

# merge sort
# 分成两段 selection sort，我靠，没得意思(lll￢ω￢)

# quick sort
quick_lst = copy.copy(number_lst)


def put_pivot(pivot):
    upper_lst = []
    lower_lst = []
    for num in quick_lst:
        if num > pivot:
            upper_lst.append(num)
        elif num < pivot:
            lower_lst.append(num)
    return lower_lst + [pivot] + upper_lst


for num in number_lst:
    quick_lst = put_pivot(num)
print('quick     list:', quick_lst)

# heap sort
# 我叉你个叉，我在哪里去给你找二叉

# counting sort 不支持小数，随便意思意思哈，小范围排序扛把子
counting_lst = random.sample(range(0, 10), 10)
bucket_lst = [[] for i in range(10)]
for count in counting_lst:
    bucket_lst[count].append(count)
table_lst = []
for bucket in bucket_lst:
    table_lst = table_lst + bucket
print('----counting sort----')
print(counting_lst)
print(bucket_lst)
print(table_lst)
print('----sort     over----')

# bucket sort
# 分桶分类各施各技排序

# radix sort 对个十百千万...数位分别进行 counting sort，弄两位意思意思
radix_lst = random.sample(range(0, 100), 10)
box_lst = [[] for i in range(10)]
for radix in radix_lst:
    index = math.floor(radix / 10)
    box_lst[index].append(radix)
print('----radix sort----')
print(radix_lst)
print(box_lst)
for box in box_lst:
    box.sort()
print(box_lst)
print('----sort   end----')
