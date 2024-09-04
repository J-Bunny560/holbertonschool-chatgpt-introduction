#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    # ... (other methods)

    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.non_mine_cells = width * height - mines
        self.revealed_non_mine_cells = 0

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        self.revealed_non_mine_cells += 1
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def print_board(self, reveal=False):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and not reveal:
                    print('#', end=' ')
                elif (y * self.width + x) in self.mines:
                    print('*', end=' ')
                else:
                    print(self.count_mines_nearby(x, y), end=' ')
            print()

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                elif self.revealed_non_mine_cells == self.non_mine_cells:
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()