from collections import defaultdict
from common import read_input

# common
def handle_input():
    split_input = [x.split() for x in read_input('aoc2024_1.txt')]
    return [int(x[0]) for x in split_input], [int(x[1]) for x in split_input]
# part1
def compute_list_distance(list1, list2):
    return [abs(x - y) for x, y in zip(list1, list2)]

def solution_part1():
    list1, list2 = handle_input()
    list1.sort()
    list2.sort()
    return sum(compute_list_distance(list1, list2))

# part2
def solution_part2():
    list1, list2 = handle_input()
    occurrence_2 = defaultdict(int)
    for number in list2:
        occurrence_2[number] += 1

    sum_occurrences = 0
    for number in list1:
        occurrence = occurrence_2.get(number, 0)
        if occurrence:
            sum_occurrences += occurrence*number
    return sum_occurrences

def main():
    return solution_part2()

if __name__ == "__main__":
    print(main())
