def longest_consec(strarr, k):
    if len(strarr) == 0 or k <= 0 or k > len(strarr):
        return ""
    return max([''.join(strarr[0+i:k+i]) for i, x in enumerate(strarr)], key=len)

if __name__ == "__main__":
    test_strarr = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
    test_k = 2
    print(f"longest string is {longest_consec(test_strarr, test_k)}")

