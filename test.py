# print("write yor string")
# s = input()
# new_S=s.replace(input(), input())
# print(new_S)
#
# x = (1,2,3)
# y = (1,2,3)
#
# print( x == y)
prices = [2,5,6,1,3,8,7,13,11,20,25,28]
def max_profit(profits):
    l, r = 0, 1
    max_p = 0
    while r < len(profits):
        if profits[l] < profits[r]:
            prof = profits[r] - profits[l]
            max_p = max(prof, max_p)
        else:
            l = r
        r += 1
    return max_p


print(max_profit(prices))
