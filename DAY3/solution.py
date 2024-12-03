import re

# get input data
with open("input.txt", 'r', encoding='utf-8') as file:
    input = file.read()

### Part One ###

# create regex and find all occurrences
mul_pattern = r"mul\((\d+),(\d+)\)"
muls = re.findall(mul_pattern, input)

# calculate results
muls_results = [int(numbers[0]) * int(numbers[1]) for numbers in muls]

print(f"Answer: Sum of all multiplications results is {sum(muls_results)}.")

# ### Part Two ###

mul_enabled = True
enabled_sum = 0

# regex to match do(), and don't()
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

position = 0
while position < len(input):
    # find 'do()', 'don't()', or 'mul(...)' in the current part of input
    do_match = re.match(do_pattern, input[position:])
    dont_match = re.match(dont_pattern, input[position:])
    mul_match = re.match(mul_pattern, input[position:])
    
    if do_match:
        mul_enabled = True
        position += do_match.end()
    elif dont_match:
        mul_enabled = False
        position += dont_match.end()
    elif mul_match:
        num1 = int(mul_match.group(1))
        num2 = int(mul_match.group(2))
        
        if mul_enabled:
            enabled_sum += num1 * num2
        position += mul_match.end()
    # if no relevant pattern is found, just move forward by one character
    else:
        position += 1

print(f"Answer: Sum of enabled multiplications results is {enabled_sum}.")
