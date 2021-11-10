def move_zeros(array):
   list_without_zero = [x for x in array if x != 0 or type(x) == bool]
   return (list_without_zero+[0]*(len(array)-len(list_without_zero)))

if __name__ == "__main__":
    test_array = [False,1,0,1,2,0,1,3,"a"]
    print(f"original array: {test_array}\nmodified array: {move_zeros(test_array)}")
