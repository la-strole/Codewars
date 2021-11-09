from collections import OrderedDict


def letter_box(start: int, end: int):
    """
    return list as frequency of digits from 0 to 9 in sequence [start-end]
    :param start: begin of sequence: int
    :param end: end of sequence: int
    :return: result: list
    """
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert 0 < start < end

    digit_dict = OrderedDict.fromkeys(map(str, range(10)), 0)
    for box_number in range(start, end + 1):
        for digit in str(box_number):
            digit_dict[digit] += 1

    return list(digit_dict.values())


def codewars_solution(start, end):
    result = [0 for _ in range(10)]
    for box_number in range(start, end + 1):
        for digit in str(box_number):
            result[int(digit)] += 1
    return result

if __name__ == "__main__":
    test_start = 1
    test_end = 999
    print(f"frequency of digits from 0 to 9 in sequence {test_start}-{test_end} = {letter_box(test_start, test_end)}")
