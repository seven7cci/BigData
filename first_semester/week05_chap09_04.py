# week01 prime number, update version
start_no = int(input("Enter Starting Number : "))
end_no = int(input("Enter Ending Number : "))

for k in range(start_no, end_no+1):
    is_prime = True

    if k <= 1:
        is_prime = False
    else:
        for i in range(2, k):
            if k % i == 0:
                is_prime = False
                break
        if is_prime:
            print(k, end=" ")
