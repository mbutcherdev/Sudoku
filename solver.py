# Copied over from my initial solver_text version
def solver(bd):
    print(bd)

    # Recursively solve the board, start as if it's full
    find = find_empty(bd)
    if not find:
        # Solution found
        return True
    else:
        row, col = find

    # Loop through 1 - 9 per box
    for idx in range(1, 10):
        # Add them into the board, if they're valid, add to the current position
        if valid_check(bd, idx, (row, col)):
            bd[row][col] = idx

            # Attempt to call solver again on the new board
            # This will either find solution or it'll return False
            # Backtrack element to 0 and retry loop
            if solver(bd):
                return True
            bd[row][col] = 0

    return False


def valid_check(bd, num, pos):
    # Check row
    for idx in range(len(bd[0])):
        # Enter a number, if the current position is that number, ignore it
        if bd[pos[0]][idx] == num and pos[1] != idx:
            return False

    # Check cols
    for idx in range(len(bd)):
        if bd[idx][pos[1]] == num and pos[0] != idx:
            return False

    # Check the 3x3 box we're in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for idx in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            # Check if it's equal, ignore current position
            if bd[idx][j] == num and (idx, j) != pos:
                return False

    # If nothing false, return True
    return True


def display_board(bd):

    print("-----------------------")
    for idx in range(len(bd)):
        if idx % 3 == 0 and idx != 0:
            print("-----------------------")

        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # If at last position, move to next line
            if j == 8:
                print(bd[idx][j])
            else:
                print(str(bd[idx][j]) + " ", end="")
    return "-----------------------"


def find_empty(bd):

    for idx in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[idx][j] == 0:

                # Return row and then col
                return (idx, j)

    # If no blank squares, return None or False
    return None
