def lonely_integer(a):

    number_element = {}
    only_one = []

    for number in a:
        if number in number_element:
            number_element[number] += 1
        else:
            number_element[number] = 1

    for key, value in number_element.items():
        if value == 1:
            only_one.append(key)

    for unique in only_one:
        return unique


if __name__ == '__main__':

    a = [1, 2, 3, 4, 3, 2, 1]

    result = lonely_integer(a)
