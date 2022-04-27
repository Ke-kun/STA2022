def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    nums = [i for i in range(30, 61)]
    for n in nums:
        if is_prime(n) is True:
            print('Prime')
        else:
            print(n)
