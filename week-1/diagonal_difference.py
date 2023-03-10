def diagonal_difference(arr):
    diagonal1 = 0
    diagonal2 = 0
    lenth_arr = len(arr)

    for number1 in arr:

        for number2 in arr:

            if number1 == number2:
                diagonal1 += arr[number1][number2]
    print(diagonal1)

    # if number1 == lenth_arr - number2 - 1:
    #     diagonal2 += arr[number1][number2]

#     return abs(diagonal1 - diagonal2)


if __name__ == "__main__":
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]

    assert diagonal_difference(arr) == 2
