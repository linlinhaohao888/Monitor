大作业说明文档
================
2016013238 软61 方梓唯 
2016013240 软61 林灏

## 实验环境

```
Python版本：3.6.6
Django版本：2.1.1
OS：Windows 10 Home
CPU：Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
RAM: 16GB
GPU: NVIDIA Geforce GTX 1070 with Max-Q Design
```

## 第三方库

* Keras：
  * 开发者：François Chollet及其它开发者
  * License：MIT
  * 实现功能：深度学习识别人脸表情、提取人脸特征

* TensorFlow-GPU：
  * 开发者：Google Brain Team
  * License：Apache 2.0 open source license
  * 实现功能：作为Keras后端支持
* Django：
  * 开发者：	Django Software Foundation
  * License：3-clause BSD
  * 实现功能：服务器后端框架
* matplotlib：	
  * 开发者：Michael Droettboom等
  * License：matplotlib license
  * 实现功能：绘制统计的情绪分布饼图
* skimage：
  * 开发者：Stéfan van der Walt
  * License：BSD License
  * 实现功能：图片维度转换
* scipy：
  * 开发者：Community library project
  * License：BSD-new license
  * 实现功能：计算人脸特征向量之间的欧几里得距离
* numpy：
  * 开发者：Community project
  * License：BSD-new license
  * 实现功能：数学运算
* OpenCV：
  * 开发者：Intel Corporation, Willow Garage, Itseez
  * License：BSD license
  * 实现功能：获取摄像头图像、图像转码处理
* face_classification:
  * 开发者：B-IT-BOTS robotics team
  * 来源：GitHub开源项目
  * 辅助实现功能：使用其训练好的Keras模型以及部分API，通过修改其源码实现表情识别、人脸位置检测
* facenet：
  * 开发者：davidsandberg
  * 来源：GitHub开源项目
  * 辅助实现功能：使用其训练好的Keras模型获取人脸特征，并添加功能实现注册用户的检测

## 实验功能

### 1、实验基本功能

#### 1.1 显示摄像头画面并进行人脸及表情识别

##### 1.1.1 实现人脸及表情识别及数据处理

* 在注册时打开摄像头，获取用户的人脸信息，使用已有CNN模型提取用户人脸特征并保存在数据库中
* 通过摄像头读取图像输入CNN模型判断人脸的位置以及人脸的表情，并将摄像头前的人脸与数据库进行对比，识别出摄像头前已经注册的用户。最终将人脸位置、表情、出现的注册用户用户名输出到画面上直观显示
* 对每一个摄像头前的注册用户的七种预设表情进行监控记录，将每一种表情所占的时间比例记录在对应的数据库用户表项中
##### 1.1.2 实现网络显⽰摄像头画⾯
* ⽹站服务搭建：使⽤Django框架
* ⽹站用户系统：
  I. ⽀持多⽤户，所有⽤户都可以通过⽹站的⽹页修改密码，并能重新校准录入的人脸信息
  II. 所有操作必须进⾏⽤户登录状态和权限的校验
  1） 使⽤session进⾏登录状态及权限校验
  2） session信息存储在服务器端持久化校验信息，设计有效时间为浏览器为关闭时有效，关闭后失效
* 使⽤Python读取摄像头画⾯，实现了：
  I. 使⽤OpenCV的Python库打开系统USB摄像头。
  II. ⽀持RTSP协议的⽹络摄像头

#### 1.2 预设管理员用户：

* 访问者可以通过在网页上输入的账号密码的方式来登录成为“管理员”
```
账号：Venessa
密码：www
```

* 管理员⽤户可以添加普通⽤户；管理员⽤户已事先添加好
* 管理员能够获取普通用户的用户名、邮箱，以及表情数据的分布饼图

### 2、拓展功能

* ⽀持RTSP协议的⽹络摄像头，在主页的相应位置输入地址连接即可
* 使⽤流媒体技术向前端推送视频流，使用Django的StreamingHttpResponse实现长连接进行推送M-JPEG
* 使⽤Python主动推送模式⽽不是轮询模式的消息提醒：后端主动检测人脸位置、表情以及人脸对应的用户并加以追踪和记录，并通过上述手段向客户端推送消息提醒、画面等

### 3 、附加功能

* 提供监控报警功能，后端会对摄像头中的画面进行分析，识别出画面中人脸对应的用户（需要注册人脸），并记录他们的表情变化，统计一段时间内各个情绪的比例，并存储在数据库中
* 当用户某一种情绪的比例大于一个预设的阈值（0.5）时，对特定网页发出主动进行推送消息提醒。后端会对消息进行查重处理，不会反复推送同一条消息
* 用户可以点击相应的按钮删除相应的历史提醒消息，页面上会显示出当前存在的所有历史消息
* 用户可以设置报警提醒的情绪比例阈值，值为0~1之间，程序会自行判断输入是否合法
## 程序使用

* 进入目录中，使用`python manage.py runserver`启动服务器
* 在Chrome中打开`http:127.0.0.1:8000/monitor`进入主页面
* 主页面中间部分为摄像头画面，右上角`LOGIN`和`SIGNUP`按钮分别能登录、注册
  * 注册页面需要填写用户名、邮箱、密码和确认密码，任何信息不合理都会被要求重新填写
  * 注册基本信息填写完毕并提交以后，会进入人脸注册页面，此时请把脸对准摄像头，注册页面会标注出当前的人脸位置，同时给出注册进度，待注册完成以后变回跳转回主页面并自动完成登录
  * 注册完或者登录完后回到主页，此时如果为普通用户登录，用户可以点击`ACCOUNT`按钮进入账户信息，此内的`CHANGE PASSWORD`和`CALIBRATE FACE`分别能修改密码或重新录入用户人脸信息。点击`LOGOUT`按钮可以退出登录
  * 如果登录用户为超级管理员账户，则多出一项`MANAGE`按钮，点击后可以看到所有用户用户名组成的列表，点击每一个表项可以查看对应用户的用户名、邮箱、表情分布图信息。列表右下角的+号可以添加普通用户
* 主页右上角输入框中可以输入RTSP网络摄像头地址，并点击`SUBMIT`获取其图像
* 进入`http:127.0.0.1:8000/monitor/alertPage`页面可以查看历史警告信息、获取最新警告的主动推送，并对历史信息进行删除
* 在警告页面右上角用户可以输入希望警示的阈值，从而改变用户的阈值设定，该阈值表示情绪比例高于此时会进行主动推送