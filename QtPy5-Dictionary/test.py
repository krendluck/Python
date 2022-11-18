import os
import re
import time

from deal import deal


def search(self, character, cursor):
    res = r'^[A-Za-z]+$'
    try:
        s = re.match(res, character).group()
        sql = 'SELECT * FROM ' + os.getenv("TABLENAME") + \
              " WHERE WORD = \'%s\'" % (s)
        for i in range(3):
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) != 0:
                    for row in result:
                        id = row[0]
                        word = row[1]
                        translate = row[2]
                        self.translate.setText(deal(translate))
                else:
                    self.translate.setText('查无此词')
                break
            except Exception as e:
                self.translate.setText("正在查询")
                time.sleep(1)
                print(e)
        else:
            if self.translate.text() == "正在查询":
                self.translate.setText("请重试")
    except Exception as e:
        print(e)
        self.translate.setText('输入格式出错')
