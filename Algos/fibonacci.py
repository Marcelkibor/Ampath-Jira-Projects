# n-> index of a number in a fibonacci List
def fibonacciNumber(n):
    if n < 0:
        return 0 
    elif n==1:
        return 1
    else:
        fibonacciList = [0,1]
        for i in range (2,n+1):
            fibonacciList.append(fibonacciList[-1]+fibonacciList[-2])
        return "the fibonacci number on index {} is-> {}".format(n,fibonacciList[n])
print(fibonacciNumber(4))