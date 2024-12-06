from collections import defaultdict

from common import read_input

def handle_input():
    return [line.replace('\n', '') for line in read_input('aoc2024_5')]

def check_line1(line, priorities):
    for i in range(len(line)-1, -1, -1):
        if not set(line[:i]).isdisjoint(priorities[line[i]]):
            return False
    return True

def check_line2(line, priorities):
    swapped = False
    i = len(line) - 1
    while i > 0:
        for j in range(i):
            if line[j] in priorities[line[i]]:
                swapped = True
                line[i], line[j] = line[j], line[i]
                i = len(line)
                break
        i -= 1
    return swapped

def compute_sum(lines, checker):
    priorities = defaultdict(set)

    sum_middle = 0
    is_priority = True
    for line in lines:
        if line == '':
            is_priority = False
            continue
        if is_priority:
            key, value_to_add = line.split('|')
            priorities[key].add(value_to_add)
        else:
            line = [n for n in line.split(',')]
            if checker(line, priorities):
                sum_middle += int(line[len(line)//2])
    return sum_middle

def main():
    lines = handle_input()
    return compute_sum(lines, check_line2)

if __name__ == "__main__":
    print(main())
