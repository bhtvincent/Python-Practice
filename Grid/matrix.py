# ----------------------------------------------------------------------
# Name:        matrix
# Purpose:     Implement matrix manipulation functions
#
# Date:        2/12/2019
# ----------------------------------------------------------------------
"""
Matrix manipulation functions.

1. Count the number of times a target appears in a matrix.
2. Gets adjacent coordinates given coordinate.
3. Blurs an image.
"""

def count_matrix(matrix, target):
    """
    Counts the number of times target appears in matrix
    :param matrix: (list) list of lists of numbers
    :param target: (number) the number to count occurrences
    :return: (number) the number of occurrences of the target
    """
    count = 0
    for row in range(len(matrix)):
        count += matrix[row].count(target)
    return count

def adjacent(matrix, target):
    """
    Returns the adjacent coordinates of the target in the matrix
    :param matrix: (matrix) list of list of numbers
    :param target: (tuple) the target to get adjacent coordinates
    :return: (set) the set of adjacent coordinates
    """
    x = target[0]
    y = target[1]
    total = {(x+x_index, y+y_index) for x_index in range(-1, 2)
             if len(matrix) > x+x_index > -1 for y_index in range(-1, 2)
             if len(matrix[0]) > y+y_index > -1}
    if target in total:
        total.remove(target)
    return total or None

def blur(matrix):
    """
    Blurs an image given lists of pixel colors
    :param matrix: (list) List of lists representing image to be blurred
    :return: (list) List of lists representing blurred image
    """
    returned = []
    for x in range(0, len(matrix)):
        row = []
        for y in range(0, len(matrix[0])):
            total = matrix[x][y]
            number_of_elements = 1
            for adjacent_coord in adjacent(matrix, (x, y)):
                total = total + \
                        matrix[adjacent_coord[0]][adjacent_coord[1]]
                number_of_elements += 1
            row.append(round(total/number_of_elements))
        returned.append(row)
    return returned

def main():
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86, 72, 72, 95, 129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80, 57, 79, 57, 29, 23],
             [29, 34, 19, 28, 38, 39, 15, 26],
             [14, 21, 18, 21, 21, 18, 24, 25]]
    grid = [[1, 2, 0],
            [4, 0, 5],
            [7, 3, 9],
            [0, 0, 0]]

    print("Test1(count_matrix):")
    print(count_matrix(grid, 6))
    print(count_matrix(grid, 0))
    print(count_matrix(grid, 4))
    print(count_matrix(grid, 9))
    print(count_matrix([[]], 4))
    print(count_matrix([], 4))

    print("\nTest2(adjacent function):")
    print(adjacent(grid, (0, 0)))
    print(adjacent(grid, (2, 1)))
    print(adjacent(grid, (3, 1)))
    print(adjacent(grid, (8, 9)))
    print(adjacent([], (0, 0)))

    print("\nTest3(blur function):")
    print(blur(image))

if __name__ == "__main__":
    main()
