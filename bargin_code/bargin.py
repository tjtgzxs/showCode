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
               code+=random.choice(self._code)
            if(i<=2): code+="-"
        return code



if __name__=="__main__":
    b=bargin()
    b.gene_code()

