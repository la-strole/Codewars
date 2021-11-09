def sum_pairs(ints, s):
    answer = set()
    for i in ints:
        if s - i in answer:
            return [s-i, i]
        else:
            answer.add(i)

if __name__ == "__main__":
    ints = [1, 4, 8, 7, 3, 15]
    s = 11
    print(sum_pairs(ints, s))
