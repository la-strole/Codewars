def count_bits(n):
    return bin(n).count('1')

if __name__ == "__main__":
    test_n = 1234
    print(f"bits count of {test_n} is {count_bits(test_n)}")
