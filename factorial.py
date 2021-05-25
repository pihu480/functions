def factorial(i):
    f=1
    while i>0:
        f=f*i
        i=i-1
    print("factorial",f)
factorial(int(input("enter the number")))
