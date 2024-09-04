#!/usr/bin/python3

import random
import os
class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.mines_set = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.non_mine_cells = width * height - mines
        self.revealed_non_mine_cells = 0

    def print_board(self, reveal=False):
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines_set:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines_set:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines_set:
            return False
        if self.revealed[y][x]:
            return True
        self.revealed[y][x] = True
        self.revealed_non_mine_cells += 1
        if self.revealed_non_mine_cells == self.non_mine_cells:
            self.print_board(reveal=True)
            print("Congratulations! You won!")
            return False
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    if (y * self.width + x) in self.mines_set:
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
