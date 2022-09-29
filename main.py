import arff  # Library https://pypi.org/project/liac-arff/. For read/write arff files
import cv2
import numpy as np
import os
import math
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
curr_dir = os.path.dirname(os.path.abspath(__file__))

'''# Retrieve the dicc from file arff
data_file_name = "ceratocystis_test_90_10_rgb_11_fs9_res20-Indexes.arff"
data_path = curr_dir + "/data/" + data_file_name
data = arff.load(open(data_path))'''

# Convert dicc to list. Only the data
'''lst_data = list(data.values())[3]

# Convert list to numeric int array
lst_data = np.array(lst_data)
num_data = lst_data.astype(float)
num_data = np.around(num_data)
num_data = num_data.astype(int)''' #não utilizar

# Get dir name from file arff
 #dirDataName = data_file_name[data_file_name.index("res"):data_file_name.index("-")]
# Load imgs
# le a matriz (imagem)
# colocar o nome da imagem que se deseja utilizar
data_name = 'Fake.png'

# tamanho desejado da largura x comprimento
tam_l = 50
tam_c = 50

# prepara o nome para a pasta e novas imagens
img_cont = (len(data_name))*-1
img_name = data_name[img_cont:data_name.find('.')]
img = cv2.imread('images/'+data_name)

# amazena os valores largura e comprimento
s = img.shape
tam_larg = s[0]
larg = math.floor(tam_larg/tam_l)
tam_comp = s[1]
comp = math.floor(tam_comp/tam_c)

# acumalador para a largura
row = 0

for a in range(larg):
    # acumalador para o comprimento
    length = 0
    for b in range(comp):
        if b < 1:
            cropped_img = img[row:row + tam_l, length:length + tam_c]
        else:
            cropped_img = img[row:row + tam_l,length + 1:length + tam_c + 1]
        imgName = f'{img_name}{"-"}{a}{"x"}{b}'
        dirname = 'results/' + img_name + '/images'

        if os.path.isdir(dirname):
            pass
        else:
            os.makedirs(dirname)

        # Save img not labeled
        cv2.imwrite(os.path.join(dirname, str(imgName) + '.png'), cropped_img)
        cv2.waitKey(0)
        length += tam_c

        #### FAZER AQUI EMBAIXO O MESMO COM IMAGEM QUE SE REFERE AO GT
        #### DIVIDIR EM PASTAS 'annotations' e 'images'

    row += tam_l



"""for l in num_data:

    # Get name for imgs cut
    imgName = f'{dirDataName}_{l[1]}_{l[2]}_{l[-1]}'
    # renomear com  DJI_0492-1x2, com os indices do for

    # Img not labeled

    cropped_img = img[l[1]:l[1] + 160, l[2]:l[2] + 192]  # img[start_row:end_row, start_col:end_col]

    # Create folder, if not exists
    dirname = 'results/' + 'Drone_492' + '/images'
    if os.path.isdir(dirname):
        pass
    else:
        os.makedirs(dirname)
    # Save img not labeled
    cv2.imwrite(os.path.join(dirname, str(imgName) + '.png'), cropped_img)
    cv2.waitKey(0)"""

    # Img labeled
    # cropped_imgLabeled = imgLabeled[l[1]:l[1] + 10, l[2]:l[2] + 10]  # img[start_row:end_row, start_col:end_col]
    # Create folder, if not exists
    # dirname = 'results/' + dirDataName + '/annotations'
    # if os.path.isdir(dirname):
    # else:
     #   os.makedirs(dirname)
    # Save img labeled
    # cv2.imwrite(os.path.join(dirname, str(imgName) + '.png'), cropped_imgLabeled)
   # cv2.waitKey(0)