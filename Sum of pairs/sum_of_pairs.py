def sum_pairs(ints, s):
    answer = set()
    for i in ints:
        if s - i in answer:
            return [s-i, i]
        else:
            answer.add(i)


print(sum_pairs([1, 4, 8, 7, 3, 15], 11))