def dig_pow(n, p):
    number = sum(int(x)**(p+i) for i, x in enumerate(str(n)))
    if number % n == 0:
        return number / n
    return -1

if __name__ == "__main__":
    test_n = 695
    test_p = 2
    print(f"number={dig_pow(test_n, test_p)}")
