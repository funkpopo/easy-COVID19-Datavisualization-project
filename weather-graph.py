import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

date_list = ["2020/1/1", "2020/1/2", "2020/1/3", "2020/1/4", "2020/1/5", "2020/1/6", "2020/1/7", "2020/1/8", "2020/1/9",
             "2020/1/10", "2020/1/11", "2020/1/12", "2020/1/13", "2020/1/14", "2020/1/15", "2020/1/16", "2020/1/17",
             "2020/1/18", "2020/1/19", "2020/1/20", "2020/1/21", "2020/1/22", "2020/1/23", "2020/1/24", "2020/1/25",
             "2020/1/26", "2020/1/27", "2020/1/28", "2020/1/29", "2020/1/30", "2020/1/31"]
weather_list = ["晴", "晴", "多云", "小到中雨", "阵雨", "多云", "晴", "晴", "晴", "晴", "晴", "晴", "晴", "晴", "晴", "晴", "晴", "晴", "晴",
                "晴", "晴", "晴", "晴", "雨夹雪", "雨夹雪", "多云", "多云", "多云", "多云", "多云", "阵雨"]
h_tmp_list = [17, 18, 18, 18, 18, 19, 20, 18, 15, 15, 17, 19, 19, 20, 15, 14, 11, 11, 16, 20, 21, 21, 21, 21, 22, 21,
              19, 18, 20]
l_tmp_list = [4, 4, 5, 7, 7, 2, 2, 4, 3, 4, 4, 3, 4, 4, 3, 4, 2, 4, 2, 3, 4, 5, 3, 2, 0, 1, 1, 2, 4, 3, 4]

c = (
    Line(init_opts=opts.InitOpts(width="900px", height="450px", theme=ThemeType.DARK))
        .add_xaxis(xaxis_data=date_list)
        .add_yaxis(
        series_name="最高气温 Highest-Temp",
        y_axis=h_tmp_list,
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
        is_smooth=True,
    )
        .add_yaxis(
        series_name="最低气温 Lowest-Temp",
        y_axis=l_tmp_list,
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
            ]
        ),
        is_smooth=False,
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="2020/3-Weather-per-day", subtitle="Based on 'China weather report'."),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
        .render("data-into-py3.html")
)
