import imagehash

from imagehash import phash
from PIL import Image
import os
def image_similar_compare(img1, img2):
    # 以phash为栗子，其余hash方法也可以直接引用的
    hash1 = phash(Image.open(img1))
    hash2 = phash(Image.open(img2))
    # 计算汉明距离
    return 1 - (hash1 - hash2) / len(hash1.hash) ** 2

rootpath = 'D://test'
filepath = os.listdir(rootpath)
image_train = []
image_test = []
count_correct = 0
count_wrong = 0
for i in filepath:
    files = os.listdir('{}//{}'.format(rootpath, i))
    image_test.append('{}//{}//{}'.format(rootpath,i,files[0]))
    image_train.append('{}//{}//{}'.format(rootpath,i,files[-1]))
for i in range(len(image_test)):
    groupin_sim = image_similar_compare(image_train[i],image_test[i])
    sim_list = []
    for j in image_train:
        sim_list.append(image_similar_compare(image_test[i],j))
    if max(sim_list) > groupin_sim:
        count_wrong += 1
    else:
        count_correct +=1
print('正确率', count_correct/(count_wrong+count_correct))
#为了方便复现，可以先采用首位两张图片进行识别