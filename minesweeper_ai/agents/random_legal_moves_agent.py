from random import randint

from .agent import Agent


class RandomLegalMovesAgent(Agent):
    def nextMove(self):
        # print("grid is ({}, {})".format(len(self.grid)))
        x = randint(0, len(self.grid[0]) - 1)
        y = randint(0, len(self.grid) - 1)

        while self.isIllegalMove(x, y, False):
            x = randint(0, len(self.grid[0]) - 1)
            y = randint(0, len(self.grid) - 1)

        return (x, y, False)

    def isIllegalMove(self, x, y, toggle_flag):
        toggle_flag = False

        # Out of bounds
        if x < 0 or y < 0 or x >= len(self.grid[0]) or y >= len(self.grid):
            return True

        # Tile already uncovered
        if self.grid[y][x].uncovered:
            return True

        # Can't uncover a flagged tile
        if not toggle_flag and self.grid[y][x].is_flagged:
            return True

        return False

    def update(self, grid, mines_left, game_state):
        self.grid = grid
        self.mines_left = mines_left
        self.game_state = game_state

    def onGameBegin(self):
        pass

    def highlightTiles(self):
        pass
