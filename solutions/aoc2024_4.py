from common import read_input

def handle_input(filename):
    input_matrix = [list(line.strip()) for line in read_input(filename)]
    return input_matrix

# part1
def is_target_sequence(x, y, dx, dy, matrix, target_sequence):
    sequence_positions = [(x, y)]
    for char in target_sequence:
        x = x + dx
        y = y + dy
        if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
            return False
        if matrix[x][y] != char:
            return False
        sequence_positions.append((x, y))

    return True

def count_sequences(matrix, target_sequence):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    occurrences = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 'X':
                occurrences += sum(
                    is_target_sequence(x, y, dx, dy, matrix, target_sequence)
                    for dx, dy in directions
                )
    return occurrences

def solution_part1():
    input_matrix = handle_input('aoc2024_4')
    target_sequence = ['M', 'A', 'S']
    return count_sequences(input_matrix, target_sequence)


# part2

def check_mas(matrix, vector_director, x, y):
    target_neighbours = [('M', 'S'), ('S', 'M')]
    first_neighbour = matrix[x+vector_director[0]][y+vector_director[1]]
    second_neighbour = matrix[x-vector_director[0]][y-vector_director[1]]
    return (first_neighbour, second_neighbour) in target_neighbours

def is_x_mas(x, y, matrix):
    if matrix[x][y] != 'A':
        return False
    diagonal_directions = [(1, 1), (1, -1)]

    for i in range(2):
        if not check_mas(matrix, diagonal_directions[i], x, y):
            return False
    return True

def solution_part2():
    input_matrix = handle_input('aoc2024_4')
    occurrences = 0
    for x in range(1, len(input_matrix)-1):
        for y in range(1, len(input_matrix[0])-1):
            if is_x_mas(x, y, input_matrix):
                occurrences += 1
    return occurrences

def main():
    print(solution_part2())

if __name__ == "__main__":
    main()
