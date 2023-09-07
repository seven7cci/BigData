import tkinter as tk  # built-in GUI


def factorial():
    n = int(en_number.get())  # 입력 상자에서 값을 꺼냄
    result = 1
    for i in range(2, n + 1):
        result = result * i
    lbl_factorial.config(text=f'{n}! = {result}')  # 레이블에 계산결과 출력


# print(factorial(5))


win = tk.Tk()
win.title("chap08 function")
win.geometry("300x150")

lbl_factorial = tk.Label(text="팩토리얼 계산 프로그램")  # 계산 결과 출력
en_number = tk.Entry()  # 숫자 입력

# command, text 키워드의 위치는 상관없다.
btn_calculate = tk.Button(text="계산!", command=factorial)

# 배치 (pack, grid, place)
lbl_factorial.pack()
en_number.pack()
btn_calculate.pack(fill="x")

win.mainloop()

# def do_nothing():
#     pass
#
# a = [1, 3, 5]
# print(do_nothing())
# print(a.pop())
# print(a.pop())
# print(a.remove(1))
# #pop과 remove의 차이 = pop은 값을 가져오고 지우지만 remove는 지우고 가져오기때문에 none이라 뜬다
# print(a)
