from common import read_input

def handle_input():
    return [list(map(int,(x.split()))) for x in read_input('aoc2024_2')]

# part1
def treat_report(report):
    # treats a report and returns true if is safe, false otherwise
    prev_diff = 0
    for i in range(len(report)-1):
        curr_diff = report[i] - report[i+1]
        if abs(curr_diff) > 3 or abs(curr_diff) < 1 or curr_diff * prev_diff < 0:
            return False
        prev_diff = curr_diff
    return True


def solution_part1(reports):
    safe_reports_count = 0
    for report in reports:
        if treat_report(report):
            safe_reports_count += 1
    return safe_reports_count

def main():
    return solution_part1(handle_input())

if __name__ == "__main__":
    print(main())
