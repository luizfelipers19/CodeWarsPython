
# def get_first_value_decimal_size(value):
#     stringValue = str(value)
#     separator_position = stringValue.find(".")
#     if separator_position != None:
#         separator_position += 1
#         return len(stringValue[separator_position : ]) -1
#
# def approx_equals(a, b):
#     size = get_first_value_decimal_size(a)
#     a = round(a, size)
#     b = round(b, size)
#     return a == b
#

def get_value_decimal_size(value):
    stringValue = str(value)
    separator_position = stringValue.find(".")
    if separator_position != None:
        separator_position += 1
        return len(stringValue[separator_position:])


def approx_equals(a, b):
    size_a = get_value_decimal_size(a)
    size_b = get_value_decimal_size(b)
    if size_a == size_b:
        size = size_a - 1
        a = round(a, size)
        b = round(b, size)
        return a == b
    else:
        size = size_a
        a = round(a, size)
        b = round(b, size)
        return a == b


# def main():
#     test = approx_equals(-156.24037, -156.24038)
#     print(test)

if __name__ == "__main__":
    # main()
    test = approx_equals(123.2345, 123.234501)
    print(test)


