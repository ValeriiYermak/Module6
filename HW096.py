def is_equal_string(utf8_string, utf16_string):
    value = utf8_string.decode('utf-8').casefold() == utf16_string.decode('utf-16').casefold()
    return value