#this algorithm return an index in an array which can make a perfect square of a given number
def isPerfectSquare(num):
    l,h=0,num
    while l<=h:
        m = (l+h)>>1
        if m*m == num:
            return True
        else:
            if m*m < num:
                l = m+1
            else:
                h = m-1
    return False
isPerfectSquare(16)
