import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd

# 資料來源
data1=pd.read_csv(r"C:\Users\tzu49\OneDrive\文件\seminar1\4.salary\total_salary.csv",header=0)
x_data = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]


salary1 = list(data1["所有職業"])
salary2  = list(data1["藥事人員(含藥師)"])
salary3  = list(data1["醫學及病理檢驗人員"])
salary4 = list(data1["護理人員"])
salary5 = list(data1["呼吸治療師"])
salary6 = list(data1["營養師"])
salary7 = list(data1["物理治療師"])
salary8 = list(data1["職能治療師"])
salary9 = list(data1["聽力及語言治療師"])
salary10 = list(data1["社工、心理專業人員(含諮商人員)"])

#繪製動態折線圖
(
# (
    Line(init_opts=opts.InitOpts(width="1400px", height="800px")) #畫布像素

        .add_xaxis(xaxis_data=x_data)

        .add_yaxis(

        series_name="所有職業",

        color="black",

        y_axis=salary1,

    ).add_yaxis(
    
        series_name="藥師",
    
        color='#00DDFF',
    
        y_axis=salary2,
    
       
    ).add_yaxis(
    
        series_name="醫檢",
    
        color='#37A2FF',
    
        y_axis=salary3,
    
    ).add_yaxis(
    
        series_name="護理",
    
        color='#FA5AC1',
    
        y_axis=salary4,
    ).add_yaxis(
    
        series_name="呼吸",
    
        color='#494FBF',
    
        y_axis=salary5,
        
    ).add_yaxis(

        series_name="營養",

        color='#F2BB16',

        y_axis=salary6,

       
    ).add_yaxis(

        series_name="物理",

        color='#F9B575',

        y_axis=salary7,

    ).add_yaxis(

        series_name="職能",

        color='#03A63C',

        y_axis=salary8,
        
        
    ).add_yaxis(

        series_name="聽語",

        color='#BDC0F2',

        y_axis=salary9,
        

    ).add_yaxis(

        series_name="社工與諮商",

        color='#E10118',

        y_axis=salary10,
            

    ).set_global_opts(

        tooltip_opts=opts.TooltipOpts(is_show=True, #一開始就呈現

                                      trigger='axis', 

                                      axis_pointer_type='cross'),

        #設定xy軸
        yaxis_opts=opts.AxisOpts(min_=35000,max_=70000,type_="value", name="月均薪"),

        xaxis_opts=opts.AxisOpts(boundary_gap=False, type_="category"),

    )
        #輸出
        .render("salary_total.html")

)

