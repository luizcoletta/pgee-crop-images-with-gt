import math
import cv2
import os
def image_process(data_name, tam_l,tam_c):
    name = data_name+'.png'
    img = cv2.imread('images/'+data_name+'/'+name)
    #data_troca = data_name.replace('-', 'L')
    annot = cv2.imread('images/'+data_name+'gt.png')

    s = img.shape
    tam_lar = s[0]
    larg = math.floor(tam_lar / tam_l)
    tam_com = s[1]
    comp = math.floor(tam_com / tam_c)
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
            annotName = f'{data_name}{"L"}{a}{"x"}{b}'
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