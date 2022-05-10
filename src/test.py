import tkinter as tk
import colors as c
import random

master = tk.Tk()

master.geometry("200x200")

def opennewwindow():
            

        game = tk.Tk()
        game.title('4096')
        game.grid()
        main_grid = tk.Frame(
            game, bg=c.grid_color, bd=3, width=600, height=600
        )
        main_grid.grid(pady=(100,0))
        

        cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    main_grid,
                    bg=c.empty_cell_color,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(main_grid, bg=c.empty_cell_color)
                cell_number.grid(row=i,column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            cells.append(row)
        
        score_frame = tk.Frame(game)
        score_frame.place(relx=0.5, y=45, anchor="center")

        tk.Label(
            score_frame,
            text="Score",
            font=c.score_label_font

        ).grid(row=0)
        score_label = tk.Label(score_frame, text="0", font=c.score_font)
        score_label.grid(row=1)

        matrix = [[0] * 4 for _ in range(4)]

        row = random.randint(0,4)
        col = random.randint(0,4)
        cells[row][col]["frame"].configure(bg=c.cell_colors[2])
        cells[row][col]["number"].configure(
            bg=c.cell_colors[2],
            fg=c
        )


btn = tk.Button(master,
			text ="Click to open a new window",
			command = opennewwindow)
btn.pack(pady = 10)
master.mainloop()