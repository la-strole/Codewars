from itertools import combinations


def choose_best_sum(t, k, ls):
    if len(ls) >= k:
        max_distance = max(combinations(ls, k), key=lambda x: sum(x) if sum(x) <= t else 0)
        if max_distance:
            return sum(max_distance) if sum(max_distance) <= t else None
    return None

if __name__ == "__main__":
    test_ls = [50, 55, 56, 57, 58]
    test_t = 163
    test_k = 3
    print(f"best is {choose_best_sum(test_t, test_k, test_ls)}")
