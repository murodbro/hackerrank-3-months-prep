def diagonal_difference(arr):

    diagonal_left = 0
    diagonal_right = 0
    lenth = len(arr)

    for i in range(0, lenth):

        for j in range(0, lenth):

            if i == j:
                diagonal_left += arr[i][j]

            if (i + j) == (lenth - 1):
                diagonal_right += arr[i][j]

    return abs(diagonal_left - diagonal_right)


if __name__ == "__main__":
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]
