from collections import defaultdict

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Grid, Geo, Pie, WordCloud
from pyecharts.commons.utils import JsCode

from const import DB_CONFIG
from mysql_util import MysqlDB



color_function = """
        function (params) {
         var colorList = [
            '#2f4554', '#61a0a8', '#d48265', '#749f83', '#ca8622',
            '#6e7074', '#c23531', '#6d8346', '#F3A43B', '#60C0DD',
            '#C1232B','#B5C334','#FCCE10','#E87C25','#27727B',
            '#FE8463','#9BCA63','#FAD860','#F3A43B','#60C0DD',
            '#D7504B','#C6E579','#F4E001','#F0805A','#26C0C0'
        ];
        return colorList[params.dataIndex]
        }
        """


# 获取排名前十的影片
def movie_score_top_ten():
    db = MysqlDB(**DB_CONFIG)
    db.connection()

    sql = """
        SELECT movie_name, movie_score FROM douban_movie ORDER BY movie_score DESC LIMIT 10
    """

    response = db.fetch_all(sql)

    print(response)
    x_data = [v.get("movie_name") for v in response]
    y_data = [float(v.get("movie_score")) for v in response]


    c = (
        Bar(init_opts=opts.InitOpts(width='1400px', height='750px'))
            .add_xaxis(x_data)
            #
            .add_yaxis("评分", y_data,
                       itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )
            .set_global_opts(
            # 标题设置
            title_opts=opts.TitleOpts(
                title="Top10影片名称及评分",
                subtitle="柱形图",
                pos_left="center",  # 标题居中
            ),
            # 图例设置
            legend_opts=opts.LegendOpts(
                type_="scroll",
                is_show=True,
                orient="vertical",  # 图例布局朝向 horizontal: 左右  vertical:上下
                legend_icon="circle",  # 形状 circle:圆点 默认:方形
                pos_right="right"  # 图例放到最右侧

            ),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        )
            .render("./templates/Top10影片名称及评分.html")
    )


def movie_score_num():
    db = MysqlDB(**DB_CONFIG)
    db.connection()

    sql = """
            SELECT movie_name, movie_score, movie_num FROM douban_movie ORDER BY movie_score DESC 
        """

    response = db.fetch_all(sql)

    print(response)
    x_data = [v.get("movie_name") for v in response]
    y1_data = [float(v.get("movie_score")) for v in response]
    y2_data = [round(float(v.get("movie_num")) / 100000, 1) for v in response]

    print(y1_data)
    print(y1_data)

    (
        # 折线图对象
        Line(opts.InitOpts(
            width='1400px', height='750px',
            bg_color="#1A1835",
        ))
            # 设置图形的全局参数
            .set_global_opts(

            title_opts=opts.TitleOpts(
                title="影片评分及评论数",
                pos_left="center",  # 标题居中
                title_textstyle_opts={
                    "color": "#c4ccd3"
                }
            ),

            tooltip_opts=opts.TooltipOpts(is_show=False),
            legend_opts=opts.LegendOpts(
                pos_right="right",
                orient="vertical",  # 图例布局朝向 horizontal: 左右  vertical:上下
                textstyle_opts=opts.TextStyleOpts(
                    color='#90979c'
                )
            ),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=-15),
                type_="category",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(
                        color="rgba(204,187,225,0.5)"
                    )
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=False
                )
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(
                    is_show=True
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False
                ),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(
                        color="rgba(204,187,225,0.5)"
                    )
                ),

            ),
            datazoom_opts=opts.DataZoomOpts(
                is_show=True,
            )
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="影片评分",
            y_axis=y1_data,
            symbol="circle",
            symbol_size=10,
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color="#6f7de3"
            ),
            markpoint_opts=opts.MarkPointOpts(
                label_opts=opts.LabelOpts(
                    color='#fff'
                ),
                data=[opts.MarkPointItem(
                    type_='max',
                    name='最大值'
                ), opts.MarkPointItem(
                    type_='min',
                    name='最小值'
                )]
            )
        )
            .add_yaxis(
            series_name="评论数量（十万次）",
            y_axis=y2_data,
            symbol="circle",
            symbol_size=10,
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color="#c257F6"
            ),
            markpoint_opts=opts.MarkPointOpts(
                label_opts=opts.LabelOpts(
                    color='#fff'
                ),
                data=[opts.MarkPointItem(
                    type_='max',
                    name='最大值'
                ), opts.MarkPointItem(
                    type_='min',
                    name='最小值'
                )]
            )
        )
            .render("./templates/影片评分及评论数.html")
    )


def movie_num_by_movie_date():
    db = MysqlDB(**DB_CONFIG)
    db.connection()

    x_data = [
        ("1930至1979"),
        ("1980至1989"),
        ("1990至1999"),
        ("2000至2009"),
        ("2010至今")
    ]

    y1_data = []
    y2_data = []

    for movie_date in x_data:
        start_dt, end_dt = movie_date.split("至")

        start_dt = int(start_dt)

        if end_dt == "今":

            sql = """
                     SELECT count(1) as total, sum(movie_num) as total_num FROM douban_movie WHERE movie_date >= %s
                 """ % start_dt

            response = db.fetch_one(sql)
        else:
            end_dt = int(end_dt)
            sql = """
                                SELECT count(1) as total, sum(movie_num) as total_num FROM douban_movie WHERE movie_date >= %s AND movie_date <= %s
                            """ % (start_dt, end_dt)

            response = db.fetch_one(sql)

        y1_data.append(response.get("total"))
        y2_data.append(int(response.get("total_num") / 1000000))
    print(y1_data)
    print(y2_data)

    title = "各年代影片数量及评论数量"

    line = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis("评论（百万次）", y2_data, is_smooth=True)
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title,
                pos_left="center",  # 标题居中
                title_textstyle_opts={
                    "color": "#c4ccd3"
                }
            ),
            legend_opts=opts.LegendOpts(
                pos_right="right"
            ),
        )
    )

    bar = (
        Bar()
            .add_xaxis(x_data)
            .add_yaxis('', y1_data, itemstyle_opts=opts.ItemStyleOpts(color="#749f83"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
            legend_opts=opts.LegendOpts(
                pos_right="right"
            ),

        )
    )

    (Grid(init_opts=opts.InitOpts(width='1200px', height='700px',
                                  # bg_color="#1A1835"
                                  )
          )
     .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
     .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))

     ).render("./templates/各年代影片数量及评论数量.html")


def movie_type():

    db = MysqlDB(**DB_CONFIG)
    db.connection()

    sql = """
            SELECT movie_type FROM douban_movie 
        """

    response = db.fetch_all(sql)

    movie_type_list = [m for v in response for m in v.get("movie_type").split(",")]
    print(movie_type_list)

    movie_type_num = {}

    for info in movie_type_list:
        if movie_type_num.get(info):
            movie_type_num[info] += 1
        else:
            movie_type_num[info] = 1

    print(movie_type_num)

    data_pair = [[k, v] for k, v in movie_type_num.items()]
    data_pair.sort(key=lambda x: x[1])

    (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
            .add(
            series_name="访问来源",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["30%", "50%"],
            label_opts=opts.LabelOpts(is_show=False),

        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="影片类型占比",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            # legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="80%",
                                        textstyle_opts=opts.TextStyleOpts(color="#fff")),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item",
                formatter="{b}: {c} ({d}%)",
            ),

            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)", formatter="{b}: {c}", font_size=20),
        )
            .render("./templates/影片类型.html")
    )


def movie_word_cloud():
    db = MysqlDB(**DB_CONFIG)
    db.connection()

    sql = """
               SELECT movie_director, movie_actors FROM douban_movie 
           """

    response = db.fetch_all(sql)

    words_dict = defaultdict(int)

    for info in response:
        movie_director, movie_actors = info.get("movie_director"), info.get("movie_actors")
        name_list = movie_actors.split(",")
        name_list.append(movie_director)

        for name in name_list:
            words_dict[name] += 1

    (
        WordCloud()
            .add(
            "",
            list(words_dict.items()),
            word_size_range=[10, 100],
            textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="导演，演员词云图",
                pos_left="center",  # 标题居中
            ))
            .render("./templates/导演,演员词云图.html")
    )

def movie_time():
    x_data = [
        ("45-93分钟"),
        ("94-141分钟"),
        ("142-189分钟"),
        ("190-300分钟")
    ]

    y_data = []

    db = MysqlDB(**DB_CONFIG)
    db.connection()

    for info in x_data:
        st, et = info.replace("分钟", '').split("-")

        sql = "SELECT count(1) as total FROM douban_movie WHERE movie_time >= %s AND movie_time <= %s" % (st, et)

        response = db.fetch_one(sql)

        y_data.append(response.get("total"))

    (
        Pie()
            .add(
            "",
            [list(z) for z in zip(x_data, y_data)],
            center=["50%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="电影时长占比", pos_left="center"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}: {c}({d}%)", font_size=15)
        )
            .render("./templates/电影时长.html")
    )
# movie_score_top_ten()
# movie_score_num()
# movie_num_by_movie_date()
# movie_type()
# movie_word_cloud()

movie_time()



