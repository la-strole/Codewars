def generate_hashtag(s):
    return '#'+''.join(map(lambda x: x.capitalize(), (s.strip().split()))) if (s and len(s)+1<140) else False

if __name__ == "__main__":
    test_string = " Hello there thanks for trying my Kata"
    print(f"hashtag from string {test_string}\n{generate_hashtag(test_string)}")
