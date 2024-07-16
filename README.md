# 简介
实现广州大学图书馆的座位自动预约、自动签到, 让你不再烦恼总是挑不到座位或者忘记签到。该项目可实现**多个用户**同时预约、签到，只需要在 `info.py` 填上多个用户信息即可。

<br/>

# 项目结构

~~~shell
├── README.md
├── json             # 保存每个房间和座位的信息
│   ├── 101.json
│   ├── 202.json
│   ├── 203.json
│   ├── 204.json
│   ├── 205.json
│   ├── ........
├── libs
│   ├── __init__.py
│   ├── info.py      # 保存个人信息
│   ├── rsa.py       # RSA 加密算法的实现
│   └── source.py    # 核心代码
├── requirements.txt # 依赖项
├── reserve.py       # 预约
└── sign.py          # 签到
~~~

<br/>

# 运行
下面的教程部署在服务器或云函数, 如需用 Github Action 部署, 请查看
1. 克隆或者下载代码

2. 安装依赖

   ~~~shell
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ~~~

3. 修改 `libs\info.py`文件，填上自己的学号、密码以及要预约的座位号

4. 运行 `reserve.py`即可预约，运行 `sign.py`可签到
   ~~~shell
   python reserve.py
   ~~~
   ~~~shell
   python sign.py
   ~~~

<br/>

# 待实现
- [ ] 一楼研讨间的预约和签到
- [ ] 五楼研讨间的预约和签到
- [x] 能自动签到对应预约的座位
- [ ] 摈弃 json 文件, 座位 ID 根据请求查询
- [x] 用户可自定义预约时间
- [ ] 处理教务系统要求改密码问题

<br/>

# 部署

> 为了实现自动预约 + 自动签到, 需要每天定时执行预约和签到脚本。可以部署到**自己的电脑**、**服务器**、**云函数**、**GitHub Actions**。(若要部署到自己的电脑, 则需要一直开机)

* `reserve.py`预约脚本可于每天早上 6:15:40 执行, 因为系统每天 6:15 开放预约
* `sign.py`签到脚本可于预约时间的1分钟后执行, 比如预约 8:30~12:30, 可 8:31 执行签到

<br/>

1. 部署到 Windows 的可以使用计划任务定时执行脚本 (自行百度)

2. 部署到 Ubuntu/CentOS 服务器的可以使用 `crontab` 定时执行脚本 (自行百度)

3. **推荐部署到云函数(腾讯云函数、阿里云函数都行), 因为它们有免费额度, 相当于白嫖**
   这里以阿里云函数为例

   1. 打开[阿里云官网](https://www.aliyun.com/), 注册阿里云账号

   2. 打开[函数计算页面](https://www.aliyun.com/product/fc)

      ![image-20230514115141532](https://img-blog.csdnimg.cn/0e99a68cb9294e0c9185887bb7e8839b.png)

   3. 点管理控制台
   
   4. 选择服务及函数，再点击创建服务，随便给个名字，例如我取名叫 `Library`
      ![image](https://github.com/ChaXxl/GZHU_LibraryAutoReserve_sign/assets/40326898/31bc937b-8f67-4579-b6ae-bb280fb77f1b)
      
   5. 创建`两个函数`，分别用于预约和签到。
         * 创建函数的方式：使用内置运行时创建
         * 函数名称：可以叫做 `Reserve` 和 `Sign`，随意
         * 请求处理程序类型：处理 HTTP 请求
         * 运行环境：Python 3.8 以上就行
         * 代码上传方式：可以选择通过文件夹 或 zip 包上传代码，反正上传代码就行
         * 执行超时时间：160 以上
         * 请求处理程序： 分别是`reserve.main`、`sign.main`(即执行 rserve.py 里的 main 函数和 sign.py 里的 main 函数)
         * 其余参数默认即可
         
         ![image-20231105092652349](https://img-blog.csdnimg.cn/36185a99601a47da818013f2b442aa53.png)
         
         
         
         ![image-20231105094104565](https://img-blog.csdnimg.cn/862e394da20b498fa9c023ba0ec917d3.png)
         
         <br/>
         
         两个函数示例：
         ![image](https://github.com/ChaXxl/GZHU_LibraryAutoReserve_sign/assets/40326898/59721804-99dc-4631-997b-f5b72457cfb4)
         
   6. 点击打开终端，输入以下命令安装依赖项
      * `-t .`: 表示将依赖安装置该目录下
      * `-r `: 指定对应的 requirements.txt 文件, 去安装这个文件里面的包     
      ~~~shell
      pip install -t . -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
      ~~~
      ![image](https://github.com/ChaXxl/GZHU_LibraryAutoReserve_sign/assets/40326898/dba1416d-9504-44ad-8b87-96b457b27e3f)
      
   7. 配置触发器
      * 触发器类型：选择异步调用
      * 触发器名称：随便起个
      
      * 预约函数的触发方式可以选我这个，我这个是每天 6:15:20 触发的意思
        ~~~shell
        CRON_TZ=Asia/Shanghai 20 15 6 * * *
        ~~~
        ![image](https://github.com/ChaXxl/GZHU_LibraryAutoReserve_sign/assets/40326898/7894b695-0eb0-4f90-8400-0cbed5ff23dd)
      * 签到函数的触发方式，我这个是每天的 8:21、8:31、8:35、8:55、12:31、13:55、16:31、20:31... 触发，弄这么多个触发点是为了以防万一签到失败，多来几次
        ~~~shell
        CRON_TZ=Asia/Shanghai 0 21,30,35,55 8,12,13,16,20 * * *
        ~~~
      
   8.  代码上传后记得点击部署，也可以点一下测试函数看看能不能正常运行，只要有输出就说明正常，`不用管它的报错`
   
      ![image](https://github.com/ChaXxl/GZHU_LibraryAutoReserve_sign/assets/40326898/1ffc4d34-9691-4291-bc6d-e813bcdb1581)


​      
​      
​      




​      

<br/>

<br/>

# 运行示例

* 预约成功示例

  <img src="https://img-blog.csdnimg.cn/00cf03bd51f1410eaeca5022f315f598.png" alt="image-20230514112415314" style="zoom:67%;" />



* 签到成功示例

  <img src="https://img-blog.csdnimg.cn/6ee31a0dd74941eeaa197474df1aee73.png" alt="image-20230514113116310" style="zoom:67%;" />

