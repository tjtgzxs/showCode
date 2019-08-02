import glob
import os
from PIL import Image

class handle_pic(object):
    def getPicPath(self,path):
        images=glob.glob(os.path.join(path,'*.jpg'))
        for image in images:
            im=Image.open(image)
            im.thumbnail((1920, 1280))#Resolution of xs
            print(im.format, im.size, im.mode)
            im.save(image,"JPEG")

if __name__=="__main__":
    handle=handle_pic()
    handle.getPicPath(".")