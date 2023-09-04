def pattern(st,n):
    var = n-2
    for i in range(1,n):
        t = 2*i-1
        print(f'{var*" "}{st*t}')
        var -= 1


pattern('*',7)

#    *
#   ***
#  ******
# ********
