import pymysql as py
import Pub_articles
import time
import requests
from lxml import etree

se = requests.session()

while True:
    db = py.connect(host='47.98.194.196',user='toutiao',password='toutiao',db='toutiao',charset='utf8')
    curs = db.cursor()
    TABLES = "SHOW TABLES;"
    curs.execute(TABLES)
    tables = list(curs.fetchall())
    for table in tables:
        cycle = 0
        fromsql = "select * from {}".format(table[0])
        curs.execute(fromsql)
        result = list(curs.fetchall())
        if len(result) != 0:
            for base in result:

                if table[0] in base[1]:
                    alls = se.get("https://www.222zhe.com/search/"+base[1]).text
                    f = etree.HTML(alls)
                    title = f.xpath("//div[@class='pagewrapper']/div[@class='cardlist']/div[@class='card col span_1_of_4']/div[@class='shop-item']/h3/a/text()")
                    bases = ""
                    for tl in title:
                        bases += tl + "\n"
                    if base[1] in bases:
                        print("当前文章重复,准备跳到下一条！")
                        break
                    else:
                        articles = Pub_articles.articles.Pub_article(base[2])
                        print(articles)
                        if str(articles) != '视频文章':
                            try:

                                listarticle = list(articles)
                                Pub_articles.articles.Blog_article(table[0], listarticle[0], listarticle[1], listarticle[2])
                            except TypeError:
                                print('NoneType')
                        else:
                            print('暂时没文章')
                        Delete_sql = "DELETE FROM {} WHERE id = {}".format(table[0],base[0])
                        curs.execute(Delete_sql)
                        db.commit()
                        if cycle == 5:
                            print("当前{}分类已发布完成,正在准备延时~~~".format(table[0]))
                            time.sleep(5)
                            break
                        else:
                            cycle += 1
        else:
            print("当前{}数据库已无数据".format(table[0]))








