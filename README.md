# 项目结构

~~~shell
├── README.md
├── json 保存每个房间和座位的信息
│   ├── 101.json
│   ├── 202.json
│   ├── 203.json
│   ├── 204.json
│   ├── 205.json
│   ├── ........
├── libs
│   ├── __init__.py
│   ├── info.py 保存个人信息
│   ├── rsa.py RSA 加密算法的实现
│   └── source.py 核心代码
├── requirements.txt 依赖项
├── reserve.py 预约
└── sign.py 签到
~~~

<br/><br/>

# 运行

1. 克隆或者下载代码

2. 安装依赖

   ~~~shell
   pip install -r requirements.txt
   ~~~

3. 修改 `libs\info.py`文件，填上自己的学号、密码以及要预约的座位号

4. 运行 `reserve.py`即可预约，运行 `sign.py`可签到

<br/>

<br/>

# 部署

> 为了实现自动预约 + 自动签到, 需要每天定时执行预约和签到脚本。可以部署到**自己的电脑**、**服务器**、**云函数**、**GitHub Actions**。(若要部署到自己的电脑, 则需要一直开机)

* `reserve.py`预约脚本可于每天早上 6:15:40 执行, 因为系统每天 6:15 开放预约
* `sign.py`签到脚本可于预约时间的1分钟后执行, 比如预约 8:30~12:30, 可 8:31 执行签到

<br/>

1. 部署到 Windows 的可以使用计划任务定时执行脚本 (自行百度)

2. 部署到 Ubuntu/CentOS 服务器的可以使用 `crontab` 定时执行脚本 (自行百度)

3. **推荐部署到云函数(腾讯云函数、阿里云函数都行), 因为它们有免费额度, 相当于白嫖。**这里以阿里云函数为例

   1. 打开[阿里云官网](https://www.aliyun.com/), 注册阿里云账号

   2. 打开[函数计算页面](https://www.aliyun.com/product/fc)

      ![image-20230514115141532](https://img-blog.csdnimg.cn/0e99a68cb9294e0c9185887bb7e8839b.png)

   3. 点管理控制台

      

<br/>

<br/>

# 运行示例

* 预约成功示例

  <img src="https://img-blog.csdnimg.cn/00cf03bd51f1410eaeca5022f315f598.png" alt="image-20230514112415314" style="zoom:67%;" />



* 签到成功示例

  <img src="https://img-blog.csdnimg.cn/6ee31a0dd74941eeaa197474df1aee73.png" alt="image-20230514113116310" style="zoom:67%;" />

