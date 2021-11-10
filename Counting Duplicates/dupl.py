def duplicate_count(text):
    text = text.lower()
    return len(set(x for x in text if text.count(x) > 1))

if __name__ == "__main__":
    test_text = 'Indivisibilities'
    print(f"the number of letter duplicates is {duplicate_count(test_text)}")
