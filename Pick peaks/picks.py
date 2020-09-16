def pick_peaks(arr):
    i = 1
    answer = {'pos': [], 'peaks': []}
    while i < len(arr)-1:
        print(f'i= {i}, arr={arr[i]}')
        if arr[i-1] < arr[i] > arr[i+1]:
            print('result here')
            answer['pos'].append(i)
            answer['peaks'].append((arr[i]))
        if arr[i-1] < arr[i] == arr[i+1]: # here is plateau
            print(f'here is plateau, start at {arr[i]}')
            for z in range(i, len(arr)-1):
                if arr[z+1] > arr[z]:
                    i = z
                    break
                elif arr[z+1] < arr[z]:
                    print('plateau result here')
                    answer['pos'].append(i)
                    answer['peaks'].append((arr[i]))
                    i = z
                    break
        i += 1
    return answer


print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))


