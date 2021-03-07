import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar, Tab, Geo, Grid
from pyecharts.globals import ThemeType

# data = pd.DataFrame(pd.read_csv('../transport-data/trans-each-month.csv', header=0, encoding='utf-8'))
# date_list = np.array(data['date'])
# nom_list = np.array(data['nom'])
# noc_list = np.array(data['noc'])
place_list = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
              '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '新疆兵团']


# print(data)
# print(nom_list)
# print(noc_list)
def g1() -> Grid:
    c = (
        Bar(init_opts=opts.InitOpts(width="970px", height="550px"))
            .add_xaxis(
            [
                '北京', '\n天津', '河北', '\n山西', '内蒙古', '\n辽宁', '吉林', '\n黑龙江', '上海', '\n江苏', '浙江', '\n安徽', '福建', '\n江西',
                '山东',
                '\n河南', '湖北',
                '\n湖南', '广东', '\n广西', '海南', '\n重庆', '四川', '\n贵州', '云南', '\n西藏', '陕西', '\n甘肃', '青海', '\n宁夏', '新疆',
                '\n新疆兵团',
            ],

        )
            .add_yaxis("⭐",
                       [0, 0, 115.01, 0, 0, 100, 0, 128.03, 0, 0, 94.97, 0, 108.98, 0, 0, 98.16, 150, 0, 0, 0, 62.7, 0,
                        0, 106.56, 25.07, 0, 0, 0, 200, 91.43, 0, 0],
                       )
            .add_yaxis("⭐⭐",
                       [319.67, 161.15, 118.43, 115.47, 132.15, 197.27, 200.75, 169.27, 348.01, 169.13, 202.45, 137.91,
                        213.26, 181.48, 195.15, 134.44, 155.52, 128.07, 199.47, 128.65, 123.56, 138.48, 166.83, 159.58,
                        67.61, 253.96, 138.08, 131.78, 161.65, 101.28, 212.02, 172.78])
            .add_yaxis("⭐⭐⭐",
                       [371.39, 262.56, 215.16, 179.05, 196.33, 223.12, 230.01, 169.42, 347.65, 195.52, 262.17, 161.99,
                        245.57, 186.41, 226.56, 174.62, 191.06, 199.23, 252.65, 166.25, 166.33, 236.82, 217.11, 198.95,
                        134.26, 324.08, 177.16, 203.26, 214.8, 198.65, 253.58, 285.35])
            .add_yaxis("⭐⭐⭐⭐",
                       [503.52, 348.27, 309.25, 277.77, 298.78, 356.43, 299.76, 288.2, 505.24, 312.22, 355.71, 310.56,
                        365.06, 244.84, 351.77, 289.09, 281.62, 298.03, 338.54, 245.85, 241.22, 296.69, 302.55, 315.62,
                        221.62, 429.38, 291.76, 279.58, 304, 235.3, 343.69, 248.62])
            .add_yaxis("⭐⭐⭐⭐⭐",
                       [805.14, 502.45, 460.66, 374.11, 473.19, 518.22, 567, 485.06, 913.63, 504.48, 483.93, 349.16,
                        542.22, 350.95, 648.64, 473.14, 550.31, 409.44, 609.87, 475.96, 598.68, 473.28, 543.5, 542.08,
                        404.72, 770.33, 523.67, 445.57, 706.05, 0, 535, 0])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-0, interval='0')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    grid = (
        Grid()
            .add(c, grid_opts=opts.GridOpts(pos_bottom="10%", pos_left="5%"))
    )
    return grid


def g2() -> Grid:
    c = (
        Bar(init_opts=opts.InitOpts(width="970px", height="550px"))
            .add_xaxis(
            [
                '北京', '\n天津', '河北', '\n山西', '内蒙古', '\n辽宁', '吉林', '\n黑龙江', '上海', '\n江苏', '浙江', '\n安徽', '福建', '\n江西',
                '山东',
                '\n河南', '湖北',
                '\n湖南', '广东', '\n广西', '海南', '\n重庆', '四川', '\n贵州', '云南', '\n西藏', '陕西', '\n甘肃', '青海', '\n宁夏', '新疆',
                '\n新疆兵团',
            ],

        )
            .add_yaxis("⭐",
                       [0, 0, 125.24, 0, 0, 111.11, 0, 0, 0, 0, 125.94, 0, 122.46, 0, 0, 0, 238.1, 0, 0, 0, 55.11, 0, 0,
                        209.75, 68.76, 0, 0, 91.43, 138, 101.5, 0, 0],
                       )
            .add_yaxis("⭐⭐",
                       [372.69, 232.88, 172.14, 118.45, 123.34, 172.01, 144.02, 132.96, 336.22, 274.52, 212.86, 156.2,
                        215.06, 185.71, 283.15, 127.3, 188.98, 124.12, 295.4, 125.76, 102.99, 164.56, 169.03, 115.67,
                        136.13, 184.44, 141.43, 172.35, 98.18, 142.32, 135.27, 122.75])
            .add_yaxis("⭐⭐⭐",
                       [444.52, 314.42, 202.42, 240.01, 163.74, 260.28, 194.15, 206.32, 365.71, 215.84, 267.09, 169.18,
                        251.41, 169.7, 215, 190.91, 291.18, 187.02, 294.29, 153.93, 157.15, 217.17, 216.75, 226.47,
                        184.02,
                        189.03, 220.87, 197.14, 178.18, 153.85, 461.73, 300.46])
            .add_yaxis("⭐⭐⭐⭐",
                       [571.52, 397.54, 317.12, 268.62, 249.76, 294.69, 287.68, 324.95, 542.6, 335.52, 385.75, 295.42,
                        322.5, 259.36, 314.11, 292.34, 267.78, 304.94, 376.82, 259.78, 261.07, 329.36, 308.39, 328.46,
                        278.64, 343.64, 296.99, 312.3, 329.98, 241.27, 282.69, 427.14])
            .add_yaxis("⭐⭐⭐⭐⭐",
                       [929.89, 547.18, 416.27, 330.57, 426.13, 437.8, 539.59, 454.48, 994.81, 524.42, 483.33, 359.88,
                        557.5, 367.13, 549.76, 481.13, 564.31, 430.19, 640.7, 412.55, 641.01, 457.45, 538.63, 501.88,
                        436.08, 0, 566.53, 334.76, 395.17, 0, 337.62, 0])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-0, interval='0')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    grid = (
        Grid()
            .add(c, grid_opts=opts.GridOpts(pos_bottom="10%", pos_left="5%"))
    )
    return grid


def g3() -> Grid:
    c = (
        Bar(init_opts=opts.InitOpts(width="970px", height="550px"))
            .add_xaxis(
            [
                '北京', '\n天津', '河北', '\n山西', '内蒙古', '\n辽宁', '吉林', '\n黑龙江', '上海', '\n江苏', '浙江', '\n安徽', '福建', '\n江西',
                '山东',
                '\n河南', '湖北',
                '\n湖南', '广东', '\n广西', '海南', '\n重庆', '四川', '\n贵州', '云南', '\n西藏', '陕西', '\n甘肃', '青海', '\n宁夏', '新疆',
                '\n新疆兵团',
            ],

        )
            .add_yaxis("⭐",
                       [0, 0, 92.55, 0, 0, 0, 0, 0, 0, 0, 82.81, 0, 82.87, 0, 0, 0, 0, 0, 0, 0, 73.23, 54.95, 120.44,
                        110.14, 64.01, 0, 0, 104.9, 119.44, 0, 0, 0],
                       )
            .add_yaxis("⭐⭐",
                       [353.87, 124.41, 221.61, 92.59, 107.87, 129.27, 68.05, 123.83, 260.23, 122.57, 165.47, 155.44,
                        207.76, 150.96, 136.97, 105.07, 125.65, 127.63, 189.2, 117.26, 84.02, 265.82, 162.29, 110.16,
                        107.96, 193.1, 127.57, 131.73, 97.9, 223.28, 169.9, 150.69])
            .add_yaxis("⭐⭐⭐",
                       [416.1, 215.52, 170.73, 190.38, 138.31, 174.3, 176.12, 180.13, 284.45, 197.44, 247.19, 176.43,
                        269.78, 176.35, 188.6, 158.55, 169.2, 205.51, 258.14, 160.92, 160.82, 212.26, 218.62, 171.47,
                        155.37, 186.38, 162.82, 188.68, 124.75, 170.33, 164.81, 169.99])
            .add_yaxis("⭐⭐⭐⭐",
                       [563.25, 331.26, 297.73, 243.29, 237.8, 259.59, 248.27, 263.89, 478.77, 315.5, 319.44, 257.69,
                        290.09, 252.23, 290.31, 263.34, 302.5, 290.12, 329.6, 235.21, 299.81, 267.97, 293.99, 230.36,
                        263.63, 192.48, 249.51, 250.57, 190.53, 136.91, 196.45, 244.95])
            .add_yaxis("⭐⭐⭐⭐⭐",
                       [765.36, 431.08, 456.58, 286.75, 344.71, 378.73, 434.93, 552.1, 860.25, 466.74, 474.27, 381.59,
                        516.54, 322.24, 490, 529.47, 447.94, 413.66, 592.17, 403.24, 955.83, 433.29, 535.77, 507.09,
                        431.36, 268.43, 420.45, 512.02, 430.44, 0, 278.87, 0])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-0, interval='0')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    grid = (
        Grid()
            .add(c, grid_opts=opts.GridOpts(pos_bottom="10%", pos_left="5%"))
    )
    return grid


def g4() -> Grid:
    c = (
        Bar(init_opts=opts.InitOpts(width="970px", height="550px"))
            .add_xaxis(
            [
                '北京', '\n天津', '河北', '\n山西', '内蒙古', '\n辽宁', '吉林', '\n黑龙江', '上海', '\n江苏', '浙江', '\n安徽', '福建', '\n江西',
                '山东',
                '\n河南', '湖北',
                '\n湖南', '广东', '\n广西', '海南', '\n重庆', '四川', '\n贵州', '云南', '\n西藏', '陕西', '\n甘肃', '青海', '\n宁夏', '新疆',
                '\n新疆兵团',
            ],

        )
            .add_yaxis("⭐",
                       [0, 0, 86.31, 0, 0, 41.67, 0, 0, 0, 0, 111.03, 0, 108.27, 0, 0, 0, 0, 0, 0, 0, 63.03, 0, 127.06,
                        97.56, 71.67, 0, 0, 112.54, 140.01, 0, 0, 0],
                       )
            .add_yaxis("⭐⭐",
                       [377.56, 154.35, 193.1, 54.76, 136.58, 126.04, 124.63, 172.34, 177.93, 156.38, 183.19, 120.7,
                        166.94, 180.53, 138.05, 131.73, 157.87, 135.06, 214.04, 147.37, 128.83, 116.24, 154.75, 136.04,
                        140.88, 0, 158.79, 154.07, 107.08, 0, 197.99, 180.39])
            .add_yaxis("⭐⭐⭐",
                       [448.04, 237.94, 179.46, 130.49, 127.06, 196.47, 201.82, 143.49, 288.3, 190.07, 236.66, 169.38,
                        234.71, 167.43, 202.43, 177.1, 188.05, 215.86, 224.33, 164.83, 202.53, 221.56, 214.57, 189.95,
                        170.02, 247.9, 173.29, 185.41, 152.41, 182.99, 183.38, 178.84])
            .add_yaxis("⭐⭐⭐⭐",
                       [530.95, 385.01, 264.19, 214.97, 237.91, 320.75, 246.03, 257.55, 400.03, 305.07, 344.3, 265.55,
                        285.31, 235.28, 284.21, 258.35, 245.12, 342.77, 302.05, 222.52, 244.6, 293.96, 275.3, 288.99,
                        294.3, 240.84, 283.53, 246.38, 244.99, 0, 239.66, 283.81])
            .add_yaxis("⭐⭐⭐⭐⭐",
                       [635.75, 461.51, 435.4, 224.38, 330.8, 351.81, 413.43, 365.02, 735.77, 443.95, 461.62, 391.6,
                        475.06, 323.17, 463.21, 464.82, 475.14, 469.1, 537.76, 339.27, 521.66, 482.15, 484.3, 473.13,
                        404.73, 0, 459.42, 433.03, 454.32, 0, 291.03, 0])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-0, interval='0')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    grid = (
        Grid()
            .add(c, grid_opts=opts.GridOpts(pos_bottom="10%", pos_left="5%"))
    )
    return grid


tab = Tab()
tab.add(g1(), "2019Q3")
tab.add(g2(), "2019Q4")
tab.add(g3(), "2020Q1")
tab.add(g4(), "2020Q2")
tab.render("PER-Q2.html")
