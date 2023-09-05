import tkinter as tk

# オセロボードのサイズ
BOARD_SIZE = 8

class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="green")
        self.canvas.pack()

        # オセロボードを描画
        self.draw_board()

        # クリックした位置に駒を配置
        self.canvas.bind("<Button-1>", self.place_piece)

    def draw_board(self):
        cell_size = 50
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x0, y0 = i * cell_size, j * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="green", outline="black")

    def place_piece(self, event):
        x, y = event.x, event.y
        cell_size = 50
        col = x // cell_size
        row = y // cell_size
        print(f"Placed piece at row {row}, col {col}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()