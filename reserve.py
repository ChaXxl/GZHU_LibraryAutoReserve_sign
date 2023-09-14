"""
预约
"""
import os
from libs.info import infos
from libs.source import ZWYT

if __name__ == '__main__':
    # action工作流
    # 获取secrets里面的数据
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    devName = os.getenv('DEVNAME')
    periods_string = os.getenv('PERIODS')
    pushplus = os.getenv('PUSHPLUS')
    pushplus = pushplus if pushplus else ''

    if username and password and devName and periods_string:
        try:
            # 初始化类示例，传入用户名、密码、时间段、推送token（推送可以为空）
            periods = eval(periods_string)
            yy = ZWYT('action', username, password, periods, pushplus)
            
            # 调用预约函数预约，传入预约座位号
            yy.reserve(devName)  
        except Exception as e:
            print(e)
            yy.pushplus("GitHub_Action预约失败", e)
    else:
        print("未配置GitHub Action必要参数，开始本地运行")

        # 本地运行
        # 遍历 info 信息，获取每个用户的昵称、预约座位号、用户名、密码、时间段、推送token（推送可以为空）
        for stu in infos:
            try:
                # 初始化类示例，传入昵称、用户名、密码、时间段、推送token（推送可以为空）
                yy = ZWYT(stu['name'], stu['sno'], stu['pwd'], stu['periods'], stu['pushplus'])
                
                # 调用预约函数预约，传入预约座位号
                yy.reserve(stu['devName'])  
            except Exception as e:
                print(e)
                yy.pushplus(stu['name']+"预约失败", e)
                continue
