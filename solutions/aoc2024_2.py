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

def treat_report_with_one_removal_authorized(report, is_removal_allowed=True):
    """
    Treats a report and returns true if is safe, false otherwise. If is_removal_allowed is True, it will try to remove
    one element from the report and check if the report is safe (recursion).
    If it is, it will return True, otherwise False.
    :param report: list of integers
    :param is_removal_allowed: boolean used to break the recursion
    :return: True if report is safe or if one element can be removed to make it safe, False otherwise
    """
    def remove_ith_el(lst, i):
        return lst[:i] + lst[i+1:]
    prev_diff = 0
    for i in range(len(report) - 1):
        curr_diff = report[i + 1] - report[i]

        case_0 = curr_diff * prev_diff < 0 and not abs(curr_diff) > 3
        case_1 = abs(curr_diff) > 3 and not curr_diff * prev_diff < 0
        case_2 = abs(curr_diff) < 1 # means the difference is 0
        if case_0:
            if is_removal_allowed:
                # if we exclude the very two first nodes case we allways want to remove the element at which the
                # monotony is broken (i.e. i+1th element)
                if i==1:
                    # check also that if removal of first element works (i.e. the first element is the one to remove)
                    return treat_report_with_one_removal_authorized(remove_ith_el(report, 0),
                                                                    False) or treat_report_with_one_removal_authorized(
                        remove_ith_el(report, 2), False)
                return treat_report_with_one_removal_authorized(remove_ith_el(report, i + 1), False)
            return False

        if case_1 or case_2:
            # try to remove the ith + 1 element
            if not is_removal_allowed:
                return False
            return treat_report_with_one_removal_authorized(remove_ith_el(report, i + 1), False)
        prev_diff = curr_diff
    return True

def count_safe_reports(reports, safety_checker):
    return sum(safety_checker(report) for report in reports)

def solution_part1(reports):
    return count_safe_reports(reports, treat_report)

def solution_part2(reports):
    return count_safe_reports(reports, treat_report_with_one_removal_authorized)

def main():
    return solution_part2(handle_input())

if __name__ == "__main__":
    print(main())
