def sort_array(source_array):
    evens = [(i, v) for i, v in enumerate(source_array) if v % 2 == 0]
    odds = sorted([x for x in source_array if x % 2 != 0])
    list(map(lambda x: odds.insert(x[0], x[1]), evens))
    return odds

if __name__ == "__main__":
    test_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"sorted odds from {test_array} are {sort_array(test_array)}")
