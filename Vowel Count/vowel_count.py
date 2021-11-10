def get_count(input_str):
    num_vowels = 0
    num_vowels = len([x for x in input_str if x in 'aeiou'])
    
    return num_vowels

if __name__ == "__main__":
    test_string = "test"
    print(f"vowels count in string {test_string} is {get_count(test_string)}")
