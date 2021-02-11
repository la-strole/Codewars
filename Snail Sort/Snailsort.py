def snail(snail_map):

    x_len = len(snail_map[0])
    y_len = len(snail_map)

    if not x_len:
        return []


    delta = 0
    current_position = [0, 0]
    result = []

    result.append(snail_map[current_position.copy()[1]][current_position.copy()[0]])

    while 1:

        exit = 1

        while x_len - current_position[0] - delta - 1 > 0:
            current_position[0] += 1
            result.append(snail_map[current_position.copy()[1]][current_position.copy()[0]])
            exit = 0

        exit = 1

        while y_len - current_position[1] - delta - 1 > 0:
            current_position[1] += 1
            result.append(snail_map[current_position.copy()[1]][current_position.copy()[0]])
            exit = 0

        exit = 1

        while current_position[0] > delta:
            current_position[0] -= 1
            result.append(snail_map[current_position.copy()[1]][current_position.copy()[0]])
            exit = 0

        delta += 1

        exit = 1

        while current_position[1] > delta:
            current_position[1] -= 1
            result.append(snail_map[current_position.copy()[1]][current_position.copy()[0]])
            exit = 0

        if exit == 1:
            break

    return result


matrix = [[]]

print(snail(matrix))
