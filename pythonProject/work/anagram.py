def get_anagram(number):
    number_string = str(number)
    number_length = len(number_string)
    square_number = number * number
    square_number_string = str(square_number)
    check_count = square_number_string[-number_length:]

    if number_string == check_count:
        return  print("number is an anagram")
    else:
        return print("number is not an anagram")


get_anagram(5)
