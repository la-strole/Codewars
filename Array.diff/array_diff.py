def array_diff(a, b):
    return [i for i in a if i not in b]

if __name__ == "__main__":
    test_a = [1,2,2,2,3]
    test_b = [2]
    print(f"difference between {test_a} and {test_b} is {array_diff(test_a, test_b)}")
