def disemvowel_trolls(sentence: str) -> str:
    """
    Get string and remove from it all vowels
    :param sentence: string: str
    :return: string without vowels
    """
    assert isinstance(sentence, str)
    vowels = "aeiouAEIOU"

    return ''.join([_ for _ in sentence if _ not in vowels])


if __name__ == '__main__':
    print(disemvowel_trolls('test string'))
