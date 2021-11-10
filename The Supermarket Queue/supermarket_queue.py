def queue_time(customers, n):
    result = [[] for x in range(n)]
    for item in customers:
        result.sort(key=sum)
        result[0].append(item)
    result.sort(key=sum)    
    return sum(result[-1])

if __name__ == "__main__":
    test_customers = [10,2,3,3]
    test_n = 2
    print(f"total time is {queue_time(test_customers, test_n)}")
