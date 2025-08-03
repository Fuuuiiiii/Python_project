import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# 資料來源
data1=pd.read_csv(r"C:\Users\tzu49\OneDrive\文件\seminar1\4.salary\total_salary.csv",header=0,usecols=[0,1,3,4,5,6,13])
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

salary1 = list(data1["所有職業"])
salary2 = list(data1["藥事人員(含藥師)"])
salary3 = list(data1["醫學及病理檢驗人員"])
salary4 = list(data1["護理人員"])
salary5 = list(data1["呼吸治療師"])

#製圖
fig, ax = plt.subplots(figsize=(8,6),constrained_layout=True)
line1, = ax.plot([], [], label="所有職業",color="black",linestyle="--")
line2, = ax.plot([], [], label="藥師", color="#915BFA")
line3, = ax.plot([], [], label="醫檢", color="#52DAF5")
line4, = ax.plot([], [], label="護理", color="#FA5AC1")
line5, = ax.plot([], [], label="呼吸", color="#0400FA")
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

ax.set_xlim(min(years), max(years))
plt.ylim(35000, 70000)
ax.set_title("輪大夜",fontsize=20)
ax.set_ylabel("均月薪")
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=5)

# 動畫每幀更新函式
def update(i):
    x = years[:i+1]
    y1 = salary1[:i+1]
    y2 = salary2[:i+1]
    y3 = salary3[:i+1]
    y4 = salary4[:i+1]
    y5 = salary5[:i+1]
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    line4.set_data(x, y4)
    line5.set_data(x, y5)
    text.set_text(f"年份：{x[-1]}")
    return line1, line2, line3, line4, line5, text

# 建立動畫
ani = animation.FuncAnimation(fig, update, frames=len(years), interval=1000, blit=True)

# 輸出成 GIF
ani.save("salary_gif_1.gif", writer="pillow", fps=1)
print("✅ 已成功產出 salary_multi_line.gif！")