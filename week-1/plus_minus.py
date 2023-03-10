def plus_minus(arr):
    cal_positive = 0
    cal_negative = 0
    cal_zero = 0

    for number in arr:
        if number > 0:
            cal_positive += 1
        elif number < 0:
            cal_negative += 1
        else:
            cal_zero += 1

    print("{:.6f}".format(cal_positive / len(arr)))
    print("{:.6f}".format(cal_negative / len(arr)))
    print("{:.6f}".format(cal_zero / len(arr)))


if __name__ == "__main__":
    plus_minus([1, 5, -6, 0, -8, 9])
