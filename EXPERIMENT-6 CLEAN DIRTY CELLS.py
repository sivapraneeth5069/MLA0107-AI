class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.position = (0, 0)
    def move_up(self):
        if self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
    def move_down(self):
        if self.position[0] < self.rows - 1:
            self.position = (self.position[0] + 1, self.position[1])
    def move_left(self):
        if self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
    def move_right(self):
        if self.position[1] < self.cols - 1:
            self.position = (self.position[0], self.position[1] + 1)
    def clean_current_cell(self):
        self.grid[self.position[0]][self.position[1]] = 'Clean'
    def is_dirty(self):
        return self.grid[self.position[0]][self.position[1]] == 'Dirty'
    def is_all_clean(self):
        for row in self.grid:
            if 'Dirty' in row:
                return False
        return True
    def clean_environment(self):
        while not self.is_all_clean():
            if self.is_dirty():
                self.clean_current_cell()
            self.move_to_nearest_dirty_cell()
    def move_to_nearest_dirty_cell(self):
        dirty_cells = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'Dirty':
                    dirty_cells.append((i, j))
        if dirty_cells:
            nearest_dirty_cell = min(dirty_cells, key=lambda cell: abs(cell[0] - self.position[0]) + abs(cell[1] - self.position[1]))
            if nearest_dirty_cell[0] < self.position[0]:
                self.move_up()
            elif nearest_dirty_cell[0] > self.position[0]:
                self.move_down()
            if nearest_dirty_cell[1] < self.position[1]:
                self.move_left()
            elif nearest_dirty_cell[1] > self.position[1]:
                self.move_right()
grid = [
    ['Clean', 'Dirty', 'Clean'],
    ['Clean', 'Clean', 'Dirty'],
    ['Dirty', 'Clean', 'Clean']
]
vacuum_cleaner = VacuumCleaner(grid)
vacuum_cleaner.clean_environment()
print("Grid after cleaning:")
for row in grid:
    print(row)
