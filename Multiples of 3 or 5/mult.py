def solution(number):
    if number < 0:
        return 0
    else:
        return(sum([x for x in range(number) if x % 3 ==0 or x % 5 == 0]))

if __name__ == "__main__":
    test_number = 10
    print(f"result is {solution(test_number)}")
