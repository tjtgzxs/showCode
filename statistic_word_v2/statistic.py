"""
Talk is Cheap show me the code. --Linus Torvalds
# statistic words of an English text in directory
"""
import glob
import os
if __name__=="__main__":
    txts=glob.glob(os.path.join("test","*.txt"))
    word_dict={}
    for txt in txts:
        with open(txt,'r') as o:
            lines=o.read().replace("\n"," ")
            words=lines.split(" ")
            for word in words:
                if not word in word_dict.keys():
                    word_dict[word]=0
                word_dict[word]+=1
    print(word_dict)
