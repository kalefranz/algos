from collections import deque
from typing import *
from time import perf_counter

def timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

class Path:
    deltas = {
        (-1,0): 'up',
        (0,1): 'right',
        (1,0): 'down',
        (0,-1): 'left',
    }
    end_coord = None
    max_busted = -1
    blocked = None
    _grid = None

    def direction_vector(self):
        nodes = list(self._jumbled_coords)
        vec = {
            nodes[0]: "first",
        }
        vec.update(
            (nodes[q], self.deltas[nodes[q][0]-nodes[q-1][0], nodes[q][1]-nodes[q-1][1]])
            for q in range(1, len(nodes))
        )
        return vec

    @classmethod
    def set_grid(cls, grid, max_busted):
        cls._grid = grid
        num_rows = len(grid)
        num_cols = len(grid[0])
        cls.end_coord = num_rows-1, num_cols-1
        cls.max_busted = max_busted
        cls.blocked = frozenset(
            (i,j) for i in range(num_rows) for j in range(num_cols) if grid[i][j] == 1
        )
        return cls

    def __init__(self, *coords, from_instance=None):
        # self._jumbled_coords = set()
        self._jumbled_coords = {}
        self.last_coord = None
        self._num_nodes = 0
        if from_instance:
            # self._jumbled_coords |= from_instance._jumbled_coords
            self._jumbled_coords.update(from_instance._jumbled_coords)
            self.last_coord = from_instance.last_coord
            self._num_nodes = from_instance._num_nodes

        if len(coords) == 2 and coords[0].isdigit():
            coords = coords,
        for coord in coords:
            self._add(coord)

    def _dump_coords(self):
        return str(list(self._jumbled_coords)).replace(' ', '')

    def _add(self, coord):
        # self._jumbled_coords.add(coord)
        self._jumbled_coords[coord] = self._num_nodes
        self._num_nodes += 1
        self.last_coord = coord
        return self

    def new_with(self, *coords):
        p = self.__class__(*coords, from_instance=self)
        return p

    @property
    def num_steps(self):
        return self._num_nodes - 1

    @property
    def break_coords(self):
        return list(self._jumbled_coords.keys() & self.blocked)

    def is_busted_with(self, coord):
        # total = len(self._jumbled_coords & self.blocked)
        total = len(self._jumbled_coords.keys() & self.blocked)
        total += coord in self.blocked
        return total > self.max_busted

    @property
    def is_busted(self):
        return self.is_busted_with((-1,-1))

    @property
    def is_end(self):
        return self.last_coord == self.end_coord

    def can_move(self, *delta):
        lc = self.last_coord
        coord = lc[0]+delta[0], lc[1]+delta[1]
        if (
            0 <= coord[0] <= self.end_coord[0]
        ) and (
            0 <= coord[1] <= self.end_coord[1]
        ) and (
            coord not in self._jumbled_coords
        ) and (
            not self.is_busted_with(coord)
        ):
            return coord
        else:
            return False

    def next_paths(self):
        paths = (
            self.new_with(coord) for delta in self.deltas if (coord := self.can_move(*delta))
        )
        return paths

    def __str__(self):
        return f"P<{self._num_nodes}:{self.last_coord}>"

    def __repr__(self):
        return str(self)

    @staticmethod
    def grid_to_str(grid, cell_padding=0):
        max_node_width = max(max(map(len, row)) for row in grid)
        w = max_node_width + 2 * cell_padding
        result = '\n'.join(
            ''.join(f"{val:^{w}}" for val in row)
            for row in grid
        )
        print(result)
        return result

    def print_grid_1(self):
        # is_sorted(list(self._jumbled_coords.values()))
        # print(self._jumbled_coords)
        grid = self._grid
        row_builder = []
        for r in range(len(grid)):
            col_builder = []
            for c in range(len(grid[0])):
                start_val = grid[r][c]
                coord = (r, c)
                col_builder.append(coord)
            row_builder.append(''.join("%3s,%-3s" % c for c in col_builder))
            col_builder = []
        print('\n'.join(row_builder))

    def print_grid(self):
        # translate = {0: ' ', 1: ' '}
        # translate = {0: ' · ', 1: '███'}
        translate = {0: ' · ', 1: '⣿⣿⣿'}

        grid = self._grid
        grid2 = [
            [translate[val] for val in row]
            for row in grid
        ]
        # self.grid_to_str(grid2)


        # translate = {"up": 'u', "right": 'r', "down": 'd', "left": 'l', None: '+'}
        translate = {
            "ll": '───',
            "rr": '───',
            "uu": ' │ ',
            "dd": ' │ ',
            "ur": ' ┌─',
            "ld": ' ┌─',
            "rd": '─┐ ',
            "ul": '─┐ ',
            "dl": '─┘ ',
            "ru": '─┘ ',
            "lu": ' └─',
            "dr": ' └─',
            "fr": '───',
            "fd": ' │ ',
            # "fr": '☞',  # ╘╞
            # "fd": '☟',   # ╖╥
        }
        # translate = {
        #     "ll": '━━━',
        #     "rr": '━━━',
        #     "uu": ' ┃ ',
        #     "dd": ' ┃ ',
        #     "ur": ' ┏━',
        #     "ld": ' ┏━',
        #     "rd": '━┓ ',
        #     "ul": '━┓ ',
        #     "dl": '━┛ ',
        #     "ru": '━┛ ',
        #     "lu": ' ┗━',
        #     "dr": ' ┗━',
        #     "fr": '━━━',
        #     "fd": ' ┃ ',
        #     # "fr": '☞',  # ╘╞
        #     # "fd": '☟',   # ╖╥
        # }
        # translate = {
        #     "ll": '═══',
        #     "rr": '═══',
        #     "uu": ' ║ ',
        #     "dd": ' ║ ',
        #     "ur": ' ╔═',
        #     "ld": ' ╔═',
        #     "rd": '═╗ ',
        #     "ul": '═╗ ',
        #     "dl": '═╝ ',
        #     "ru": '═╝ ',
        #     "lu": ' ╚═',
        #     "dr": ' ╚═',
        #     "fr": '═══',
        #     "fd": ' ║ ',
        #     # "fr": '☞',  # ╘╞
        #     # "fd": '☟',   # ╖╥
        # }
        vec = list(self.direction_vector().items())
        for q in range(1,len(vec)):
            # ((r, c), dd)
            coord_p, dd_p = vec[q-1]
            coord, dd = vec[q]
            key = dd_p[0] + dd[0]
            r, c = coord_p
            grid2[r][c] = translate[key]

        for (r,c) in self.break_coords:
            grid2[r][c] = ' 💣 '

        self.grid_to_str(grid2)

        # for r in range(len(grid)):
        #     col_builder = []
        #     for c in range(len(grid[0])):
        #         orig_val = grid[r][c]
        #         coord = (r, c)
        #         col_builder.append(translate[orig_val])
        #     grid2.append(col_builder)
        #     col_builder = []

        # for q in range(len(row_builder)):
        #     row_builder[q] = ''.join("%3s" % c for c in row_builder[q])
        # print('\n'.join(row_builder))

    def print_grid_3(self):
        dds = self.direction_vector()
        grid = self._grid
        row_builder = []
        for r in range(len(grid)):
            col_builder = []
            for c in range(len(grid[0])):
                coord = (r, c)
                col_builder.append(coord)
            row_builder.append(col_builder)
            col_builder = []
        print('\n'.join(map(str, row_builder)))


# def is_sorted(lst):
#     for q in range(len(lst)-1):
#         assert lst[q] < lst[q+1], (q, q+1)




class Solution:
    def get_shortest_path(self):
        start_coord = 0, 0
        start = Path(start_coord,)
        if start.is_busted:
            return None

        if start.is_end:
            return start
        q = 0
        visited = set(start.last_coord,)
        queue = deque((start,))
        while queue:
            path: Path = queue.popleft()
            paths = path.next_paths()
            for p in paths:
                if p.is_end:
                    print(f"COMPLETED {repr(p)} in [{q}] iterations.")
                    return p
                if p.last_coord not in visited:
                    visited.add(p.last_coord)
                    queue.append(p)
            q += 1
            if q % 10000 == 0:
                print(f"{q}: {len(queue)}")
        return None

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        Path.set_grid(grid, k)
        shortest_p = self.get_shortest_path()
        return shortest_p
        # return shortest_p and shortest_p.num_steps or -1




grid_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
shortest_coords_1_0 = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19),(0,20),(0,21),(0,22),(0,23),(0,24),(0,25),(0,26),(0,27),(0,28),(0,29),(0,30),(0,31),(0,32),(0,33),(0,34),(0,35),(0,36),(0,37),(0,38),(0,39),(1,39),(2,39),(2,38),(2,37),(2,36),(2,35),(2,34),(2,33),(2,32),(2,31),(2,30),(2,29),(2,28),(2,27),(2,26),(2,25),(2,24),(2,23),(2,22),(2,21),(2,20),(2,19),(2,18),(2,17),(2,16),(2,15),(2,14),(2,13),(2,12),(2,11),(2,10),(2,9),(2,8),(2,7),(2,6),(2,5),(2,4),(2,3),(2,2),(2,1),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(4,12),(4,13),(4,14),(4,15),(4,16),(4,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),(4,24),(4,25),(4,26),(4,27),(4,28),(4,29),(4,30),(4,31),(4,32),(4,33),(4,34),(4,35),(4,36),(4,37),(4,38),(4,39),(5,39),(6,39),(6,38),(6,37),(6,36),(6,35),(6,34),(6,33),(6,32),(6,31),(6,30),(6,29),(6,28),(6,27),(6,26),(6,25),(6,24),(6,23),(6,22),(6,21),(6,20),(6,19),(6,18),(6,17),(6,16),(6,15),(6,14),(6,13),(6,12),(6,11),(6,10),(6,9),(6,8),(6,7),(6,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(8,15),(8,16),(8,17),(8,18),(8,19),(8,20),(8,21),(8,22),(8,23),(8,24),(8,25),(8,26),(8,27),(8,28),(8,29),(8,30),(8,31),(8,32),(8,33),(8,34),(8,35),(8,36),(8,37),(8,38),(8,39),(9,39),(10,39),(10,38),(10,37),(10,36),(10,35),(10,34),(10,33),(10,32),(10,31),(10,30),(10,29),(10,28),(10,27),(10,26),(10,25),(10,24),(10,23),(10,22),(10,21),(10,20),(10,19),(10,18),(10,17),(10,16),(10,15),(10,14),(10,13),(10,12),(10,11),(10,10),(10,9),(10,8),(10,7),(10,6),(10,5),(10,4),(10,3),(10,2),(10,1),(10,0),(11,0),(12,0),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12),(12,13),(12,14),(12,15),(12,16),(12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,23),(12,24),(12,25),(12,26),(12,27),(12,28),(12,29),(12,30),(12,31),(12,32),(12,33),(12,34),(12,35),(12,36),(12,37),(12,38),(12,39),(13,39),(14,39),(14,38),(14,37),(14,36),(14,35),(14,34),(14,33),(14,32),(14,31),(14,30),(14,29),(14,28),(14,27),(14,26),(14,25),(14,24),(14,23),(14,22),(14,21),(14,20),(14,19),(14,18),(14,17),(14,16),(14,15),(14,14),(14,13),(14,12),(14,11),(14,10),(14,9),(14,8),(14,7),(14,6),(14,5),(14,4),(14,3),(14,2),(14,1),(14,0),(15,0),(16,0),(16,1),(16,2),(16,3),(16,4),(16,5),(16,6),(16,7),(16,8),(16,9),(16,10),(16,11),(16,12),(16,13),(16,14),(16,15),(16,16),(16,17),(16,18),(16,19),(16,20),(16,21),(16,22),(16,23),(16,24),(16,25),(16,26),(16,27),(16,28),(16,29),(16,30),(16,31),(16,32),(16,33),(16,34),(16,35),(16,36),(16,37),(16,38),(16,39),(17,39),(18,39),(18,38),(18,37),(18,36),(18,35),(18,34),(18,33),(18,32),(18,31),(18,30),(18,29),(18,28),(18,27),(18,26),(18,25),(18,24),(18,23),(18,22),(18,21),(18,20),(18,19),(18,18),(18,17),(18,16),(18,15),(18,14),(18,13),(18,12),(18,11),(18,10),(18,9),(18,8),(18,7),(18,6),(18,5),(18,4),(18,3),(18,2),(18,1),(18,0),(19,0),(20,0),(20,1),(20,2),(20,3),(20,4),(20,5),(20,6),(20,7),(20,8),(20,9),(20,10),(20,11),(20,12),(20,13),(20,14),(20,15),(20,16),(20,17),(20,18),(20,19),(20,20),(20,21),(20,22),(20,23),(20,24),(20,25),(20,26),(20,27),(20,28),(20,29),(20,30),(20,31),(20,32),(20,33),(20,34),(20,35),(20,36),(20,37),(20,38),(20,39),(21,39),(22,39),(22,38),(22,37),(22,36),(22,35),(22,34),(22,33),(22,32),(22,31),(22,30),(22,29),(22,28),(22,27),(22,26),(22,25),(22,24),(22,23),(22,22),(22,21),(22,20),(22,19),(22,18),(22,17),(22,16),(22,15),(22,14),(22,13),(22,12),(22,11),(22,10),(22,9),(22,8),(22,7),(22,6),(22,5),(22,4),(22,3),(22,2),(22,1),(22,0),(23,0),(24,0),(24,1),(24,2),(24,3),(24,4),(24,5),(24,6),(24,7),(24,8),(24,9),(24,10),(24,11),(24,12),(24,13),(24,14),(24,15),(24,16),(24,17),(24,18),(24,19),(24,20),(24,21),(24,22),(24,23),(24,24),(24,25),(24,26),(24,27),(24,28),(24,29),(24,30),(24,31),(24,32),(24,33),(24,34),(24,35),(24,36),(24,37),(24,38),(24,39),(25,39),(26,39),(26,38),(26,37),(26,36),(26,35),(26,34),(26,33),(26,32),(26,31),(26,30),(26,29),(26,28),(26,27),(26,26),(26,25),(26,24),(26,23),(26,22),(26,21),(26,20),(26,19),(26,18),(26,17),(26,16),(26,15),(26,14),(26,13),(26,12),(26,11),(26,10),(26,9),(26,8),(26,7),(26,6),(26,5),(26,4),(26,3),(26,2),(26,1),(26,0),(27,0),(28,0),(28,1),(28,2),(28,3),(28,4),(28,5),(28,6),(28,7),(28,8),(28,9),(28,10),(28,11),(28,12),(28,13),(28,14),(28,15),(28,16),(28,17),(28,18),(28,19),(28,20),(28,21),(28,22),(28,23),(28,24),(28,25),(28,26),(28,27),(28,28),(28,29),(28,30),(28,31),(28,32),(28,33),(28,34),(28,35),(28,36),(28,37),(28,38),(28,39),(29,39),(30,39),(30,38),(30,37),(30,36),(30,35),(30,34),(30,33),(30,32),(30,31),(30,30),(30,29),(30,28),(30,27),(30,26),(30,25),(30,24),(30,23),(30,22),(30,21),(30,20),(30,19),(30,18),(30,17),(30,16),(30,15),(30,14),(30,13),(30,12),(30,11),(30,10),(30,9),(30,8),(30,7),(30,6),(30,5),(30,4),(30,3),(30,2),(30,1),(30,0),(31,0),(32,0),(32,1),(32,2),(32,3),(32,4),(32,5),(32,6),(32,7),(32,8),(32,9),(32,10),(32,11),(32,12),(32,13),(32,14),(32,15),(32,16),(32,17),(32,18),(32,19),(32,20),(32,21),(32,22),(32,23),(32,24),(32,25),(32,26),(32,27),(32,28),(32,29),(32,30),(32,31),(32,32),(32,33),(32,34),(32,35),(32,36),(32,37),(32,38),(32,39),(33,39),(34,39),(34,38),(34,37),(34,36),(34,35),(34,34),(34,33),(34,32),(34,31),(34,30),(34,29),(34,28),(34,27),(34,26),(34,25),(34,24),(34,23),(34,22),(34,21),(34,20),(34,19),(34,18),(34,17),(34,16),(34,15),(34,14),(34,13),(34,12),(34,11),(34,10),(34,9),(34,8),(34,7),(34,6),(34,5),(34,4),(34,3),(34,2),(34,1),(34,0),(35,0),(36,0),(36,1),(36,2),(36,3),(36,4),(36,5),(36,6),(36,7),(36,8),(36,9),(36,10),(36,11),(36,12),(36,13),(36,14),(36,15),(36,16),(36,17),(36,18),(36,19),(36,20),(36,21),(36,22),(36,23),(36,24),(36,25),(36,26),(36,27),(36,28),(36,29),(36,30),(36,31),(36,32),(36,33),(36,34),(36,35),(36,36),(36,37),(36,38),(36,39)]
shortest_coords_1_1 = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19),(0,20),(0,21),(0,22),(0,23),(0,24),(0,25),(0,26),(0,27),(0,28),(0,29),(0,30),(0,31),(0,32),(0,33),(0,34),(0,35),(0,36),(0,37),(0,38),(0,39),(1,39),(2,39),(3,39),(4,39),(5,39),(6,39),(6,38),(6,37),(6,36),(6,35),(6,34),(6,33),(6,32),(6,31),(6,30),(6,29),(6,28),(6,27),(6,26),(6,25),(6,24),(6,23),(6,22),(6,21),(6,20),(6,19),(6,18),(6,17),(6,16),(6,15),(6,14),(6,13),(6,12),(6,11),(6,10),(6,9),(6,8),(6,7),(6,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(8,15),(8,16),(8,17),(8,18),(8,19),(8,20),(8,21),(8,22),(8,23),(8,24),(8,25),(8,26),(8,27),(8,28),(8,29),(8,30),(8,31),(8,32),(8,33),(8,34),(8,35),(8,36),(8,37),(8,38),(8,39),(9,39),(10,39),(10,38),(10,37),(10,36),(10,35),(10,34),(10,33),(10,32),(10,31),(10,30),(10,29),(10,28),(10,27),(10,26),(10,25),(10,24),(10,23),(10,22),(10,21),(10,20),(10,19),(10,18),(10,17),(10,16),(10,15),(10,14),(10,13),(10,12),(10,11),(10,10),(10,9),(10,8),(10,7),(10,6),(10,5),(10,4),(10,3),(10,2),(10,1),(10,0),(11,0),(12,0),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12),(12,13),(12,14),(12,15),(12,16),(12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,23),(12,24),(12,25),(12,26),(12,27),(12,28),(12,29),(12,30),(12,31),(12,32),(12,33),(12,34),(12,35),(12,36),(12,37),(12,38),(12,39),(13,39),(14,39),(14,38),(14,37),(14,36),(14,35),(14,34),(14,33),(14,32),(14,31),(14,30),(14,29),(14,28),(14,27),(14,26),(14,25),(14,24),(14,23),(14,22),(14,21),(14,20),(14,19),(14,18),(14,17),(14,16),(14,15),(14,14),(14,13),(14,12),(14,11),(14,10),(14,9),(14,8),(14,7),(14,6),(14,5),(14,4),(14,3),(14,2),(14,1),(14,0),(15,0),(16,0),(16,1),(16,2),(16,3),(16,4),(16,5),(16,6),(16,7),(16,8),(16,9),(16,10),(16,11),(16,12),(16,13),(16,14),(16,15),(16,16),(16,17),(16,18),(16,19),(16,20),(16,21),(16,22),(16,23),(16,24),(16,25),(16,26),(16,27),(16,28),(16,29),(16,30),(16,31),(16,32),(16,33),(16,34),(16,35),(16,36),(16,37),(16,38),(16,39),(17,39),(18,39),(18,38),(18,37),(18,36),(18,35),(18,34),(18,33),(18,32),(18,31),(18,30),(18,29),(18,28),(18,27),(18,26),(18,25),(18,24),(18,23),(18,22),(18,21),(18,20),(18,19),(18,18),(18,17),(18,16),(18,15),(18,14),(18,13),(18,12),(18,11),(18,10),(18,9),(18,8),(18,7),(18,6),(18,5),(18,4),(18,3),(18,2),(18,1),(18,0),(19,0),(20,0),(20,1),(20,2),(20,3),(20,4),(20,5),(20,6),(20,7),(20,8),(20,9),(20,10),(20,11),(20,12),(20,13),(20,14),(20,15),(20,16),(20,17),(20,18),(20,19),(20,20),(20,21),(20,22),(20,23),(20,24),(20,25),(20,26),(20,27),(20,28),(20,29),(20,30),(20,31),(20,32),(20,33),(20,34),(20,35),(20,36),(20,37),(20,38),(20,39),(21,39),(22,39),(22,38),(22,37),(22,36),(22,35),(22,34),(22,33),(22,32),(22,31),(22,30),(22,29),(22,28),(22,27),(22,26),(22,25),(22,24),(22,23),(22,22),(22,21),(22,20),(22,19),(22,18),(22,17),(22,16),(22,15),(22,14),(22,13),(22,12),(22,11),(22,10),(22,9),(22,8),(22,7),(22,6),(22,5),(22,4),(22,3),(22,2),(22,1),(22,0),(23,0),(24,0),(24,1),(24,2),(24,3),(24,4),(24,5),(24,6),(24,7),(24,8),(24,9),(24,10),(24,11),(24,12),(24,13),(24,14),(24,15),(24,16),(24,17),(24,18),(24,19),(24,20),(24,21),(24,22),(24,23),(24,24),(24,25),(24,26),(24,27),(24,28),(24,29),(24,30),(24,31),(24,32),(24,33),(24,34),(24,35),(24,36),(24,37),(24,38),(24,39),(25,39),(26,39),(26,38),(26,37),(26,36),(26,35),(26,34),(26,33),(26,32),(26,31),(26,30),(26,29),(26,28),(26,27),(26,26),(26,25),(26,24),(26,23),(26,22),(26,21),(26,20),(26,19),(26,18),(26,17),(26,16),(26,15),(26,14),(26,13),(26,12),(26,11),(26,10),(26,9),(26,8),(26,7),(26,6),(26,5),(26,4),(26,3),(26,2),(26,1),(26,0),(27,0),(28,0),(28,1),(28,2),(28,3),(28,4),(28,5),(28,6),(28,7),(28,8),(28,9),(28,10),(28,11),(28,12),(28,13),(28,14),(28,15),(28,16),(28,17),(28,18),(28,19),(28,20),(28,21),(28,22),(28,23),(28,24),(28,25),(28,26),(28,27),(28,28),(28,29),(28,30),(28,31),(28,32),(28,33),(28,34),(28,35),(28,36),(28,37),(28,38),(28,39),(29,39),(30,39),(30,38),(30,37),(30,36),(30,35),(30,34),(30,33),(30,32),(30,31),(30,30),(30,29),(30,28),(30,27),(30,26),(30,25),(30,24),(30,23),(30,22),(30,21),(30,20),(30,19),(30,18),(30,17),(30,16),(30,15),(30,14),(30,13),(30,12),(30,11),(30,10),(30,9),(30,8),(30,7),(30,6),(30,5),(30,4),(30,3),(30,2),(30,1),(30,0),(31,0),(32,0),(32,1),(32,2),(32,3),(32,4),(32,5),(32,6),(32,7),(32,8),(32,9),(32,10),(32,11),(32,12),(32,13),(32,14),(32,15),(32,16),(32,17),(32,18),(32,19),(32,20),(32,21),(32,22),(32,23),(32,24),(32,25),(32,26),(32,27),(32,28),(32,29),(32,30),(32,31),(32,32),(32,33),(32,34),(32,35),(32,36),(32,37),(32,38),(32,39),(33,39),(34,39),(34,38),(34,37),(34,36),(34,35),(34,34),(34,33),(34,32),(34,31),(34,30),(34,29),(34,28),(34,27),(34,26),(34,25),(34,24),(34,23),(34,22),(34,21),(34,20),(34,19),(34,18),(34,17),(34,16),(34,15),(34,14),(34,13),(34,12),(34,11),(34,10),(34,9),(34,8),(34,7),(34,6),(34,5),(34,4),(34,3),(34,2),(34,1),(34,0),(35,0),(36,0),(36,1),(36,2),(36,3),(36,4),(36,5),(36,6),(36,7),(36,8),(36,9),(36,10),(36,11),(36,12),(36,13),(36,14),(36,15),(36,16),(36,17),(36,18),(36,19),(36,20),(36,21),(36,22),(36,23),(36,24),(36,25),(36,26),(36,27),(36,28),(36,29),(36,30),(36,31),(36,32),(36,33),(36,34),(36,35),(36,36),(36,37),(36,38),(36,39)]
gg2 = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]

inputs = (
    ([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 0, 10),
    ([[0,0,0],[0,1,0],[0,0,0],[0,1,1],[0,0,0]], 0, 6),
    ([[0,0,0],[1,1,0],[0,0,0],[0,1,0],[0,0,0]], 0, 6),
    ([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1, 6),
    ([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 2, 6),
    ([[0]], 0, 0),
    ([[0]], 1, 0),
    ([[0,1,1],[1,1,1],[1,0,0]], 0, -1),
    ([[0,1,1],[1,1,1],[1,0,0]], 1, -1),

    (grid_1, 0, 777),
    (grid_1, 1, 699),
    (grid_1, 2, 621),
    (grid_1, 3, 543),
    (grid_1, 4, 465),
    (grid_1, 5, 387),
)

def test():
    failed = 0
    for q, (grid, k, steps) in enumerate(inputs):
        shortest_p = Solution().shortestPath(grid, k)
        # shortest_p.print_grid()
        least_steps = shortest_p.num_steps if shortest_p is not None else -1
        # least_steps = Solution().shortestPath(grid, k)
        if steps != least_steps:
            print(f"{q} {steps == least_steps}: {steps} == {least_steps}  m x n == {len(grid)} x {len(grid[0])} == {len(grid)*len(grid[0])}")
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
    else:
        print("SUCCESS: ALL TESTS PASSED")
test()

@timer
def print_one(grid, k=0):
    # Path.set_grid(grid, k)
    p = Solution().shortestPath(grid, k)
    # print(p._dump_coords())
    p.print_grid()
# print_one(grid_1, 2)




def print_chars():
    f = lambda dx: lambda base: f'{base:>5}: ' + ' '.join(f'{chr(x)}' for x in range(base, base+dx))
    f = lambda dx: lambda base: f'{base:>5}: ' + ''.join(f'{chr(x)}' for x in range(base, base+dx))
    dx = 50
    mn = int(1e4)
    mx = 2*mn
    # ff = f(dx)

    dx = 20
    mn = 9460
    mx =9600
    for b in range(mn, mx, dx):
        line = f(dx)(b)
        print(line)

    # dx = 50
    # mn = 8500
    # mx = 10250
    # f = lambda dx: lambda base: f'{base:>5}: ' + ' '.join(f'{chr(x)}' for x in range(base, base+dx))
    # with open('unichars2.txt', 'w', encoding='utf-8') as fd:
    #     for b in range(mn, mx, dx):
    #         line = f(dx)(b)
    #         # print(line)
    #         fd.write(line)
    #         fd.write('\n')
# print_chars()
