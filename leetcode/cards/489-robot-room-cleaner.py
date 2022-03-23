"""
Robot Room Cleaner

You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n
binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not
have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the
room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is
90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays
on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Note that the initial direction of the robot will be facing up. You can assume all four edges of
the grid are all surrounded by a wall.

Custom testing:
  The input is only given to initialize the room and the robot's position internally. You must
  solve this problem "blindfolded". In other words, you must control the robot using only the four
  mentioned APIs without knowing the room layout and the initial robot's position.
[I guess `inspect.getsource()` is cheating. Oh well.]

Now trying to figure out how to get the code to LinkNode for the uber frustrating prob 19.

`inspect.getsource()` isn't working

import inspect
def get_caller():
    return inspect.stack()[2]   # 1 is get_caller's caller
def trace_call():
    _, filename, line, function, _, _ = get_caller()
    print("Called by %r at %r:%d" % (function, filename, line))
def main():
    trace_call()

https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2794/

"""
from collections import deque
from typing import *

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# ##  Backtracking Template
#     def backtrack(candidate):
#         if find_solution(candidate):
#             output(candidate)
#             return

#         # iterate all possible candidates.
#         for next_candidate in list_of_candidates:
#             if is_valid(next_candidate):
#                 # try this partial candidate solution
#                 place(next_candidate)
#                 # given the candidate, explore further.
#                 backtrack(next_candidate)
#                 # backtrack
#                 remove(next_candidate)

def print_grid(grid):
    rows = []
    for row in grid:
        rows.append("".join(f" {c} " for c in row))
    print("\n".join(rows))


class Robot:

    # ['clean', 'col', 'direction', 'dmap', 'move', 'needClean', 'room', 'row', 'turnLeft', 'turnRight']
    def __init__(self, vec2d, r, c):
        self.move_number = 0
        self.room = vec2d
        self.row = r
        self.col = c
        self.direction = 0
        self.needClean = 0
        self.dmap = [[-1,0],[0,1],[1,0],[0,-1]]  # s, e, n, w  --or-- n, e, s, w??
        self.duni = ['↑', '→', '↓', '←']
        for i in range(len(self.room)):
            for j in range(len(self.room[0])):
                if self.room[i][j] == 1:
                    self.needClean += 1

    def clean(self):
        if self.room[self.row][self.col] == 1:
            self.room[self.row][self.col] = 2
            self.needClean -= 1

    def turnLeft(self):
        self.move_number += 1
        newd = (self.direction + 3) % 4
        self.direction = newd
        print(f"{self.move_number}: ({self.row},{self.col},{self.duni[self.direction]})")

    def turnRight(self):
        self.move_number += 1
        newd = (self.direction + 1) % 4
        self.direction = newd
        print(f"{self.move_number}: ({self.row},{self.col},{self.duni[self.direction]})")

    def move(self):
        if self.move_number > 100:
            print_grid(self.room)
            raise
        self.move_number += 1
        r = self.row + self.dmap[self.direction][0]
        c = self.col + self.dmap[self.direction][1]
        if r < 0 or c < 0 or r >= len(self.room) or c >= len(self.room[0]) or self.room[r][c] == 0:
            print(f"{self.move_number}: ({self.row},{self.col},{self.duni[self.direction]})")
            return False
        self.row = r
        self.col = c
        print(f"{self.move_number}: ({self.row},{self.col},{self.duni[self.direction]})")
        return True


# ## shortened template
# def backtrack(candidate):
#     if find_solution(candidate):
#         output(candidate)
#         return
#     for next_candidate in list_of_candidates:
#         if is_valid(next_candidate):
#             place(next_candidate)
#             backtrack(next_candidate)
#             remove(next_candidate)

# ## Sudoku Backtracking
#     def place_next_numbers(row, col):
#         """
#         Call backtrack function in recursion
#         to continue to place numbers
#         till the moment we have a solution
#         """
#         # if we're in the last cell
#         # that means we have the solution
#         if col == N - 1 and row == N - 1:
#             nonlocal sudoku_solved
#             sudoku_solved = True
#         # if not yet
#         else:
#             # if we're in the end of the row
#             # go to the next row
#             if col == N - 1:
#                 backtrack(row + 1, 0)
#             # go to the next column
#             else:
#                 backtrack(row, col + 1)
#
#     def backtrack(row=0, col=0):
#         """
#         Backtracking
#         """
#         # if the cell is empty
#         if board[row][col] == '.':
#             # iterate over all numbers from 1 to 9
#             for d in range(1, 10):
#                 if could_place(d, row, col):
#                     place_number(d, row, col)
#                     place_next_numbers(row, col)
#                     # if sudoku is solved, there is no need to backtrack
#                     # since the single unique solution is promised
#                     if not sudoku_solved:
#                         remove_number(d, row, col)
#         else:
#             place_next_numbers(row, col)


direction_order = {
    'n': ((0, 1), (1, 0), (0, -1), (-1, 0)),
    'e': ((1, 0), (0, -1), (-1, 0), (0, 1)),
    's': ((0, -1), (-1, 0), (0, 1), (1, 0)),
    'w': ((-1, 0), (0, 1), (1, 0), (0, -1)),
}
direction = {
    (0, 1): 'n',
    (1, 0): 'e',
    (0, -1): 's',
    (-1, 0): 'w',

}
rotate_one_right = {('n', 'e'), ('e', 's'), ('s', 'w'), ('w', 'n')}
rotate_one_left = {('n', 'w'), ('w', 's'), ('s', 'e'), ('e', 'n')}
rotate_two = {('n', 's'), ('s', 'n'), ('e', 'w'), ('w', 'e')}


class Solution:

    def cleanRoom(self, robot):
        is_blocked = set()
        is_cleaned = set()

        def do_rotation(d_start, d_end):
            if (d_start, d_end) in rotate_one_right:
                robot.turnRight()
            elif (d_start, d_end) in rotate_one_left:
                robot.turnLeft()
            elif (d_start, d_end) in rotate_two:
                robot.turnRight()
                robot.turnRight()
            else:
                if d_start != d_end:
                    raise
            return d_end

        def attempt_move_to(xy, path, dp):
            xp, yp = path[-1]
            delta = xy[0] - xp, xy[1] - yp
            d = direction[delta]
            dnew = do_rotation(dp, d)
            assert dnew == d
            return d, robot.move()

        def get_next_possible_moves(xy, path, d):
            (x, y), deltas = xy, direction_order[d]
            points = (
                (x+dx, y+dy) for dx, dy in deltas
            )
            points = (
                xyp for xyp in points
                if xyp not in is_blocked
                and xyp not in is_cleaned
            )
            points = tuple(points)
            if not points:
                raise
            return points[0]
            # for xp, yp in points:
            #     yield xp, yp

            # for dx, dy in deltas:
            #     xp, yp = xy[0] + dx, xy[1] + dy
            #     if (xp, yp) in is_blocked:
            #         continue
            #     if (xp, yp) in is_cleaned:
            #         # this should only be a soft block
            #         continue
            #     yield (xp, yp)  # going to need to pass direction too probably
            # also, here, need to create a map of the walls, and then know where the uncleaned places are

        def backtrack(xy, path, d):
            # ## TODO: if has_nowhere_else_to_go()
            # if has_moved((x,y), path):  # has_moved
            #     robot.clean()  # clean
            #     is_cleaned.add((x,y))
            #     # don't return because we can keep going -- I think
            # else:
            #     is_blocked.add((x,y))
            #     return

            # xyp = get_next_attempt(xy, path, d)
            # dp, did_move = attempt_move_to(xyp, path, d)
            # if did_move:  # try move
            #     robot.clean()
            #     is_cleaned.add(xyp)
            #     path.append(xyp)
            #     backtrack(xyp, path, d)
            #     path.pop()
            # else:
            #     is_blocked.add(xyp)

            for xyp in get_next_possible_moves(xy, path, d):
                # after going deep into the backtracking, maybe these possible moves aren't
                # even valid anymore
                # need to verify
                dp, did_move = attempt_move_to(xyp, path, d)
                if did_move:  # try move
                    robot.clean()
                    is_cleaned.add(xyp)
                    path.append(xyp)
                    backtrack(xyp, path, d)
                    path.pop()
                else:
                    is_blocked.add(xyp)

        path = deque()
        path.append((0, 0))
        backtrack((0, 0), path, 'n')



CASES = (
    # ## expected, *input_args
    (0, [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], 1, 3),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        robot = Robot(*input_args)
        Solution().cleanRoom(robot)

        result = robot.needClean
        if result == expected:
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            print(f"  {expected} != {result}")
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")
test()
