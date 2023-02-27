#Jasmine Bumbray
#CIS 261
#Recursive Function

def fib(b):
    if b == 0:
        return 0 #only works with 0 tried 1,2,and 3
    elif b == 1:
        return 1
    else:
        return fib(b - 1) + fib(b - 2) #will add the number infront to get the next number

def main():
    for i in range(16):
        print(fib(i), end=', ')
    print('. . .')

if __name__ == "__main__":
    main()