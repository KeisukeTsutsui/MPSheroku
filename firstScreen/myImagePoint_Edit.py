#2020-11-28
#筒井渓祐
#編集　児玉大聖
#ソフトウェア総合演習Ⅱ
#ワードバルーンの画像を元画像に貼り付けて、そのワードバルーン内にテキストを入力するプログラムです
#入力部分と出力部分を調整した(編集部分)

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
    draw.text(position, text, font_color, font=font)
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
        ballon_height = content[3]
        ballon_wight = content[4]
        points[0] = [content[5],content[6]]
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
        #画像タイトルを入力
        imgtittle = title
        
        # #画像の読み込み
        # print(sys.path)
        im1 = Image.open(imgname)
        im2 = Image.open(balloonname)

        #ワードバルーンのサイズを貼り付けられる画像のサイズの1/4に定義
        img = cv2.imread(imgname)
        img2 = cv2.imread(balloonname)
        height = ballon_height
        width = ballon_wight
        im3 = cv2.resize(img2 , (int(width), int(height)))
        cv2.imwrite(os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/newWordballoon.png'),im3)
        im2 = Image.open(os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/newWordballoon.png'))

        # print("ワードバルーンを差し込みたい場所をクリックして、その後Qキーを押してください。")
        # window = cv2.imread(imgname,1)
        # cv2.namedWindow("window",cv2.WINDOW_KEEPRATIO)
        # cv2.setMouseCallback("window",mouse_event)
        # while True:
        #     cv2.imshow("window",window)
        #     if cv2.waitKey(1) & 0xFF == ord("q"):
        #         break
        # cv2.destroyAllWindows()

        # #ワードバルーンの画像をペーストした座標を出力
        # print(points[0][0])

        #maskにする場合は.convert('L')でグレースケールに画像を変更しないとできない
        mask_im = Image.open(os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/newWordballoon.png')).convert('L')
        back_im = im1.copy()

        #クリックした座標を真ん中にワードバルーンを配置する座標を計算
        x = points[0][0][0]-(width/2)
        y = points[0][0][1]-(height/2)
        back_im.paste(im2,(int(x),int(y)),mask_im,)

        #画像に文字入力
        base_img=back_im
        font_path= os.path.join(BASE_DIR, 'firstScreen/static/CreatePainting/myfont.ttc')
        font_size=50
        font_color=(0, 0, 0)
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(back_im)
        w, h = draw.textsize(msg,font)
        height=points[0][0][1]-(h/2)
        width=points[0][0][0]-(w/2)
        img = add_text_to_image(base_img, msg, font_path, font_size, font_color, height, width)
        saveimgname="firstScreen/static/save/"+imgtittle+".png"
        img.save(os.path.join(BASE_DIR, saveimgname), "PNG")

        # #完成した画像を画面に出力。qでウィンドウ削除。
        # print("出来上がった画像を確認したら、Qキーを押してください。")
        # window = cv2.imread(saveimgname,1)
        # while True:
        #     cv2.imshow("widow",window)
        #     if cv2.waitKey(1) & 0xFF == ord("q"):
        #         break
        # cv2.destroyAllWindows()
