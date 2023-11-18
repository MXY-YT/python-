import requests
from django.db import connection
from django.shortcuts import render

from models.mysqlConfig.models import Movies
from bs4 import BeautifulSoup

import re
import pandas as pd


# Create your views here.

# 返回视图给前端，在同级目录下的 urls 中被调用
# urls.py （ 需要自己新建 ） 中 写入以下内容
# urlpatterns = [
#     path('movie/', movie_list, name='movie_list'),
#     # path 第一个参数 url: 'http://localhost:8000/movie/',
#     # 第二个参数 函数，返回的内容（在本例子中的 def movie_list(request) 返回了一个视图 'user_list.html'，还有参数 {'users': users}）
#     # 第三个参数 name 可以自定义，可以方便被引用（无关紧要）
# ]

def get_movies(start):
    url = "https://movie.douban.com/top250?start=%d&filter=" % start
    lists = []
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) "
                      "Version/9.0 Mobile/13B143 Safari/601.1"}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")
    items = soup.find("ol", class_="grid_view").find_all("li")
    for i in items:
        movie = Movies()
        movie.name = i.find("span", "title").text
        movie.link = i.find("div", "pic").find("a").get("href")
        movie.directer = re.findall(re.compile(r'<p class="">(.*?)</p>', re.S), str(i))[0].replace("...<br/>",
                                                                                                   "").replace(
            "\n                            ", "")
        movie.score = float(i.find("span", "rating_num").text)
        movie.descr = i.find("span", "inq").text if (i.find("span", "inq")) else ""
        lists.append(movie)
    return lists


# 获取电影列表
def movie(request):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS mysqlconfig_movies")  # 删除数据库表
        createTab = """CREATE TABLE mysqlconfig_movies(
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(20) NOT NULL,
                link VARCHAR(50) NOT NULL,
                score FLOAT,
                descr VARCHAR(50),
                directer VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )"""
        cursor.execute(createTab)
    Movies.objects.all().delete()  # 删除数据库中的电影数据
    start = 0
    while start < 250:
        movies = get_movies(start)
        for movie in movies:
            movie.save()
        start += 25
    top_movies = Movies.objects.order_by('-score')[:10]
    return render(request, 'movie.html', {'movies': top_movies})


# 返回主页的视图
def index(request):
    return render(request, 'index.html')


# 获取评分页面
def score(request):
    score_list = []
    num_list = []
    with connection.cursor() as cursor:
        cursor.execute("select score,count(score) from mysqlconfig_movies group by score")
        data = cursor.fetchall()
        for item in data:
            score_list.append(item[0])
            num_list.append(item[1])

    return render(request, "score.html", {"score": score_list, "num": num_list})


def word(request):
    return render(request, "word.html")


def team(request):
    return render(request, "team.html")
