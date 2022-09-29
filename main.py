import os
import numpy as np
import cv2
import math
from PIL import Image
from Process import image_process
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
curr_dir = os.path.dirname(os.path.abspath(__file__))


# colocar o nome da imagem que se deseja utilizar

data_name = 'DJI_0280-1x0'
# tamanho desejado da largura x comprimento
tam_l = 224
tam_c = 224


label_name = (data_name.replace('-',  'L'))+'.png'
im = Image.open('images/'+data_name+'/'+label_name)
img1 = np.array(im)
im = Image.fromarray(img1)
caminho_annot = 'images/'+data_name+'/'+data_name+'gt.png'
im.save(caminho_annot)


name = data_name+'.png'
img = cv2.imread('images/'+data_name+'/'+name)
annot = cv2.imread('images/'+data_name+'/'+data_name+'gt.png')


s = img.shape
tam_larg = s[0]
larg = math.floor(tam_larg / tam_l)
tam_comp = s[1]
comp = math.floor(tam_comp / tam_c)
row =0
for a in range(larg):
    # acumalador para o comprimento
    length = 0
    for b in range(comp):
        if b < 1:
            cropped_img = img[row:row + tam_l, length:length + tam_c]
            cropped_annot = annot[row:row + tam_l, length:length + tam_c]
        else:
            cropped_img = img[row:row + tam_l, length + 1:length + tam_c + 1]
            cropped_annot = annot[row:row + tam_l, length + 1:length + tam_c + 1]
        imgName = f'{data_name}{"-"}{a}{"x"}{b}'
        annotName = f'{data_name}{"-"}{a}{"x"}{b}'
        dirname = 'results/' + data_name + '/images'
        dirname2 = 'results/' + data_name + '/annotation'
        if os.path.isdir(dirname):
            pass
        else:
            os.makedirs(dirname)
        if os.path.isdir(dirname2):
            pass
        else:
            os.makedirs(dirname2)

        # Save img not labeled
        cv2.imwrite(os.path.join(dirname, str(imgName) + '.png'), cropped_img)
        cv2.imwrite(os.path.join(dirname2, str(annotName) + '.png'), cropped_annot)
        cv2.waitKey(0)
        length += tam_c

    row += tam_l