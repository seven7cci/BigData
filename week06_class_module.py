import pandas as pd
import tkinter as tk
import cilearn

def predict_life_satisfaction():
    x = int(en_GDP_per_capita.get())  # scalar input
    X_new = [[x]]

    # csv file download and data loading
    life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    # print(life_satisfaction.tail(5))
    # print(life_satisfaction.shape)
    # print(life_satisfaction.describe())

    X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d array
    y = life_satisfaction[["Life satisfaction"]].values  # return 2d array
    # print(X)
    # print(y)

    # model choice
    model = cilearn.LinearRegression()

    # model train
    model.fit(X, y)
    lbl_life_satisfaction.config(text=f"해당 국가의 삶의 만족도는 {model.predict(X_new)}으로 예상합니다.")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("삶의 만족도 예측 프로그램 v0.1")
    window.geometry("600x300")

    lbl_life_satisfaction = tk.Label(window, text="아래 입력상자에 삶의 만족도를 알소 싶은\n국가의 1인당 GDP값을 입력해주세요")
    en_GDP_per_capita = tk.Entry(window)
    btn_predict = tk.Button(window, text="에측", command=predict_life_satisfaction)

    lbl_life_satisfaction.pack()
    en_GDP_per_capita.pack(fill='x')
    btn_predict.pack(fill='x')

    window.mainloop()
