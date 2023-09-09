def pattern(st,n):
    var = n-2
    for i in range(1,n):
        t = 2*i-1
        print(f'{var*" "}{st*t}')
        var -= 1


pattern('*',5)

#    *
#   ***
#  ******
# ********
#
# maxi = [2,4,12,1,8,10,7]
#
#
# def find_max(ls):
#     if not ls:
#         return None
#     else:
#         max_ele = ls[0]
#         for num in ls:
#             if num > max_ele:
#                 max_ele = num
#         return max_ele


# print(find_max(maxi))


# my_array = ['a', 'b', 'c', 'b', 'd', 'e', 'a']
#
#
# def num_occurrences(array, char):
#     count = 0
#
#     for element in array:
#         if element == char:
#             count += 1
#     return count
#
#
# print(num_occurrences(my_array, "b"))
#
