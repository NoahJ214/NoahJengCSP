def tree(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print('*',end='')
        for i in range(0,z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()
tree(9)
def pole(n):
    for i in range(0,n):
        for i in range(n+1):
            print(' ', end=' ')
        print('*****')
pole(2)