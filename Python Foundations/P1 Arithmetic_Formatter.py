def arithmetic_arranger(problems, show_answers=False):
    # Limit check
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for expr in problems:
        expr = expr.strip()

        # Identify operator
        if "+" in expr:
            left_operand, right_operand = [x.strip() for x in expr.split("+")]
            operator = "+"
        elif "-" in expr:
            left_operand, right_operand = [x.strip() for x in expr.split("-")]
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        # Check digits
        if not left_operand.isdigit() or not right_operand.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Check operand size
        if len(left_operand) > 4 or len(right_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Width for alignment
        width = max(len(left_operand), len(right_operand)) + 2

        # Format lines
        top = left_operand.rjust(width)
        bottom = operator + right_operand.rjust(width - 1)
        line = "-" * width

        # Calculate result if needed
        if operator == "+":
            result = str(int(left_operand) + int(right_operand))
        else:
            result = str(int(left_operand) - int(right_operand))
        res = result.rjust(width)

        # Collect
        first_line.append(top)
        second_line.append(bottom)
        dashes.append(line)
        results.append(res)

    # Combine
    arranged = "    ".join(first_line) + "\n" + \
               "    ".join(second_line) + "\n" + \
               "    ".join(dashes)

    if show_answers:
        arranged += "\n" + "    ".join(results)

    return arranged


# Example usage
print(f'\n{arithmetic_arranger(["44 + 8155", "909 - 2", "45 + 43", "123 + 49"])}')
