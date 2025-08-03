import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# 資料來源
data1=pd.read_csv(r"C:\Users\tzu49\OneDrive\文件\seminar1\4.salary\total_salary.csv",header=0,usecols=[0,1,6,7,8,9,11,14])
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

salary1 = list(data1["所有職業"])
salary2 = list(data1["營養師"])
salary3 = list(data1["物理治療師"])
salary4 = list(data1["職能治療師"])
salary5 = list(data1["聽力及語言治療師"])
salary6 = list(data1["社工、心理專業人員(含諮商人員)"])

#製圖
fig, ax = plt.subplots(figsize=(8,6),constrained_layout=True)
line1, = ax.plot([], [], label="所有職業",color="black",linestyle="--")
line2, = ax.plot([], [], label="營養", color="#F9B575")
line3, = ax.plot([], [], label="物理", color="#024059")
line4, = ax.plot([], [], label="職能", color="#03A64A")
line5, = ax.plot([], [], label="聽語", color="#FAEA00")
line6, = ax.plot([], [], label="社工及諮商", color="#E10118")
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

ax.set_xlim(min(years), max(years))
plt.ylim(35000, 70000)
ax.set_title("不輪大夜",fontsize=20)
ax.set_ylabel("均月薪")
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=3)

# 動畫每幀更新函式
def update(i):
    x = years[:i+1]
    y1 = salary1[:i+1]
    y2 = salary2[:i+1]
    y3 = salary3[:i+1]
    y4 = salary4[:i+1]
    y5 = salary5[:i+1]
    y6 = salary6[:i+1]
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    line4.set_data(x, y4)
    line5.set_data(x, y5)
    line6.set_data(x, y6)
    text.set_text(f"年份：{x[-1]}")
    return line1, line2, line3, line4, line5,line6, text

# 建立動畫
ani = animation.FuncAnimation(fig, update, frames=len(years), interval=1000, blit=True)

# 輸出成 GIF
ani.save("salary_gif_2.gif", writer="pillow", fps=1)
# ani.save('animation.mp4', writer='ffmpeg',fps=1)
print("✅ 已成功產出！")
