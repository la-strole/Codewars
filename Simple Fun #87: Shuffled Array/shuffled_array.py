from random import randint


def correct_mistake(shuffled_array: list) -> list:
    """
    find and rebove element wich is sum of array elements. return sorted array without sum
    :param shuffled_array: array: list
    :return: sorted array : list
    """
    assert isinstance(shuffled_array, list)
    assert 2 <= len(shuffled_array) <= 30
    for i in shuffled_array:
        assert isinstance(i, int)
        assert -300 <= i <= 300

    for i in shuffled_array:
        if i == sum(shuffled_array) - i:
            return_array = shuffled_array.copy()
            return_array.remove(i)
            return sorted(return_array)


if __name__ == "__main__":
    # make test array
    while True:
        test_array = [randint(-300, 300) for _ in range(randint(2, 31))]
        if -300 <= sum(test_array) <= 300:
            test_array.insert(randint(0, len(test_array)), sum(test_array))
            break
    print(f"mistake_array:{test_array}\ncorrect_array:{correct_mistake(test_array)}")
