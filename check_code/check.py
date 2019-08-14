import glob
import os
import re
def get_codes_in_dir(path):
    #test


    files=glob.glob(os.path.join(path,"*.py")) # Get all py files in directory
    total_count=0
    comment_count=0
    space_count=0
    code_count=0
    for file in files:
        with open(file,'r') as f:
            lines=f.readlines()
            for line in lines:
                total_count+=1
                regex1=re.compile(r"(\s*)#")
                regex2=re.compile(r"(\s*)$")
                if regex1.match(line):
                    comment_count+=1
                elif regex2.match(line):
                    space_count+=1
                else:
                    code_count+=1
    return {"code":code_count,"comment":comment_count,"space":space_count,'total':total_count}
if __name__=="__main__":
    count=get_codes_in_dir(".")
    print(count)