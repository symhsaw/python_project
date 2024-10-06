"""
Naming convention , snake_case , camelCase and PascalCase


def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    print (snake_cased_char_list)
    snake_cased_string = ''.join(snake_cased_char_list)
    print (snake_cased_string)

    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

snake_case = convert_to_snake_case("_isThisCard_")
print (snake_case)
"""
"""
A list comprehension in Python is a concise way to create lists. It allows you to generate a new list by applying
an expression to each element in an existing iterable (like a list, string, or range) in a single line of code.

Basic structure of list comprehension
[expression for item in iterable if condition]

"""


def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char  # this line is expression                         
        for char in pascal_or_camel_cased_string     # this line is for item in iterable  , (there is no if condition in this code)
    ]
    print(snake_cased_char_list)
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))
main()
