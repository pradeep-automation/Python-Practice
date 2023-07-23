# [0,1,1,2,,3,5,8,13] ----- 8


def fibonacci(series):
    if series <= 0:
        return []
    elif series == 1:
        return [0]
    elif series == 2:
        return [0,1]
    else:
        fib_series = [0,1]
        len(fib_series)
        while len(fib_series) < series:
            next_term = fib_series[-1]+fib_series[-2]
            fib_series.append(next_term)
        return fib_series


print(fibonacci(5))
