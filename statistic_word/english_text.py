"""
Talk is Cheap show me the code. --Linus Torvalds
# statistic words of an English text
"""
class statistic():
    def statistic(self,path):
        with open(path,'r') as o:
            lines=o.read().replace("\n","")
            statistic_count={}
            words=lines.split(" ")
            for word in words:
                if(not word in statistic_count.keys()):
                    statistic_count[word] =0
                statistic_count[word]+=1
            print(statistic_count)





if __name__=="__main__":
    s=statistic()
    s.statistic("./test.txt")
