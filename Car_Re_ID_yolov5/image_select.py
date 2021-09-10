import os
import shutil

def image_select(rootpath, io_dic):
    print('筛选上行车辆，请选择1，筛选下行车辆，请选择0，全部保留请输入-1')
    flag = eval(input())
    filename = os.listdir(rootpath)

    if flag == -1:
        number_select(rootpath)
        return
    elif flag == 0:
        for i in filename:
            if i not in io_dic['0']:

                print('{}{}'.format(rootpath, i))
                try:
                    shutil.rmtree('{}{}'.format(rootpath, i))
                    print('successfully delete {}{}'.format(rootpath, i))
                except:
                    print('sth error')
    elif flag == 1:
        for i in filename:
            if i not in io_dic['1']:

                print('{}{}'.format(rootpath, i))
                try:
                    shutil.rmtree('{}{}'.format(rootpath, i))
                    print('successfully delete {}{}'.format(rootpath, i))
                except:
                    print('sth error')
    number_select(rootpath)

#若含有图像超过10个，则选取其中最大（默认最大的代表清晰度最高，特征最多）的十个图像，舍弃其他图像
def number_select(rootpath):
    single_car_list = os.listdir(rootpath)
    for single_car in single_car_list:
        single_folder_path = '{}{}'.format(rootpath, single_car)
        files_path = os.listdir(single_folder_path)
        size_dic = {}
        for file in files_path:
            size_dic[file] = os.path.getsize('{}//{}'.format(single_folder_path, file))
            #对字典进行排序
        sorted(size_dic.items(),key=lambda item:item[1],reverse=True)
        count = 0
        for k,v in size_dic.items():
            if count > 9:
                os.remove('{}//{}'.format(single_folder_path, k))
            count += 1
            #print(count)



#从网上寻找的，一种删除文件夹及内部文件的方法，但是已经被弃用
def del_file(filepath):
    del_list = os.listdir(filepath)
    for file in del_list:
        file_path = os.path.join(filepath, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    os.rmdir(filepath)