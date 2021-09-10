# Car_Re_ID_Attempt_baseonyolov5
This is an attempt on car Re_ID question by on Yolov5


1.车辆跟踪检测

![image](https://user-images.githubusercontent.com/61690115/132781073-990de531-5058-43c9-b52e-32aa5387e430.png)


2.车辆方向检测

![image](https://user-images.githubusercontent.com/61690115/132781212-3fdb0e24-ad9a-44eb-ab6a-221e04acc039.png)

3.根据选定方向保存一个方向的车辆截图

![image](https://user-images.githubusercontent.com/61690115/132781226-3ed85a26-f952-4ace-8ed8-85c8bc4aa6a0.png)

4.选择质量最高的10张图片作为训练集

![image](https://user-images.githubusercontent.com/61690115/132781333-65966692-63f4-467b-af5d-b8120373e1eb.png)

5.利用PHash方法对一段时间内的车辆进行自训练

![image](https://user-images.githubusercontent.com/61690115/132781362-367dd4ea-39ed-439a-be04-cef73a9d5101.png)

图像保存的根目录在main.py文件中58行设置
视频的位置在main.py 文件中的71行修改

在调用main.py 后，运行phash.py 获得图像重识别的自匹配成功率。

based on:
1.https://github.com/dyh/unbox_yolov5_deepsort_counting 行人跟踪检测项目
