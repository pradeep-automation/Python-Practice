""" Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers
such that they add up to a specific target number.
Let these two numbers be
numbers[index1] and numbers[index2]
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space. """

my_lst = [1, 3, 4, 5, 7, 10, 11]
def twosums(ls, target):
    l, r = 0 , len(ls)-1

    while l < r:
        cur_sum = ls[l] + ls[r]
        if cur_sum > target:
            r -= 1
        elif cur_sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []


print(twosums(my_lst, 9))

