def time_conversion(s):
    hour = s[0:2]
    min_sec = s[3:8]
    time_format = s[8:10]

    if time_format == "PM" and int(hour) != 12:
        hour = int(hour) + 12

    elif time_format == "AM" and int(hour) == 12:
        hour = "00"

    return "{}:{}".format(hour, min_sec)


if __name__ == '__main__':
    result = time_conversion("07:05:45PM")
