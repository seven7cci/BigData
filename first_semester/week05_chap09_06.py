# week01 prime number, update version 2

# is_prime function

def is_prime(n):
    """
    Return True if the argument is prime number. if is not then return False
    :param n: input integer value
    :return: bool (if n is prime number then return True)
    """
    if k <= 1:
        return False
    else:
        for i in range(2, k):
            if k % i == 0:
                return False
    return True


# start_no, end_no = input("Enter Starting & Ending Number : ").split()
# start_no = int(start_no)
# end_no = int(end_no)
start_no, end_no = sorted(map(int, input("Enter Starting & Ending Number : ").split()))

# if start_no > end_no:
#     start_no, end_no = end_no, start_no

for k in range(start_no, end_no+1):
    if is_prime(k):
        print(k, end=" ")
