import math


def divide_nums (a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: by zero is not allowed")
    except TypeError as e:
        print(f'error:{e}')
    except Exception:
        print("Error: Unexpected error occured")
    finally:
        print("this will be always executed regardless of exceptions")


result = divide_nums(10, math.sqrt(-1))
print("Results: ",result)

