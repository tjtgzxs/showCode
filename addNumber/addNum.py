"""
Talk is Cheap show me the code. --Linus Torvalds
add red number at a pic right head
"""
from PIL import Image,PSDraw,ImageDraw,ImageFont
import sys
class handle_pic(object):
    """
    use pillow to handle picture
    """
    def __init__(self,pic_path):
        self._pic=self.get_pic(pic_path)
        self._num=self.get_num()

    @classmethod
    def get_pic(cls,pic_path):
        im = Image.open(pic_path)
        return im

    @classmethod
    def get_num(cls):
        return  4

    def draw(self):
        base=self._pic.convert('RGBA')
        txt=Image.new("RGBA",base.size,(255,255,255,0))
        fnt=ImageFont.truetype("./DroidSans.ttf",size=100)
        d=ImageDraw.Draw(txt)
        d.text((base.size[0]*0.9, 10), str(self._num),fill=(255, 0, 0, 255),font=fnt)
        out = Image.alpha_composite(base, txt)

        out.show()

if __name__=="__main__":
    pic=handle_pic('./4.jpeg')
    pic.draw()

