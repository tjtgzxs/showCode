"""
Talk is Cheap show me the code. --Linus Torvalds
# task 01 generate 200 bargin codes
# task 02 save code to mysql
# task 03 save code to redis
"""
import sys
import random
import string
sys.path.append("..")
from sql import Sql
from predis import predis

class bargin(object):
    def __init__(self):
        self._code = string.ascii_letters
        self._code += ("".join([str(x) for x in range(0, 10)]))

    def gene_code(self):
        code = ""
        for i in range(4):
            for j in range(4):
                code += random.choice(self._code)  # random.choice return a random item in list/set/string
            if (i <= 2): code += "-"
        return code

    def generateList(self, num):
        list = []
        for i in range(num):
            code = self.gene_code()
            while code in list:
                code = self.gene_code()
            list.append(self.gene_code())
        return list

    def insert_code(self, codes):
        for code in codes:
            Sql.insert('codes', code=code)
            r=predis()
            r.rpush(code=code)
        return True


if __name__ == "__main__":
    b = bargin()
    codes = b.generateList(200)
    b.insert_code(codes)
