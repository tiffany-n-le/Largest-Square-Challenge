
# check all possible starting positions
# try every possible square size from that square 
# checking if all those squares are equal

# solving: given a N x N grid of nums, find the largest square
# where every num in the square is the same
def largest_square(grid):
    n = len(grid) # n (size of grid)
    largest = 0 # largest (largest sq size so far)
    best_pos = None # best_pos (where sq starts)
    best_val = None # best_val (num inside)

    for row in range(n): # for each row
        for col in range(n): # for each col

            # start in top left and save its val
            val = grid[row][col] 

            # max possible square size from this pos
            max_poss_size = min(n - row, n - col)

            # try increasing sq sizes
            for size in range(1, max_poss_size + 1):
                valid_sq = True
                
                # make sure square fits inside grid
                # check every cell in square
                for r in range(row, row + size):
                    for c in range(col, col + size):
                        # if cell not same num, not valid
                        if grid[r][c] != val: 
                            valid_sq = False
                            break
                    if not valid_sq:
                        break
                # if all cells equal the top left val
                if valid_sq:
                    # update largest if this sq is bigger
                    if size > largest:
                        largest = size
                        best_val = val
                        best_pos = (row, col)
                else:
                    # stop checking larger squares in the pos
                    break
    # return largest sq size so far, val inside, and position
    return largest, best_val, best_pos 

    
# test cases
# expected output: (1, 5, (0, 0))
print(largest_square([[5]])) # smallest possible grid

# expected output: (2, 2, (0, 0))
print(largest_square([ # all nums the same
    [2, 2],
    [2, 2]
]))

# expected output: (1, 1, (0, 0))
print(largest_square([
    [1, 2], # no 2x2 square exits
    [3, 4]
]))

# expected output: (3, 2, (0, 1))
print(largest_square([
    [1, 2, 2, 2, 3], # 3x3 square of 2's inside
    [4, 2, 2, 2, 5],
    [6, 2, 2, 2, 7],
    [8, 9, 9, 9, 0],
    [1, 1, 1, 1, 1]
]))


