def largest_prime(num):
    largest = 0
    i = 2
    while i * i <= num:
        if num % i == 0:
            num = num / i
            largest = i
        else:
            i += 1

    if num > largest:
        largest = num
    return largest

def main():
    testnum = 600851475143
    print largest_prime(testnum)

if __name__ == '__main__':
    main()