def is_isogram(string):
    if len(set(string.lower())) == len(string):
        return True
    return False

if __name__ == "__main__":
    test_string = "Dermatoglyphics"
    print(f"{test_string} is isogram? {is_isogram(test_string)}")
