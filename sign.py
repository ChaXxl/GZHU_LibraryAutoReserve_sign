"""
签到
"""
from libs.info import infos
from libs.source import ZWYT


def main(*args, **kwargs):
    # 遍历 info 信息，获取每个用户的昵称、预约座位号、用户名、密码、时间段、推送token（推送可以为空）
    for stu in infos:
        try:
            # 初初始化类示例，传入昵称、用户名、密码、时间段、推送token（推送可以为空）
            yy = ZWYT(stu['name'], stu['sno'], stu['pwd'], stu['periods'], stu['pushplus'])

            # 调用签到函数进行签到，传入预约座位号
            yy.sign(stu['devName'])
        except Exception as e:
            print(e)
            if stu['pushplus']:
                yy.pushplus(f"{stu['name']} {stu['devName']} 签到失败", e)
            continue


if __name__ == '__main__':
    main()
