def fibbo_recur(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbo_recur(n-2)+fibbo_recur(n-1)
num=int(input("Enter the number: "))

print(fibbo_recur(num))
 
#  0 1 1 2 3 5 8


