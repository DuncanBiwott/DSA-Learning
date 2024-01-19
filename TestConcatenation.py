import re

def process_list(input_list):
    result_list = []
    current_concatenation = ""

    for element in input_list:
        match = re.match(r'\d+\.\d+', element)

        if match:
            # Concatenate previous elements and add to result_list
            result_list.append(current_concatenation)
            # Reset current_concatenation for the next sequence
            current_concatenation = ""

        # Append the current element to the current_concatenation
        current_concatenation += element

    # Add the last concatenation (if any) to the result_list
    result_list.append(current_concatenation)

    return result_list

# Example usage:
input_list = ["1.2", "a", "b", "3.4", "c", "d", "5.6"]
result = process_list(input_list)
print(result)

my_list = [1,2]
new_list = my_list*2
print(new_list)