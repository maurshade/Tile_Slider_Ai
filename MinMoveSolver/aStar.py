import random
from typing import List
import heapq



# Define the goal state of the puzzle
GOAL = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Define the possible moves for the blank space
MOVES = {'left': [-1, 0], 'right': [1, 0], 'up': [0, -1], 'down': [0, 1]}

itCnt = 0

# Define the heuristic function for A*
def heuristic(state: List[int]) -> int:
    global itCnt
    # print("Entering heuristic")
    h = 0
    for i in range(len(state)):
        if state[i] != GOAL[i]:
            h += 1
    # print("Leaving heuristic")
    itCnt += 1
   # if itCnt % 100000 == 0:
        #print(round(itCnt / 1000000), " Million times leaving the heuristic function")
    return h

# Define the A* search algorithm
def astar(start: List[int]) -> int:
    global itCnt
    heap = []
    heapq.heappush(heap, (heuristic(start), 0, start))
    visited = set()

    while heap:
        h, g, state = heapq.heappop(heap)

        if state == GOAL:
            print("Num of iterations: ", itCnt)
            return g
        visited.add(frozenset(state))

        blank_pos = state.index(0)
        blank_x = blank_pos % 3
        blank_y = blank_pos // 3

        for move, (dx, dy) in MOVES.items():
            x = blank_x + dx
            y = blank_y + dy
            if itCnt == 1000000:
                return None
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = state[:]
                new_blank_pos = y * 3 + x
                new_state[blank_pos], new_state[new_blank_pos] = new_state[
                    new_blank_pos], new_state[blank_pos]
                f = g + 1 + heuristic(new_state)
                heapq.heappush(heap, (f, g + 1, new_state))
    print("Leaving A*")
    return None

def is_unsolvable(puzzle: List[int]) -> bool:
    """
    Check if a sliding puzzle is unsolvable
    :param puzzle: The current configuration of the puzzle
    :return: True if the puzzle is unsolvable, False otherwise
    """
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i+1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    blank_pos = puzzle.index(0)
    blank_row = blank_pos // 3
    if blank_row % 2 == 0:
        return inversions % 2 != 0
    else:
        return inversions % 2 == 0

# Create a random configuration of the puzzle
solved = 0
moves = []
unsolved = 0
unsolvable = 0
for i in range(100):
    print("Start Program")
    start = GOAL.copy()
    random.shuffle(start)
    print("Random configuration:", start)
    if is_unsolvable(start) == True:
        print("Unsolveable\n")
        unsolvable += 1
    else:
        # Use the A* search algorithm to find the solution
        solution = astar(start)

        # Print the result
        if solution is not None:
            print("Minimum number of moves to solve the puzzle:", solution)
            moves.append(solution)
            solved +=1
        else:
            print("No solution was found.")
            unsolved +=1

        print("End Program\n")
        itCnt = 0
print("******************************************")
print("Solved: ", solved)
print("Unsolved: ", unsolved)
print("Unsolveable ", unsolvable)
print("Min Number of moves for each run", moves)
print("Move avg: ", (sum(moves) / len(moves)))
print("******************************************")


