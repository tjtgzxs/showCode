"""
Talk is Cheap show me the code. --Linus Torvalds
generate 200 bargin codes
"""
import random
import string
class bargin(object):
    def __init__(self):
        self._code=string.ascii_letters
        self._code+=("".join([str(x) for x in range(0,10)]))


    def gene_code(self):
        code=""
        for i in range(4):
            for j in range(4):
               code+=random.choice(self._code)#random.choice return a random item in list/set/string
            if(i<=2): code+="-"
        return code

    def generateList(self,num):
        list=[]
        for i in range(num):
            code=self.gene_code()
            while code in list:
                code=self.gene_code()
            list.append(self.gene_code())
        return list



if __name__=="__main__":
    b=bargin()
    b.generateList(200)

