def balanced_number(number: int):
    """
    return if number is balanced (look at Balanced Number.txt)
    :param number: positive integer
    :return: "Balanced" or "Not Balanced"
    """

    def recursive_function(sequence, right_hand=0, left_hand=0):
        """
        Returns if number is balanced
        :param sequence: list of digits (int)
        :param right_hand: sum of digits from the right from the middle
        :param left_hand: sum of digits from the left of the middle
        :return: "Balanced" or "Non Balanced"
        """
        # base case of recursion
        if len(sequence) == 1 or len(sequence) == 2:
            if left_hand == right_hand:
                return "Balanced"
            else:
                return "Not Balanced"
        else:
            left_hand += sequence[0]
            right_hand += sequence[-1]
            return recursive_function(sequence[1:-1], right_hand, left_hand)

    digit_sequence = [int(_) for _ in str(number)]
    return recursive_function(digit_sequence)