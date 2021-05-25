def check_numbers_list(check_numbers,check_numbers1):
    i=0
    while i<len(check_numbers):
        if check_numbers[i]%2==0 and check_numbers1[i]%2==0:
            print("dono even hai")
        elif check_numbers[i]%2!=0 and check_numbers1[i]%2!=0:
            print("dono even nhi hai")
        i=i+1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

