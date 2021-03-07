import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar, Tab
from pyecharts.globals import ThemeType

# data = pd.DataFrame(pd.read_csv('../transport-data/trans-each-month.csv', header=0, encoding='utf-8'))
# date_list = np.array(data['date'])
# nom_list = np.array(data['nom'])
# noc_list = np.array(data['noc'])

# print(data)
# print(nom_list)
# print(noc_list)

c = (
    Bar(init_opts=opts.InitOpts(width="970px", height="545px"))
        .add_xaxis(
        [
            "19年10月运输量", "19年11月运输量", "19年12月运输量",
            "20年1月运输量", "20年2月运输量", "20年3月运输量",
            "20年4月运输量", "20年5月运输量", "20年6月运输量",
            "20年7月运输量", "20年8月运输量", "20年9月运输量",
            "20年10月运输量",
        ]
    )
        .add_yaxis("客运量", [2418, 2250, 2145, 2572, 605, 1008, 1266, 1373, 1527, 1714, 1952, 1904, 1795])
        .add_yaxis("货运量", [11271, 14300, 11300, 9051, 4808, 9947, 10955, 10542, 10795, 9700, 9863, 10866, 8507])
        .set_global_opts(
        title_opts=opts.TitleOpts(title="一年范围内运输状况     (单位：/万人；/万吨)",
                                  subtitle="Based on 'Department of Transport of Yunnan Province'."),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
        datazoom_opts=opts.DataZoomOpts(type_="inside"),
        toolbox_opts=opts.ToolboxOpts(),
    )
        .render('trans-graph.html')
)
