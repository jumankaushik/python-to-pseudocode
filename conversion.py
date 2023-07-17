def convert_python_to_pseudocode(input_file, output_file):
    with open(input_file, 'r') as f:
        python_code = f.readlines()

    pseudocode = []
    step_number = 1

    conversions = {
        'def': 'Function',
        'if': 'If',
        'else': 'Else',
        'elif': 'Else If',
        'while': 'While',
        'for': 'For',
        'print': 'Print',
        '=': 'Equal to',
        '+': 'Plus',
        '-': 'Minus',
        '*': 'Multiplied by',
        '/': 'Divided by',
        '%': 'Modulo',
        '<': 'Less than',
        '<=': 'Less than or equal to',
        '>': 'Greater than',
        '>=': 'Greater than or equal to',
        '==': 'Equals',
        '!=': 'Not equals',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'True': 'True',
        'False': 'False',
        'None': 'None',
        '(': '',
        ')': '',
        ':': '',
        ',': '',
        '#': 'Step {}'.format(step_number),
        '\n': '\n'
    }

    for line in python_code:
        line = line.strip()

        if line.startswith('#'):
            # Comment line
            pseudocode.append(line)
        elif line:
            # Non-empty line
            # Check for conversions
            converted_line = ''
            words = line.split()
            for word in words:
                converted_word = conversions.get(word, word)
                converted_line += converted_word + ' '

            # Increment the step number for each line
            converted_line = 'Step {}: '.format(step_number) + converted_line.strip()

            pseudocode.append(converted_line)
            step_number += 1

    with open(output_file, 'w') as f:
        f.write('\n'.join(pseudocode))

    print("Conversion complete. Pseudocode written to", output_file)

# Usage example
input_file = 'input.py'
output_file = 'output.txt'
convert_python_to_pseudocode(input_file, output_file)
