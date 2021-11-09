def find_uniq(arr):
    if arr[0] == arr[1]:
        same_number = arr[0]
    else:
        same_number = arr[3]
    for item in set(arr):
        if item != same_number:
            return item

if __name__ == "__main__"
    test_array = [ 1, 1, 1, 2, 1, 1 ]
    print(f"unique number in array {test_array} is {find_uniq(test_array)}")
