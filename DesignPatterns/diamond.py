def diamond(n: int):
    for i in range(n):
        x = (i * 2) + 1
        print(f"{(n-i-1) * ' '}{x*'*'}")

    y = n-1

    while y:
        print(f"{(n-y) * ' '}{(2*y-1)*'*'}")
        y -= 1



diamond(10)
