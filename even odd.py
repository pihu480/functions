def isEven(list):
    i=0
    while i<len(list):
        if list[i]%2==0:
            print("Even Number")
        elif list[i]%2!=0:
            print("Old Number")
        i=i+1
#num=int(input("enter tha number"))
isEven([0,1,2,3])
