# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as py

class CcPipeline(object):
    def open_spider(self,spider):
        self.db = py.connect(host='47.98.194.196',user='toutiao',password='toutiao',db='toutiao',charset='utf8')
        self.curs = self.db.cursor()

    def process_item(self, item, spider):
        tables = ""
        set_mysql = "SHOW TABLES;"
        self.curs.execute(set_mysql)
        allts = list(self.curs.fetchall())
        if len(allts) == 0:
            mksql = "DROP TABLE IF EXISTS {}".format(item['key'])
            self.curs.execute(mksql)
            mkbs = """CREATE TABLE {}(ID INT AUTO_INCREMENT PRIMARY KEY,TITLE CHAR (200),URL CHAR (200))""".format(item['key'])
            self.curs.execute(mkbs)
        elif len(allts) > 0:
            for table in allts:
                tables += table[0]
            if item['key'] not in tables:
                mksql = "DROP TABLE IF EXISTS {}".format(item['key'])
                self.curs.execute(mksql)
                mkbs = """CREATE TABLE {}(ID INT AUTO_INCREMENT PRIMARY KEY,TITLE CHAR (200),URL CHAR (200))""".format(
                    item['key'])
                self.curs.execute(mkbs)
        setsql = """INSERT INTO {}(TITLE,URL)VALUES (%s,%s)""".format(item['key'])
        data = item['name']
        print(data)
        self.curs.executemany(setsql,data)
        self.db.commit()
        return item


    def close_spider(self,spider):
        self.curs.close()
        self.db.close()