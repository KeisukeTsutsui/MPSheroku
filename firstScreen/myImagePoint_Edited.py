#2021-1-6更新
#筒井渓祐
#ワードバルーンのサイズを決める変数は不要になりました。
#文字のサイズと元の画像のサイズによりワードバルーンとテキストサイズが決まるようになりました。
#変数font_typeは１、２、３でそれぞれ大きい、普通、小さいです。
#HTMLから引っ張ってきてください引っ張ってきた場合７９行目を消してください
#ワードバルーンに入れれるテキストの最大数を増やすのお願いします




# coding: utf-8
import sys, os
import string
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
import cv2

from MPS.settings import BASE_DIR

points = np.zeros([1,1,2],dtype = int)


#画像に文字を入力する関数
def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=800):
    position = (width, height)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    #ここで文字数制限処理、多すぎると「...」でかき消されます。文字数制限を変更する場合は、上のmax_lengthを変更する。
    if draw.textsize(text, font=font)[0] > max_length:
        while draw.textsize(text + '…', font=font)[0] > max_length:
            text = text[:-1]
        text = text + '…'
    for i in text.splitlines(False):
        draw.text(position, i, font_color, font=font)
        height+=font_size
        position = (width, height)
    return img

#マウスの左クリックを完治するイベント関数
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        points[0] = [x,y]
 
class PaintingCreate:
    def merge(content, painting):
        title = content[0]
        text = content[1]
        ballon_type = content[2]
        # ballon_height = content[3]
        # ballon_wight = content[4]
        font_type = content[3]
        points[0] = [content[4],content[5]]
        PaintingName = 'firstScreen/static/' + painting

        #ベースとなる画像の名前を入力
        imgname = os.path.join(BASE_DIR, PaintingName)
        #ワードバルーンのタイプはどれですか。吹き出しの向きを選んでください。\n 1.左下\n 2.左上\n 3.右下\n 4.右上\n"
        balloonname = BASE_DIR
        if ballon_type=='1':
            balloonname = os.path.join(BASE_DIR,'firstScreen/static/CreatePainting/under_left.png')
        elif(ballon_type=='2'):
            balloonname = os.path.join(BASE_DIR,'firstScreen/static/CreatePainting/up_left.png')
        elif(ballon_type=='3'):
            balloonname = os.path.join(BASE_DIR,'firstScreen/static/CreatePainting/under_right.png')
        elif(ballon_type=='4'):
            balloonname = os.path.join(BASE_DIR,'firstScreen/static/CreatePainting/up_left.png')
        #吹き出しに、入れたい文字を入力
        msg = text
        max_msg_size = max([len(x) for x in msg.splitlines(False)])
        #画像タイトルを入力
        imgtittle = title
        
        # #画像の読み込み
        # print(sys.path)
        im1 = Image.open(imgname)
        im2 = Image.open(balloonname)
        
        #フォントサイズの定義
        #font_type = '1'
        width = im1.width
        if font_type=='1': #大きい
            font_size = int(width/40)
        elif(font_type=='2'): #普通
            font_size = int(width/60)
        elif(font_type=='3'): #小さい
            font_size = int(width/90)


        #ワードバルーンのサイズ
        img = cv2.imread(imgname)
        img2 = cv2.imread(balloonname)
        height = font_size * (len(msg)-3)
        width = font_size * (max_msg_size+5)
        im3 = cv2.resize(img2 , (int(width), int(height)))
        cv2.imwrite(os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/newWordballoon.png'),im3)
        im2 = Image.open(os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/newWordballoon.png'))


        #maskにする場合は.convert('L')でグレースケールに画像を変更しないとできない
        mask_im = Image.open(os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/newWordballoon.png')).convert('L')
        back_im = im1.copy()

        #クリックした座標を真ん中にワードバルーンを配置する座標を計算
        x = points[0][0][0]-(width/2)
        y = points[0][0][1]-(height/2)-int(font_size/130)
        # if ballon_type=='1':
        #     y=points[0][0][1]
        #     x=0
        # elif(ballon_type=='2'):
        #     y=0
        #     x=0
        # elif(ballon_type=='3'):
        #     y=points[0][0][1]
        #     x=points[0][0][0]
        # elif(ballon_type=='4'):
        #     y=0
        #     x=points[0][0][0]-(w/2)
        back_im.paste(im2,(int(x),int(y)),mask_im,)

        #ワードバルーンの中に入れるテキストの設定
        width = im1.width
        height = im1.height
        print((str)(width) + " " + str(height))
        base_img= back_im
        font_path= os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/myfont.ttc')
        #font_size= int(width/65)
        font_color=(0, 0, 0)
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(back_im)
        w, h = draw.textsize(msg,font)
        height=points[0][0][1]-(h/2)
        width=points[0][0][0]-(w/2)
        img = add_text_to_image(base_img, msg, font_path, font_size, font_color, height, width)
        saveimgname="firstScreen/static/save/"+imgtittle+".png"
        img.save(os.path.join(BASE_DIR, saveimgname), "PNG")


