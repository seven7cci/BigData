# import random
import numpy as np
import tkinter as tk # Build in GUI
from tkinter import messagebox # pop-up window

"""
# v = np.array([1, 3, -9, 2])
# v = np.array([1, 3, -9, 2], dtype='int64')
v = np.array([[1, 3, -9, 2],[71, 13, -22, 7]], dtype='int64')
print(v.ndim, v.shape, v.data, v.dtype, v.strides) # ndim : 차원, shape : 배열, data : 메모리 주소, : dtype : 데이터 타입, strides : 메모리 간격

n = int(input("input number : "))
# l = list()
# for i in range(n):
#     l.append(random.randint(1, 100))
l = [random.randint(1, 100) for i in range(n)]
v = np.array(l, dtype='int16')
print(v)
# print(v.ndim, v.shape, v.data, v.dtype, v.strides)
"""

def press_enter_key(ev):
    click_button()
    messagebox.showinfo('x, y', f"({ev.x}, {ev.y})")


def click_button():
    try:
        r, c = map(int, en_row_column.get().split()) # spacebar
        # r = int(en_row.get())
        # c = int(en_column.get())
        # rows = [[random.randint(1,100) for i in range(r)] for i in range(c)]
        # matrix = np.array(create_2d_array(r,c), dtype='int16')
        matrix = np.random.randint(1, 101, size=(r, c))

        # matrix = np.array(rows, dtype='int16')
        lbl_result.config(text=matrix)
        # print(rows)
        # v = np.array(l, dtype='int16')

    except ValueError as err:
        # lbl_result.config(text=f"입력 값이 없습니다.\n{err}")
        messagebox.showerror("Error!", f"입력 값이 없습니다.\n{err}")
        # showinfo, showwarning


window = tk.Tk()
window.title('numpy gui version v1.8')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy array")
en_row_column = tk.Entry()
# en_column = tk.Entry()
btn_click = tk.Button(text="Click me", command=click_button)

# Enter Key Binding With Entry Widget

en_row_column.bind("<Return>", press_enter_key)

# widget layout
# lbl_result.place(x=50, y=50)
# btn_click.place(x=0, y=0)

# lbl_result.grid(row=0, column=0, columnspan=2)
# en_row.grid(row=1, column=0)
# en_column.grid(row=1, column=1)
# btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW) #E:east, W:west

lbl_result.pack()
en_row_column.pack(fill='x')
# en_column.grid(row=1, column=1)
btn_click.pack(fill='x') #E:east, W:west

# lbl_result.pack(side='right')
# en_number.pack(side='right')
# btn_click.pack(side='right')

window.mainloop()
# n = int(input("input number : "))
# l = [random.randint(1, 100) for i in range(n)]
# v = np.array(l, dtype='int16')
# print(v)