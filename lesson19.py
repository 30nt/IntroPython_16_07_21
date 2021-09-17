import random
from tkinter import *


FONT_SIZE = 100  # добавить параметр font_size, отвечающий за размер шрифта

class My15:
    def __init__(self):
        self._my_15 = self._generate_15()
        self._row, self._col = self._get_space()
        # table = {(0, 0): "4", (0, 1): "", (3, 3): "15"}
        # value = table[(self.row, self.col)]

    @property
    def my_15(self):
        return tuple([tuple(row) for row in self._my_15])

    def _generate_15(self):
        my_15 = []
        all_values = [str(i) for i in range(1, 16)] + [""]
        random.shuffle(all_values)
        for row_number in range(4):
            my_15.append(all_values[4 * row_number: 4 * (row_number + 1)])
        return my_15

    def _get_space(self):
        row_ = 0
        col_ = 0
        for i, row in enumerate(self._my_15):
            if '' in row:
                row_ = i
                for j, col in enumerate(row):
                    if '' == col:
                        col_ = j
        return row_, col_

    def move_down(self):
        if self._row == 3:
            return
        self._my_15[self._row][self._col], self._my_15[self._row + 1][self._col] = self._my_15[self._row + 1][
                                                                                       self._col], \
                                                                                   self._my_15[self._row][self._col]
        self._row += 1

    def move_up(self):
        if self._row == 0:
            return
        self._my_15[self._row][self._col], self._my_15[self._row - 1][self._col] = self._my_15[self._row - 1][
                                                                                       self._col], \
                                                                                   self._my_15[self._row][self._col]
        self._row -= 1

    def move_right(self):
        if self._col == 3:
            return
        self._my_15[self._row][self._col], self._my_15[self._row][self._col + 1] = self._my_15[self._row][
                                                                                       self._col + 1], \
                                                                                   self._my_15[self._row][self._col]
        self._col += 1

    def move_left(self):
        if self._col == 0:
            return
        self._my_15[self._row][self._col], self._my_15[self._row][self._col - 1] = self._my_15[self._row][
                                                                                       self._col - 1], \
                                                                                   self._my_15[self._row][self._col]
        self._col -= 1


def draw_15_table(my_15, font_size=FONT_SIZE):
    for row_index, row in enumerate(my_15.my_15):
        for col_index, col in enumerate(row):
            label = Entry(root, width=2, fg='white', bg='black', font=('Arial', font_size, 'bold'), justify='center')
            label.config(highlightbackground="black")
            label.grid(row=row_index, column=col_index)
            label.insert(END, col)


def left(event):
    my_15.move_left()
    draw_15_table(my_15)


def right(event):
    my_15.move_right()
    draw_15_table(my_15)


def up(event):
    my_15.move_up()
    draw_15_table(my_15)


def down(event):
    my_15.move_down()
    draw_15_table(my_15)


my_15 = My15()
root = Tk()
root.title("15")
root.geometry()
root.configure(background='black')
draw_15_table(my_15)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()
