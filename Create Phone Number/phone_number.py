def create_phone_number(n):
    n = ''.join([str(x) for x in n])
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"

if __name__ == "__main__":
    test_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(f"number with mask = {create_phone_number(test_number)}")
