def in_array(array1, array2):
    return sorted(set([x for x in array1 if x in ' '.join(array2)]))

if __name__ == "__main__":
    test_arr1 = ["arp", "live", "strong"]
    test_arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    print(f"result of strings {test_arr1} and {test_arr2} is {in_array(test_arr1, test_arr2)}")
