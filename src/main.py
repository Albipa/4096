import tkinter as tk
import colors as color
tilesx = 600
tilesy = 600
#w, h
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("4096")
        self.main_grid = tk.Frame(self, bg=color.GRID_COLOR, bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100,0))

    def gui(self):
        self.tiles = []
        for i in range(4):
            row = []
            for j in range(4):
                tile_frame = tk.Frame(
                    self.main_grid, bg=color.EMPTY_CELL_COLOR, width=150, height=150
                )
                tile_frame.grid(row=i, column=j, padx=5, pady=5)
                tile_number = tk.Label(self.main_grid, bg=color.EMPTY_CELL_COLOR)
                tile_number.grid(row=i, column=j)
                tile_data = {"frame": cell_frame, "number": cell_number}
                row.append(tile_data)
            self.tiles.append(row)


def main():
    #x = input("Size X: ")
    #y = input("Size Y: ")int(x), int(y)
    Game()

if __name__ == "__main__":
    main()