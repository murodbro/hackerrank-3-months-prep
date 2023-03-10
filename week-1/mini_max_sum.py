def mini_max_sum(arr):
    calculate_number = 0

    for number in arr:
        calculate_number += number
        calculate_max = calculate_number - min(arr)
        calculate_min = calculate_number - max(arr)

    print(calculate_min, calculate_max)


if __name__ == '__main__':
    mini_max_sum([1, 2, 5, 0, 3, 6])
