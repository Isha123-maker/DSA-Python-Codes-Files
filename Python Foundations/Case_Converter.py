# In Python, a list comprehension is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition. Apart from being briefer, list comprehensions often run faster.

# Function to convert PascalCase or camelCase string into snake_case using a for loop
def convert_to_snake_case_using_for_loop(pascal_or_camel_cased_string):

    snake_cased_char_list = []   # Empty list to hold converted characters
    for char in pascal_or_camel_cased_string:   # Iterate over each character of the input string
        if char.isupper():   # If the character is uppercase
            converted_character = '_' + char.lower()   # Convert it to lowercase and prepend underscore
            snake_cased_char_list.append(converted_character)  # Add to the list
        else:
            snake_cased_char_list.append(char)  # Otherwise, add the character as it is
    
    # Join the list into a string
    snake_cased_string = ''.join(snake_cased_char_list)
    # Remove leading/trailing underscores
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string   # Return the final snake_case string

# Function to convert PascalCase or camelCase string into snake_case using list comprehension
def convert_to_snake_case_using_list(pascal_or_camel_cased_string):

    # Build a list: add '_' + lowercase if uppercase, else add character directly
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join into string and strip leading/trailing underscores
    return ''.join(snake_cased_char_list).strip('_')

# Main function to test both implementations
def main():
    # Test using list comprehension version
    print(convert_to_snake_case_using_list('aLongAndComplexString'))
    # Test using for loop version
    print(convert_to_snake_case_using_for_loop('ishaIsACoder'))

# Run the program
main()