def fibonacci(limit):
    fib = [1,2]
    limit_hit = False

    while(not limit_hit):
        next_fib = fib[len(fib)-1] + fib[len(fib)-2]
        if next_fib < limit:
            fib.append(next_fib)
        else:
            limit_hit = True
    return fib

def main():
    fibs = fibonacci(4000000)
    print sum([x for x in fibs if x % 2 == 0])

if __name__ == '__main__':
    main()