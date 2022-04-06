import tkinter as tk
import colors as color
tilesx = 0
tilesy = 0

class Game(tk.Frame):
    def __init__(self, w, h):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("4096")

        self.main_grid = tk.Frame(
            self, bg=color.GRID_COLOR, bd=3, width=w, height=h
        )
        self.main_grid.grid(pady=(100,0))

    def gui(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                tile_frame = tk.Frame(
                    self.main_grid, bg=color.EMPTY_CELL_COLOR, width=150, height=150
                )
                tile_frame.grid(row=i, column=j, padx=5, pady=5)
                tile_number = tk.Label(self.main_grid, bg=color.EMPTY_CELL_COLOR)


def main():
    x = input("Size X: ")
    y = input("Size Y: ")
    Game(int(x), int(y))

if __name__ == "__main__":
    main()