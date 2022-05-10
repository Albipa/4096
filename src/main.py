import tkinter as tk
import colors as c
import random
from time import sleep

class Game(tk.Frame):
    def __init__(self):
        """
           Summary: Constructor of the game. Specifies name and icon and size, and calls functions to create gui, bind the keys and run the game.
        """ 
        tk.Frame.__init__(self)
        
        self.grid()
        self.master.title('4096')
        self.master.iconbitmap('src/icon.ico')
        self.main_grid = tk.Frame(
            self, bg=c.grid_color, bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100,0))

        self.make_gui()
        self.start_game()

        self.bind_keys()

        self.mainloop()

    def make_gui(self):
        """
        Summary: Creates a GUI consisting of 4x4 cells and a score header.
        """
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.empty_cell_color,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.empty_cell_color)
                cell_number.grid(row=i,column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            font=c.score_label_font

        ).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.score_font)
        self.score_label.grid(row=1)


    def start_game(self):
        """
        Summary: Creates a 2d list of values and fills it with 0, Then spawns a random Two and configures it with the right color values. Also generates another and ensures that they arent in the same slot. Sets initial score value to 0.
        """ 
        # create matrix of zeroes
        self.matrix = [[0] * 4 for _ in range(4)]

        # fill 2 random cells with 2s
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.cell_colors[2])
        self.cells[row][col]["number"].configure(
            bg=c.cell_colors[2],
            fg=c.cell_number_colors[2],
            font=c.cell_number_fonts[2],
            text="2")
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.cell_colors[2])
        self.cells[row][col]["number"].configure(
            bg=c.cell_colors[2],
            fg=c.cell_number_colors[2],
            font=c.cell_number_fonts[2],
            text="2")

        self.score = 0

    def bind_keys(self):
        """
        Summary: Binds the movement functions to arrow keys on the keyboard.
        """
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
    
    def unbind_keys(self):
        """
        Summary: unbinds movement keys temporarily so game wont crash when losing or winning.
        """
        self.master.bind("<Left>", self.dummy)
        self.master.bind("<Right>", self.dummy)
        self.master.bind("<Up>", self.dummy)
        self.master.bind("<Down>", self.dummy)


    def stack(self):
        """
        Summary: Compress all 0 Values toward the left, and removing the gaps between, then fills empty cells.
        """ 
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix

    def combine(self):
        """
        Summary: Adds together all horizontally adjacent tiles of the same values and merges them to the left. If any merges happen, the respective score is added to the total.
        """
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]
    
    def reverse(self):
        """
        Summary: Reverse the order of each row in the matrix. 
        """
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix
    
    def transpose(self):
        """
        Summary: Flips the matrix over the diagonal.
        """
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    
    def add_new_tile(self):
        """
        Summary: Adds a 2 or 4 tile after each player move. Functions the exact same as the tiles generated at the start of the game.
        """
        row = random.randint(0,3)
        col = random.randint(0,3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = random.choice([2,4])
    
    def update_gui(self):
        """
        Summary: Updates the gui to match the matrix of values. Also updates the score label according to score value.
        """
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.empty_cell_color)
                    self.cells[i][j]["number"].configure(
                        bg=c.empty_cell_color, text="")
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=c.cell_colors[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.cell_colors[cell_value],
                        fg=c.cell_number_colors[cell_value],
                        font=c.cell_number_fonts[cell_value],
                        text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()
    
    def left(self, event):
        """
        Summary: Checks if a horizontal move is possible. If it is, compress The non-zero to the left of the matrix, then combine horizontally adjacent numbers and then eliminate newly created zeros. Then add new tiles, update the gui and check if game has been won/lost.
        input: event
        """
        if self.horizontal_move_exists():
            self.stack()
            self.combine()
            self.stack()
            self.add_new_tile()
            self.update_gui()
            self.game_over()
        else:pass


    def right(self, event):
        """
        Summary: Copy of the left function except that it reverses the matrix so the move can be treated as a left move.
        input: event
        """
        if self.horizontal_move_exists():
            self.reverse()
            self.stack()
            self.combine()
            self.stack()
            self.reverse()
            self.add_new_tile()
            self.update_gui()
            self.game_over()
        else:pass


    def up(self, event):
        """
        Summary: Copy of the left function except that it transposes the matrix so the move can be treated as a left move.
        input: event
        """
        if self.vertical_move_exists():
            self.transpose()
            self.stack()
            self.combine()
            self.stack()
            self.transpose()
            self.add_new_tile()
            self.update_gui()
            self.game_over()
        else:pass


    def down(self, event):
        """
        Summary: Copy of the left function except that it transposes and reverses the matrix so the move can be treated as a left move.
        input: event
        """
        if self.vertical_move_exists():
            self.transpose()
            self.reverse()
            self.stack()
            self.combine()
            self.stack()
            self.reverse()
            self.transpose()
            self.add_new_tile()
            self.update_gui()
            self.game_over()
        else:pass
    
    def dummy(self):
        """
        Summary: Does nothing.
        """
        pass

    def horizontal_move_exists(self):
        """
        Summary: Checks if a legal horizontal move is possible.
        """
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        return False

    def vertical_move_exists(self):
        """
        Summary: Checks if a legal vertical move is possible.
        """
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False

    def restartgame(self):
        """
        Summary: Restarts game by clearing all values of the matrix and calling restarting functions. also closes the lose/win window.
        """
        self.matrix.clear()
        self.start_game()
        self.update_gui()
        game_over_frame.withdraw()
        self.bind_keys()
        

    def game_over(self):
        """
        Summary: checks if the game has been won or lost(2048 on the board/if the board is full). Launches a independent window telling the user that they won/lost and offers a restart button.
        """
        global game_over_frame
        if any(2048 in row for row in self.matrix):
            self.unbind_keys()
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            game_over_frame = tk.Toplevel()
            tk.Label(
                game_over_frame,
                text="You win!",
                bg=c.winner_bg,
                fg=c.game_over_font_color,
                font=c.game_over_font).pack()
            tk.Button(
                game_over_frame,
                text="Play Again?",
                command=self.restartgame,
                bg=c.loser_bg,
                fg=c.game_over_font_color,
                font=c.game_over_font).pack()
        elif not any(0 in row for row in self.matrix):
            self.unbind_keys()
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            game_over_frame = tk.Toplevel()
            tk.Label(
                game_over_frame,
                text="Game over!",
                bg=c.loser_bg,
                fg=c.game_over_font_color,
                font=c.game_over_font).pack()
            tk.Button(
                game_over_frame,
                text="Try Again?",
                command=self.restartgame,
                bg=c.loser_bg,
                fg=c.game_over_font_color,
                font=c.game_over_font).pack()
    

    def randommoves(self):
        """
        Summary: Random moves so the game plays itself.
        """
        while True:
            randomchoice = random.randint(1,4)
            if randomchoice == 1:
                self.up()
            elif randomchoice == 2:
                self.down()
            elif randomchoice == 3:
                self.left()
            elif randomchoice == 4:
                self.right()
            sleep(1)
    
def main():
    Game()
    
if __name__ == "__main__":
    main()
    
    