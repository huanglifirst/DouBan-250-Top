from flask import Flask, render_template

import create_html as cth

app = Flask(__name__)  # 注册Flask

"""
在这段代码中，@app.route('/') 和 @app.route('/top10') 是使用 Flask 框架时的装饰器（Decorator）用法。
装饰器是 Python 中的一种语法糖，它可以用来修改函数或类的行为。

在 Flask 框架中，@app.route('/') 和 @app.route('/top10') 用于指定 URL 路由和对应的处理函数。
当用户请求对应的 URL 时，Flask 将会调用相应的处理函数来处理请求并返回响应。

例如，当用户访问根路径（'/'）时，Flask 将会调用被 @app.route('/') 装饰的函数 index() 来处理请求。
同样地，当用户访问 '/top10' 路径时，Flask 将会调用被 @app.route('/top10') 装饰的函数 top_ten() 来处理请求。

这样的装饰器用法使得编写 Web 应用变得更加简洁和易读，同时也提供了路由和视图函数之间的关联。
"""


# @app.route() 装饰器来定义应用的路由。
# 装饰器下面的函数是该路由的视图函数，当访问对应的 URL 时，Flask 将执行这个函数。
@app.route('/')
def index():
    html_name = "index.html"
    return render_template(html_name)


@app.route('/top10')  # http://127.0.0.1:5000/top10
def top_ten():
    html_name = "Top10影片名称及评分.html"
    cth.movie_score_top_ten(html_name)
    print(999)
    return render_template(html_name)


@app.route('/movie_score_comment')
def movie_score_comment():
    html_name = "影片评分及评论数.html"
    cth.movie_score_comment(html_name)
    return render_template(html_name)


@app.route('/movie_comment_num')
def movie_comment_num():
    html_name = "各年代影片数量及评论数量.html"
    cth.movie_comment_num(html_name)
    return render_template(html_name)


@app.route('/movie_director_actors')
def movie_director_actors():
    html_name = "导演,演员词云图.html"
    cth.movie_director_actors(html_name)
    return render_template(html_name)


@app.route('/movie_type')
def movie_type():
    html_name = "影片类型.html"
    cth.movie_type(html_name)
    return render_template(html_name)


@app.route('/movie_time')
def movie_time():
    html_name = "电影时长.html"
    cth.movie_time(html_name)
    return render_template(html_name)


if __name__ == '__main__':
    app.run()
