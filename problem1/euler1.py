def sum_of_multiples(size):
    return sum([x for x in range(size) if (x % 3 == 0 or x % 5 == 0)])

def main():
    print sum_of_multiples(1000)

if __name__ == '__main__':
    main()