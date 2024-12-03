from common import read_input
import re

def handle_input():
    return ''.join(read_input('aoc2024_3')).replace('\n', '')

# part1
def solution_part1(input_str):
    total = 0
    matches = re.findall(r"mul\(\d+,\d+\)", input_str)
    for match in matches:
        numbers = re.findall(r"\d+", match)
        total += int(numbers[0]) * int(numbers[1])
    return total

# part2
def solution_part2(input_str):
    combined_pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))"
    matches = [m.group(0) if m.group(1) else 'do' if m.group(2) else 'dont'
               for m in re.finditer(combined_pattern, input_str)]

    ignore_next = False
    total = 0
    for match in matches:
        if match == 'do':
            ignore_next = False
        elif match == 'dont':
            ignore_next = True
        else:
            if ignore_next:
                continue
            numbers = re.findall(r"\d+", match)
            total += int(numbers[0]) * int(numbers[1])
    return total

def main():
    input = handle_input()
    return solution_part2(input)

if __name__ == "__main__":
    print(main())
