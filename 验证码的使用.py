from PIL import Image,ImageFont, ImageDraw ,ImageFilter    #pip install pillow ,然后使用from PIL import Image
import random


def rand_chr():
    return chr(random.randint(65,90))   # 从a-z中
def rand_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rand_color1():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
def get_rand():
    for i in range(4):
        s=""
        n=random.randint(1,2)   #n==1 数字  n==2 字母
        if n==1:
            num=random.randint(0,9)
            s+=str(num)
        else:
            n1=random.randint(1,2)   #n==1 大写  n==2小写
            n2 = random.randint(1, 26)
            if n1==1:
                num=chr(64+n2)
                s+=num
            else:
                num = chr(96+n2)
                s += num
    return s

width=240
height=60
#创建字体对及文字大小
font=ImageFont.truetype("arial.ttf",36)

#这里会展示一张设定好的图片
image=Image.new("RGB",(width,height),(0,0,0))

draw=ImageDraw.Draw(image)
for i in range(width):
    for j in range(height):
        draw.point((i,j),fill=rand_color1())

for i in range(4):
    draw.text((60*i+10,10),get_rand(),font=font,fill=rand_color())
image=image.filter(ImageFilter.BLUR)
image.show()
image.save("yzm.jpg","jpeg")

