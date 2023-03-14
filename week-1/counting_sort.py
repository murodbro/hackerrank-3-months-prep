def counting_sort(arr):

    listed_numbers = [0] * (max(arr) + 1)

    for numbers in arr:

        listed_numbers[numbers] += 1

    return listed_numbers


if __name__ == '__main__':

    result = counting_sort([1, 1, 3, 2, 1])

    print(result)
